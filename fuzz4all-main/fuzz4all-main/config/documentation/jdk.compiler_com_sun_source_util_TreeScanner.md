# Class TreeScanner<R,​P>

**Source:** `jdk.compiler\com\sun\source\util\TreeScanner.html`

### Class Description

```java
public class
TreeScanner<R,​P>

extends
Object

implements
TreeVisitor
<R,​P>
```

A TreeVisitor that visits all the child tree nodes.
To visit nodes of a particular type, just override the
corresponding visitXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of identifier nodes in a tree:

```java
class CountIdentifiers extends TreeScanner<Integer,Void> {
@Override
public Integer visitIdentifier(IdentifierTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

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

#### public TreeScanner()

*No description found.*

---

### Method Details

#### public
R
scan​(
Tree
tree,

P
p)

Scans a single node.

**Parameters:**
- tree

- the node to be scanned
- p

- a parameter value passed to the visit method

**Returns:**
- the result value from the visit method

---

#### public
R
scan​(
Iterable
<? extends
Tree
> nodes,

P
p)

Scans a sequence of nodes.

**Parameters:**
- nodes

- the nodes to be scanned
- p

- a parameter value to be passed to the visit method for each node

**Returns:**
- the combined return value from the visit methods.
The values are combined using the

reduce

method.

---

#### public
R
reduce​(
R
r1,

R
r2)

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:**
- r1

- the first of the values to be combined
- r2

- the second of the values to be combined

**Returns:**
- the result of combining the two parameters

---

#### public
R
visitCompilationUnit​(
CompilationUnitTree
node,

P
p)

Visits a CompilationUnitTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitPackage​(
PackageTree
node,

P
p)

Visits a PackageTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitImport​(
ImportTree
node,

P
p)

Visits an ImportTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitClass​(
ClassTree
node,

P
p)

Visits a ClassTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitMethod​(
MethodTree
node,

P
p)

Visits a MethodTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitVariable​(
VariableTree
node,

P
p)

Visits a VariableTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitEmptyStatement​(
EmptyStatementTree
node,

P
p)

Visits an EmptyStatementTree node. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitBlock​(
BlockTree
node,

P
p)

Visits a BlockTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitDoWhileLoop​(
DoWhileLoopTree
node,

P
p)

Visits a DoWhileTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitWhileLoop​(
WhileLoopTree
node,

P
p)

Visits a WhileLoopTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitForLoop​(
ForLoopTree
node,

P
p)

Visits a ForLoopTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitEnhancedForLoop​(
EnhancedForLoopTree
node,

P
p)

Visits an EnhancedForLoopTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitLabeledStatement​(
LabeledStatementTree
node,

P
p)

Visits a LabeledStatementTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitSwitch​(
SwitchTree
node,

P
p)

Visits a SwitchTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitCase​(
CaseTree
node,

P
p)

Visits a CaseTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitSynchronized​(
SynchronizedTree
node,

P
p)

Visits a SynchronizedTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitTry​(
TryTree
node,

P
p)

Visits a TryTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitCatch​(
CatchTree
node,

P
p)

Visits a CatchTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitConditionalExpression​(
ConditionalExpressionTree
node,

P
p)

Visits a ConditionalExpressionTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitIf​(
IfTree
node,

P
p)

Visits an IfTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitExpressionStatement​(
ExpressionStatementTree
node,

P
p)

Visits an ExpressionStatementTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitBreak​(
BreakTree
node,

P
p)

Visits a BreakTree node. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitContinue​(
ContinueTree
node,

P
p)

Visits a ContinueTree node. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitReturn​(
ReturnTree
node,

P
p)

Visits a ReturnTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitThrow​(
ThrowTree
node,

P
p)

Visits a ThrowTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitAssert​(
AssertTree
node,

P
p)

Visits an AssertTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitMethodInvocation​(
MethodInvocationTree
node,

P
p)

Visits a MethodInvocationTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitNewClass​(
NewClassTree
node,

P
p)

Visits a NewClassTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitNewArray​(
NewArrayTree
node,

P
p)

Visits a NewArrayTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitLambdaExpression​(
LambdaExpressionTree
node,

P
p)

Visits a LambdaExpressionTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitParenthesized​(
ParenthesizedTree
node,

P
p)

Visits a ParenthesizedTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitAssignment​(
AssignmentTree
node,

P
p)

Visits an AssignmentTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitCompoundAssignment​(
CompoundAssignmentTree
node,

P
p)

Visits a CompoundAssignmentTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitUnary​(
UnaryTree
node,

P
p)

Visits a UnaryTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitBinary​(
BinaryTree
node,

P
p)

Visits a BinaryTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitTypeCast​(
TypeCastTree
node,

P
p)

Visits a TypeCastTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitInstanceOf​(
InstanceOfTree
node,

P
p)

Visits an InstanceOfTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitArrayAccess​(
ArrayAccessTree
node,

P
p)

Visits an ArrayAccessTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitMemberSelect​(
MemberSelectTree
node,

P
p)

Visits a MemberSelectTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitMemberReference​(
MemberReferenceTree
node,

P
p)

Visits a MemberReferenceTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitIdentifier​(
IdentifierTree
node,

P
p)

Visits an IdentifierTree node. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitLiteral​(
LiteralTree
node,

P
p)

Visits a LiteralTree node. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitPrimitiveType​(
PrimitiveTypeTree
node,

P
p)

Visits a PrimitiveTypeTree node. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitArrayType​(
ArrayTypeTree
node,

P
p)

Visits an ArrayTypeTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitParameterizedType​(
ParameterizedTypeTree
node,

P
p)

Visits a ParameterizedTypeTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitUnionType​(
UnionTypeTree
node,

P
p)

Visits a UnionTypeTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitIntersectionType​(
IntersectionTypeTree
node,

P
p)

Visits an IntersectionTypeTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitTypeParameter​(
TypeParameterTree
node,

P
p)

Visits a TypeParameterTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitWildcard​(
WildcardTree
node,

P
p)

Visits a WildcardTypeTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitModifiers​(
ModifiersTree
node,

P
p)

Visits a ModifiersTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitAnnotation​(
AnnotationTree
node,

P
p)

Visits an AnnotatedTree node. This implementation scans the children in left to right order.

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
- the result of scanning

---

#### public
R
visitAnnotatedType​(
AnnotatedTypeTree
node,

P
p)

Visits an AnnotatedTypeTree node. This implementation scans the children in left to right order.

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
- the result of scanning

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

hierarchy. This implementation returns

null

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
- the result of scanning

---

#### public
R
visitErroneous​(
ErroneousTree
node,

P
p)

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:**
- visitErroneous

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
- the result of scanning

---

### Additional Sections

#### Class TreeScanner<R,​P>

java.lang.Object

- com.sun.source.util.TreeScanner<R,​P>

com.sun.source.util.TreeScanner<R,​P>

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

**Direct Known Subclasses:** TreePathScanner

```java
public class
TreeScanner<R,​P>

