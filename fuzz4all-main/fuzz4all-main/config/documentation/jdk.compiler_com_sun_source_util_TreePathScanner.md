# Class TreePathScanner<R,​P>

**Source:** `jdk.compiler\com\sun\source\util\TreePathScanner.html`

### Class Description

```java
public class
TreePathScanner<R,​P>

extends
TreeScanner
<R,​P>
```

A TreeVisitor that visits all the child tree nodes, and provides
support for maintaining a path for the parent nodes.
To visit nodes of a particular type, just override the
corresponding visitorXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

**All Implemented Interfaces:** TreeVisitor

<R,​P>

---

### Field Details

*No entries found.*

### Constructor Details

#### public TreePathScanner()

*No description found.*

---

### Method Details

#### public
R
scan​(
TreePath
path,

P
p)

Scans a tree from a position identified by a TreePath.

**Parameters:**
- path

- the path identifying the node to be scanned
- p

- a parameter value passed to visit methods

**Returns:**
- the result value from the visit method

---

#### public
R
scan​(
Tree
tree,

P
p)

Scans a single node.
The current path is updated for the duration of the scan.

**Overrides:**
- scan

in class

TreeScanner

<

R

,​

P

>

**Parameters:**
- tree

- the node to be scanned
- p

- a parameter value passed to the visit method

**Returns:**
- the result value from the visit method

**API Note:**
- This method should normally only be called by the
scanner's

visit

methods, as part of an ongoing scan
initiated by

scan(TreePath, P)

.
The one exception is that it may also be called to initiate
a full scan of a

CompilationUnitTree

.

---

#### public
TreePath
getCurrentPath()

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:**
- the current path

---

### Additional Sections

#### Class TreePathScanner<R,​P>

java.lang.Object

- com.sun.source.util.TreeScanner

<R,​P>
- - com.sun.source.util.TreePathScanner<R,​P>

com.sun.source.util.TreeScanner

<R,​P>

- com.sun.source.util.TreePathScanner<R,​P>

com.sun.source.util.TreePathScanner<R,​P>

**All Implemented Interfaces:** TreeVisitor

<R,​P>

```java
public class
TreePathScanner<R,​P>

extends
TreeScanner
<R,​P>
```

A TreeVisitor that visits all the child tree nodes, and provides
support for maintaining a path for the parent nodes.
To visit nodes of a particular type, just override the
corresponding visitorXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

**API Note:** In order to initialize the "current path", the scan must be
started by calling one of the

scan

methods.
**Since:** 1.6

public class

TreePathScanner<R,​P>

extends

TreeScanner

<R,​P>

A TreeVisitor that visits all the child tree nodes, and provides
support for maintaining a path for the parent nodes.
To visit nodes of a particular type, just override the
corresponding visitorXYZ method.
Inside your method, call super.visitXYZ to visit descendant
nodes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreePathScanner

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TreePath

getCurrentPath

()

Returns the current path for the node, as built up by the currently
active set of scan calls.

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

TreePath

path,

P

p)

Scans a tree from a position identified by a TreePath.

- Methods declared in class com.sun.source.util.

TreeScanner

reduce

,

scan

,

visitAnnotatedType

,

visitAnnotation

,

visitArrayAccess

,

visitArrayType

,

visitAssert

,

visitAssignment

,

visitBinary

,

visitBlock

,

visitBreak

,

visitCase

,

visitCatch

,

visitClass

,

visitCompilationUnit

,

visitCompoundAssignment

,

visitConditionalExpression

,

visitContinue

,

visitDoWhileLoop

,

visitEmptyStatement

,

visitEnhancedForLoop

,

visitErroneous

,

visitExpressionStatement

,

visitForLoop

,

visitIdentifier

,

visitIf

,

visitImport

,

visitInstanceOf

,

visitIntersectionType

,

visitLabeledStatement

,

visitLambdaExpression

,

visitLiteral

,

visitMemberReference

,

visitMemberSelect

,

visitMethod

,

visitMethodInvocation

,

visitModifiers

,

visitNewArray

,

visitNewClass

,

visitOther

,

visitPackage

,

visitParameterizedType

,

visitParenthesized

,

visitPrimitiveType

,

visitReturn

,

visitSwitch

,

visitSynchronized

,

visitThrow

,

visitTry

,

visitTypeCast

,

visitTypeParameter

,

visitUnary

,

visitUnionType

,

visitVariable

,

visitWhileLoop

,

visitWildcard

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

TreePathScanner

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

TreePath

getCurrentPath

()

Returns the current path for the node, as built up by the currently
active set of scan calls.

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

TreePath

path,

P

p)

Scans a tree from a position identified by a TreePath.

- Methods declared in class com.sun.source.util.

TreeScanner

reduce

,

scan

,

visitAnnotatedType

,

visitAnnotation

,

visitArrayAccess

,

visitArrayType

,

visitAssert

,

visitAssignment

,

visitBinary

,

visitBlock

,

visitBreak

,

visitCase

,

visitCatch

,

visitClass

,

visitCompilationUnit

,

visitCompoundAssignment

,

visitConditionalExpression

,

visitContinue

,

visitDoWhileLoop

,

visitEmptyStatement

,

visitEnhancedForLoop

,

visitErroneous

,

visitExpressionStatement

,

visitForLoop

,

visitIdentifier

,

visitIf

,

visitImport

,

visitInstanceOf

,