extends
Object

implements
TreeVisitor
<R,​P>
```

A TreeVisitor that visits all the child tree nodes.
To visit nodes of a particular type, just override the
corresponding visitXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of identifier nodes in a tree:

```java
class CountIdentifiers extends TreeScanner<Integer,Void> {
@Override
public Integer visitIdentifier(IdentifierTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

**Since:** 1.6

public class

TreeScanner<R,​P>

extends

Object

implements

TreeVisitor

<R,​P>

A TreeVisitor that visits all the child tree nodes.
To visit nodes of a particular type, just override the
corresponding visitXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of identifier nodes in a tree:

```java
class CountIdentifiers extends TreeScanner<Integer,Void> {
@Override
public Integer visitIdentifier(IdentifierTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

The default implementation of the visitXYZ methods will determine
a result as follows:

- If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of identifier nodes in a tree:

```java
class CountIdentifiers extends TreeScanner<Integer,Void> {
@Override
public Integer visitIdentifier(IdentifierTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

If the node being visited has no children, the result will be

null

.

If the node being visited has one child, the result will be the
result of calling

scan

on that child. The child may be a simple node
or itself a list of nodes.

If the node being visited has more than one child, the result will
be determined by calling

scan

each child in turn, and then combining the
result of each scan after the first with the cumulative result
so far, as determined by the

reduce(R, R)

method. Each child may be either
a simple node of a list of nodes. The default behavior of the

reduce

method is such that the result of the visitXYZ method will be the result of
the last child scanned.

Here is an example to count the number of identifier nodes in a tree:

```java
class CountIdentifiers extends TreeScanner<Integer,Void> {
@Override
public Integer visitIdentifier(IdentifierTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}
```

class CountIdentifiers extends TreeScanner<Integer,Void> {
@Override
public Integer visitIdentifier(IdentifierTree node, Void p) {
return 1;
}
@Override
public Integer reduce(Integer r1, Integer r2) {
return (r1 == null ? 0 : r1) + (r2 == null ? 0 : r2);
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreeScanner

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

reduce

​(

R

r1,

R

r2)

Reduces two results into a combined result.

R

scan

​(

Tree

tree,

P

p)

Scans a single node.

R

scan

​(

Iterable

<? extends

Tree

> nodes,

P

p)

Scans a sequence of nodes.

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

Constructor Summary

Constructors

Constructor

Description

TreeScanner

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

reduce

​(

R

r1,

R

r2)

Reduces two results into a combined result.

R

scan

​(

Tree

tree,

P

p)

Scans a single node.

R

scan

​(

Iterable

<? extends

Tree

> nodes,

P

p)

Scans a sequence of nodes.

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

Reduces two results into a combined result.

Scans a single node.

Scans a sequence of nodes.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TreeScanner

```java
public TreeScanner()
```

============ METHOD DETAIL ==========

- Method Detail

- scan

```java
public
R
scan​(
Tree
tree,

P
p)
```

Scans a single node.

**Parameters:** tree

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

- scan

```java
public
R
scan​(
Iterable
<? extends
Tree
> nodes,

P
p)
```

Scans a sequence of nodes.

**Parameters:** nodes

- the nodes to be scanned
**Parameters:** p

- a parameter value to be passed to the visit method for each node
**Returns:** the combined return value from the visit methods.
The values are combined using the

reduce

method.

- reduce

```java
public
R
reduce​(
R
r1,

R
r2)
```

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:** r1

- the first of the values to be combined
**Parameters:** r2

- the second of the values to be combined
**Returns:** the result of combining the two parameters

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

Visits a CompilationUnitTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a PackageTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an ImportTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ClassTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MethodTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a VariableTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an EmptyStatementTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a BlockTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a DoWhileTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a WhileLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ForLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an EnhancedForLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a LabeledStatementTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a SwitchTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a CaseTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a SynchronizedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a TryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a CatchTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ConditionalExpressionTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an IfTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an ExpressionStatementTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a BreakTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a ContinueTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a ReturnTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ThrowTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AssertTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MethodInvocationTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a NewClassTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a NewArrayTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a LambdaExpressionTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ParenthesizedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AssignmentTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a CompoundAssignmentTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a UnaryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a BinaryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a TypeCastTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an InstanceOfTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an ArrayAccessTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MemberSelectTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MemberReferenceTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an IdentifierTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a LiteralTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a PrimitiveTypeTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits an ArrayTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ParameterizedTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a UnionTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an IntersectionTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a TypeParameterTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a WildcardTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ModifiersTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AnnotatedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AnnotatedTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

hierarchy. This implementation returns

null

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
**Returns:** the result of scanning

- visitErroneous

```java
public
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:** visitErroneous

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
**Returns:** the result of scanning

Constructor Detail

- TreeScanner

```java
public TreeScanner()
```

---

#### Constructor Detail

TreeScanner

```java
public TreeScanner()
```

---

#### TreeScanner

public TreeScanner()

Method Detail

- scan

```java
public
R
scan​(
Tree
tree,

P
p)
```

Scans a single node.

**Parameters:** tree

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

- scan

```java
public
R
scan​(
Iterable
<? extends
Tree
> nodes,

P
p)
```

Scans a sequence of nodes.

**Parameters:** nodes

- the nodes to be scanned
**Parameters:** p

- a parameter value to be passed to the visit method for each node
**Returns:** the combined return value from the visit methods.
The values are combined using the

reduce

method.

- reduce

```java
public
R
reduce​(
R
r1,

R
r2)
```

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:** r1

- the first of the values to be combined
**Parameters:** r2

- the second of the values to be combined
**Returns:** the result of combining the two parameters

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

Visits a CompilationUnitTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a PackageTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an ImportTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ClassTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MethodTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a VariableTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an EmptyStatementTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a BlockTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a DoWhileTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a WhileLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ForLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an EnhancedForLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a LabeledStatementTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a SwitchTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a CaseTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a SynchronizedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a TryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a CatchTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ConditionalExpressionTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an IfTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an ExpressionStatementTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a BreakTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a ContinueTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a ReturnTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ThrowTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AssertTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MethodInvocationTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a NewClassTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a NewArrayTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a LambdaExpressionTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ParenthesizedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AssignmentTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a CompoundAssignmentTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a UnaryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a BinaryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a TypeCastTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an InstanceOfTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an ArrayAccessTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MemberSelectTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a MemberReferenceTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an IdentifierTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a LiteralTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits a PrimitiveTypeTree node. This implementation returns

null

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
**Returns:** the result of scanning

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

Visits an ArrayTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ParameterizedTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a UnionTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an IntersectionTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a TypeParameterTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a WildcardTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits a ModifiersTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AnnotatedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

Visits an AnnotatedTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

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

hierarchy. This implementation returns

null

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
**Returns:** the result of scanning

- visitErroneous

```java
public
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:** visitErroneous

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
**Returns:** the result of scanning

---

#### Method Detail

scan

```java
public
R
scan​(
Tree
tree,

P
p)
```

Scans a single node.

**Parameters:** tree

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

---

#### scan

public

R

scan​(

Tree

tree,

P

p)

Scans a single node.

scan

```java
public
R
scan​(
Iterable
<? extends
Tree
> nodes,

P
p)
```

Scans a sequence of nodes.

**Parameters:** nodes

- the nodes to be scanned
**Parameters:** p

- a parameter value to be passed to the visit method for each node
**Returns:** the combined return value from the visit methods.
The values are combined using the

reduce

method.

---

#### scan

public

R

scan​(

Iterable

<? extends

Tree

> nodes,

P

p)

Scans a sequence of nodes.

reduce

```java
public
R
reduce​(
R
r1,

R
r2)
```

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

**Parameters:** r1

- the first of the values to be combined
**Parameters:** r2

- the second of the values to be combined
**Returns:** the result of combining the two parameters

---

#### reduce

public

R

reduce​(

R

r1,

R

r2)

Reduces two results into a combined result.
The default implementation is to return the first parameter.
The general contract of the method is that it may take any action whatsoever.

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

Visits a CompilationUnitTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitCompilationUnit

public

R

visitCompilationUnit​(

CompilationUnitTree

node,

P

p)

Visits a CompilationUnitTree node. This implementation scans the children in left to right order.

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

Visits a PackageTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitPackage

public

R

visitPackage​(

PackageTree

node,

P

p)

Visits a PackageTree node. This implementation scans the children in left to right order.

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

Visits an ImportTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitImport

public

R

visitImport​(

ImportTree

node,

P

p)

Visits an ImportTree node. This implementation scans the children in left to right order.

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

Visits a ClassTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitClass

public

R

visitClass​(

ClassTree

node,

P

p)

Visits a ClassTree node. This implementation scans the children in left to right order.

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

Visits a MethodTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitMethod

public

R

visitMethod​(

MethodTree

node,

P

p)

Visits a MethodTree node. This implementation scans the children in left to right order.

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

Visits a VariableTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitVariable

public

R

visitVariable​(

VariableTree

node,

P

p)

Visits a VariableTree node. This implementation scans the children in left to right order.

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

Visits an EmptyStatementTree node. This implementation returns

null

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
**Returns:** the result of scanning

---

#### visitEmptyStatement

public

R

visitEmptyStatement​(

EmptyStatementTree

node,

P

p)

Visits an EmptyStatementTree node. This implementation returns

null

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

Visits a BlockTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitBlock

public

R

visitBlock​(

BlockTree

node,

P

p)

Visits a BlockTree node. This implementation scans the children in left to right order.

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

Visits a DoWhileTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitDoWhileLoop

public

R

visitDoWhileLoop​(

DoWhileLoopTree

node,

P

p)

Visits a DoWhileTree node. This implementation scans the children in left to right order.

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

Visits a WhileLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitWhileLoop

public

R

visitWhileLoop​(

WhileLoopTree

node,

P

p)

Visits a WhileLoopTree node. This implementation scans the children in left to right order.

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

Visits a ForLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitForLoop

public

R

visitForLoop​(

ForLoopTree

node,

P

p)

Visits a ForLoopTree node. This implementation scans the children in left to right order.

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

Visits an EnhancedForLoopTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitEnhancedForLoop

public

R

visitEnhancedForLoop​(

EnhancedForLoopTree

node,

P

p)

Visits an EnhancedForLoopTree node. This implementation scans the children in left to right order.

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

Visits a LabeledStatementTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitLabeledStatement

public

R

visitLabeledStatement​(

LabeledStatementTree

node,

P

p)

Visits a LabeledStatementTree node. This implementation scans the children in left to right order.

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

Visits a SwitchTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitSwitch

public

R

visitSwitch​(

SwitchTree

node,

P

p)

Visits a SwitchTree node. This implementation scans the children in left to right order.

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

Visits a CaseTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitCase

public

R

visitCase​(

CaseTree

node,

P

p)

Visits a CaseTree node. This implementation scans the children in left to right order.

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

Visits a SynchronizedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitSynchronized

public

R

visitSynchronized​(

SynchronizedTree

node,

P

p)

Visits a SynchronizedTree node. This implementation scans the children in left to right order.

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

Visits a TryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitTry

public

R

visitTry​(

TryTree

node,

P

p)

Visits a TryTree node. This implementation scans the children in left to right order.

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

Visits a CatchTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitCatch

public

R

visitCatch​(

CatchTree

node,

P

p)

Visits a CatchTree node. This implementation scans the children in left to right order.

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

Visits a ConditionalExpressionTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitConditionalExpression

public

R

visitConditionalExpression​(

ConditionalExpressionTree

node,

P

p)

Visits a ConditionalExpressionTree node. This implementation scans the children in left to right order.

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

Visits an IfTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitIf

public

R

visitIf​(

IfTree

node,

P

p)

Visits an IfTree node. This implementation scans the children in left to right order.

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

Visits an ExpressionStatementTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitExpressionStatement

public

R

visitExpressionStatement​(

ExpressionStatementTree

node,

P

p)

Visits an ExpressionStatementTree node. This implementation scans the children in left to right order.

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

Visits a BreakTree node. This implementation returns

null

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
**Returns:** the result of scanning

---

#### visitBreak

public

R

visitBreak​(

BreakTree

node,

P

p)

Visits a BreakTree node. This implementation returns

null

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

Visits a ContinueTree node. This implementation returns

null

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
**Returns:** the result of scanning

---

#### visitContinue

public

R

visitContinue​(

ContinueTree

node,

P

p)

Visits a ContinueTree node. This implementation returns

null

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

Visits a ReturnTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitReturn

public

R

visitReturn​(

ReturnTree

node,

P

p)

Visits a ReturnTree node. This implementation scans the children in left to right order.

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

Visits a ThrowTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitThrow

public

R

visitThrow​(

ThrowTree

node,

P

p)

Visits a ThrowTree node. This implementation scans the children in left to right order.

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

Visits an AssertTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitAssert

public

R

visitAssert​(

AssertTree

node,

P

p)

Visits an AssertTree node. This implementation scans the children in left to right order.

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

Visits a MethodInvocationTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitMethodInvocation

public

R

visitMethodInvocation​(

MethodInvocationTree

node,

P

p)

Visits a MethodInvocationTree node. This implementation scans the children in left to right order.

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

Visits a NewClassTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitNewClass

public

R

visitNewClass​(

NewClassTree

node,

P

p)

Visits a NewClassTree node. This implementation scans the children in left to right order.

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

Visits a NewArrayTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitNewArray

public

R

visitNewArray​(

NewArrayTree

node,

P

p)

Visits a NewArrayTree node. This implementation scans the children in left to right order.

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

Visits a LambdaExpressionTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitLambdaExpression

public

R

visitLambdaExpression​(

LambdaExpressionTree

node,

P

p)

Visits a LambdaExpressionTree node. This implementation scans the children in left to right order.

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

Visits a ParenthesizedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitParenthesized

public

R

visitParenthesized​(

ParenthesizedTree

node,

P

p)

Visits a ParenthesizedTree node. This implementation scans the children in left to right order.

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

Visits an AssignmentTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitAssignment

public

R

visitAssignment​(

AssignmentTree

node,

P

p)

Visits an AssignmentTree node. This implementation scans the children in left to right order.

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

Visits a CompoundAssignmentTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitCompoundAssignment

public

R

visitCompoundAssignment​(

CompoundAssignmentTree

node,

P

p)

Visits a CompoundAssignmentTree node. This implementation scans the children in left to right order.

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

Visits a UnaryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitUnary

public

R

visitUnary​(

UnaryTree

node,

P

p)

Visits a UnaryTree node. This implementation scans the children in left to right order.

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

Visits a BinaryTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitBinary

public

R

visitBinary​(

BinaryTree

node,

P

p)

Visits a BinaryTree node. This implementation scans the children in left to right order.

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

Visits a TypeCastTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitTypeCast

public

R

visitTypeCast​(

TypeCastTree

node,

P

p)

Visits a TypeCastTree node. This implementation scans the children in left to right order.

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

Visits an InstanceOfTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitInstanceOf

public

R

visitInstanceOf​(

InstanceOfTree

node,

P

p)

Visits an InstanceOfTree node. This implementation scans the children in left to right order.

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

Visits an ArrayAccessTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitArrayAccess

public

R

visitArrayAccess​(

ArrayAccessTree

node,

P

p)

Visits an ArrayAccessTree node. This implementation scans the children in left to right order.

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

Visits a MemberSelectTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitMemberSelect

public

R

visitMemberSelect​(

MemberSelectTree

node,

P

p)

Visits a MemberSelectTree node. This implementation scans the children in left to right order.

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

Visits a MemberReferenceTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitMemberReference

public

R

visitMemberReference​(

MemberReferenceTree

node,

P

p)

Visits a MemberReferenceTree node. This implementation scans the children in left to right order.

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

Visits an IdentifierTree node. This implementation returns

null

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
**Returns:** the result of scanning

---

#### visitIdentifier

public

R

visitIdentifier​(

IdentifierTree

node,

P

p)

Visits an IdentifierTree node. This implementation returns

null

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

Visits a LiteralTree node. This implementation returns

null

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
**Returns:** the result of scanning

---

#### visitLiteral

public

R

visitLiteral​(

LiteralTree

node,

P

p)

Visits a LiteralTree node. This implementation returns

null

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

Visits a PrimitiveTypeTree node. This implementation returns

null

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
**Returns:** the result of scanning

---

#### visitPrimitiveType

public

R

visitPrimitiveType​(

PrimitiveTypeTree

node,

P

p)

Visits a PrimitiveTypeTree node. This implementation returns

null

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

Visits an ArrayTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitArrayType

public

R

visitArrayType​(

ArrayTypeTree

node,

P

p)

Visits an ArrayTypeTree node. This implementation scans the children in left to right order.

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

Visits a ParameterizedTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitParameterizedType

public

R

visitParameterizedType​(

ParameterizedTypeTree

node,

P

p)

Visits a ParameterizedTypeTree node. This implementation scans the children in left to right order.

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

Visits a UnionTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitUnionType

public

R

visitUnionType​(

UnionTypeTree

node,

P

p)

Visits a UnionTypeTree node. This implementation scans the children in left to right order.

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

Visits an IntersectionTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitIntersectionType

public

R

visitIntersectionType​(

IntersectionTypeTree

node,

P

p)

Visits an IntersectionTypeTree node. This implementation scans the children in left to right order.

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

Visits a TypeParameterTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitTypeParameter

public

R

visitTypeParameter​(

TypeParameterTree

node,

P

p)

Visits a TypeParameterTree node. This implementation scans the children in left to right order.

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

Visits a WildcardTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitWildcard

public

R

visitWildcard​(

WildcardTree

node,

P

p)

Visits a WildcardTypeTree node. This implementation scans the children in left to right order.

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

Visits a ModifiersTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitModifiers

public

R

visitModifiers​(

ModifiersTree

node,

P

p)

Visits a ModifiersTree node. This implementation scans the children in left to right order.

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

Visits an AnnotatedTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitAnnotation

public

R

visitAnnotation​(

AnnotationTree

node,

P

p)

Visits an AnnotatedTree node. This implementation scans the children in left to right order.

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

Visits an AnnotatedTypeTree node. This implementation scans the children in left to right order.

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
**Returns:** the result of scanning

---

#### visitAnnotatedType

public

R

visitAnnotatedType​(

AnnotatedTypeTree

node,

P

p)

Visits an AnnotatedTypeTree node. This implementation scans the children in left to right order.

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

hierarchy. This implementation returns

null

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
**Returns:** the result of scanning

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

hierarchy. This implementation returns

null

.

visitErroneous

```java
public
R
visitErroneous​(
ErroneousTree
node,

P
p)
```

Visits an ErroneousTree node. This implementation returns

null

.

**Specified by:** visitErroneous

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
**Returns:** the result of scanning

---

#### visitErroneous

public

R

visitErroneous​(

ErroneousTree

node,

P

p)

Visits an ErroneousTree node. This implementation returns

null

.

---