visitIntersectionType

,

visitLabeledStatement

,

visitLambdaExpression

,

visitLiteral

,

visitMemberReference

,

visitMemberSelect

,

visitMethod

,

visitMethodInvocation

,

visitModifiers

,

visitNewArray

,

visitNewClass

,

visitOther

,

visitPackage

,

visitParameterizedType

,

visitParenthesized

,

visitPrimitiveType

,

visitReturn

,

visitSwitch

,

visitSynchronized

,

visitThrow

,

visitTry

,

visitTypeCast

,

visitTypeParameter

,

visitUnary

,

visitUnionType

,

visitVariable

,

visitWhileLoop

,

visitWildcard

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

Returns the current path for the node, as built up by the currently
active set of scan calls.

Scans a single node.

Scans a tree from a position identified by a TreePath.

Methods declared in class com.sun.source.util.

TreeScanner

reduce

,

scan

,

visitAnnotatedType

,

visitAnnotation

,

visitArrayAccess

,

visitArrayType

,

visitAssert

,

visitAssignment

,

visitBinary

,

visitBlock

,

visitBreak

,

visitCase

,

visitCatch

,

visitClass

,

visitCompilationUnit

,

visitCompoundAssignment

,

visitConditionalExpression

,

visitContinue

,

visitDoWhileLoop

,

visitEmptyStatement

,

visitEnhancedForLoop

,

visitErroneous

,

visitExpressionStatement

,

visitForLoop

,

visitIdentifier

,

visitIf

,

visitImport

,

visitInstanceOf

,

visitIntersectionType

,

visitLabeledStatement

,

visitLambdaExpression

,

visitLiteral

,

visitMemberReference

,

visitMemberSelect

,

visitMethod

,

visitMethodInvocation

,

visitModifiers

,

visitNewArray

,

visitNewClass

,

visitOther

,

visitPackage

,

visitParameterizedType

,

visitParenthesized

,

visitPrimitiveType

,

visitReturn

,

visitSwitch

,

visitSynchronized

,

visitThrow

,

visitTry

,

visitTypeCast

,

visitTypeParameter

,

visitUnary

,

visitUnionType

,

visitVariable

,

visitWhileLoop

,

visitWildcard

---

#### Methods declared in class com.sun.source.util. TreeScanner

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

- TreePathScanner

```java
public TreePathScanner()
```

============ METHOD DETAIL ==========

- Method Detail

- scan

```java
public
R
scan​(
TreePath
path,

P
p)
```

Scans a tree from a position identified by a TreePath.

**Parameters:** path

- the path identifying the node to be scanned
**Parameters:** p

- a parameter value passed to visit methods
**Returns:** the result value from the visit method

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
The current path is updated for the duration of the scan.

**Overrides:** scan

in class

TreeScanner

<

R

,​

P

>
**API Note:** This method should normally only be called by the
scanner's

visit

methods, as part of an ongoing scan
initiated by

scan(TreePath, P)

.
The one exception is that it may also be called to initiate
a full scan of a

CompilationUnitTree

.
**Parameters:** tree

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

- getCurrentPath

```java
public
TreePath
getCurrentPath()
```

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:** the current path

Constructor Detail

- TreePathScanner

```java
public TreePathScanner()
```

---

#### Constructor Detail

TreePathScanner

```java
public TreePathScanner()
```

---

#### TreePathScanner

public TreePathScanner()

Method Detail

- scan

```java
public
R
scan​(
TreePath
path,

P
p)
```

Scans a tree from a position identified by a TreePath.

**Parameters:** path

- the path identifying the node to be scanned
**Parameters:** p

- a parameter value passed to visit methods
**Returns:** the result value from the visit method

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
The current path is updated for the duration of the scan.

**Overrides:** scan

in class

TreeScanner

<

R

,​

P

>
**API Note:** This method should normally only be called by the
scanner's

visit

methods, as part of an ongoing scan
initiated by

scan(TreePath, P)

.
The one exception is that it may also be called to initiate
a full scan of a

CompilationUnitTree

.
**Parameters:** tree

- the node to be scanned
**Parameters:** p

- a parameter value passed to the visit method
**Returns:** the result value from the visit method

- getCurrentPath

```java
public
TreePath
getCurrentPath()
```

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:** the current path

---

#### Method Detail

scan

```java
public
R
scan​(
TreePath
path,

P
p)
```

Scans a tree from a position identified by a TreePath.

**Parameters:** path

- the path identifying the node to be scanned
**Parameters:** p

- a parameter value passed to visit methods
**Returns:** the result value from the visit method

---

#### scan

public

R

scan​(

TreePath

path,

P

p)

Scans a tree from a position identified by a TreePath.

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
The current path is updated for the duration of the scan.

**Overrides:** scan

in class

TreeScanner

<

R

,​

P

>
**API Note:** This method should normally only be called by the
scanner's

visit

methods, as part of an ongoing scan
initiated by

scan(TreePath, P)

.
The one exception is that it may also be called to initiate
a full scan of a

CompilationUnitTree

.
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
The current path is updated for the duration of the scan.

getCurrentPath

```java
public
TreePath
getCurrentPath()
```

Returns the current path for the node, as built up by the currently
active set of scan calls.

**Returns:** the current path

---

#### getCurrentPath

public

TreePath

getCurrentPath()

Returns the current path for the node, as built up by the currently
active set of scan calls.

---

