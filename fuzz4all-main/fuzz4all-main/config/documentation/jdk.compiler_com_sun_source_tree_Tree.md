# Interface Tree

**Source:** `jdk.compiler\com\sun\source\tree\Tree.html`

### Class Description

```java
public interface
Tree
```

Common interface for all nodes in an abstract syntax tree.

WARNING:

This interface and its sub-interfaces are
subject to change as the Java™ programming language evolves.
These interfaces are implemented by the JDK Java compiler (javac)
and should not be implemented either directly or indirectly by
other applications.

**All Known Subinterfaces:** AnnotatedTypeTree

,

AnnotationTree

,

ArrayAccessTree

,

ArrayTypeTree

,

AssertTree

,

AssignmentTree

,

BinaryTree

,

BlockTree

,

BreakTree

,

CaseTree

,

CatchTree

,

ClassTree

,

CompilationUnitTree

,

CompoundAssignmentTree

,

ConditionalExpressionTree

,

ContinueTree

,

DirectiveTree

,

DoWhileLoopTree

,

EmptyStatementTree

,

EnhancedForLoopTree

,

ErroneousTree

,

ExportsTree

,

ExpressionStatementTree

,

ExpressionTree

,

ForLoopTree

,

IdentifierTree

,

IfTree

,

ImportTree

,

InstanceOfTree

,

IntersectionTypeTree

,

LabeledStatementTree

,

LambdaExpressionTree

,

LiteralTree

,

MemberReferenceTree

,

MemberSelectTree

,

MethodInvocationTree

,

MethodTree

,

ModifiersTree

,

ModuleTree

,

NewArrayTree

,

NewClassTree

,

OpensTree

,

PackageTree

,

ParameterizedTypeTree

,

ParenthesizedTree

,

PrimitiveTypeTree

,

ProvidesTree

,

RequiresTree

,

ReturnTree

,

StatementTree

,

SwitchTree

,

SynchronizedTree

,

ThrowTree

,

TryTree

,

TypeCastTree

,

TypeParameterTree

,

UnaryTree

,

UnionTypeTree

,

UsesTree

,

VariableTree

,

WhileLoopTree

,

WildcardTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Tree.Kind
getKind()

Returns the kind of this tree.

**Returns:**
- the kind of this tree.

---

#### <R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Parameters:**
- visitor

- the visitor to be called
- data

- a value to be passed to the visitor

**Returns:**
- the result returned from calling the visitor

**Type Parameters:**
- R

- result type of this operation.
- D

- type of additional data.

---

### Additional Sections

#### Interface Tree

**All Known Subinterfaces:** AnnotatedTypeTree

,

AnnotationTree

,

ArrayAccessTree

,

ArrayTypeTree

,

AssertTree

,

AssignmentTree

,

BinaryTree

,

BlockTree

,

BreakTree

,

CaseTree

,

CatchTree

,

ClassTree

,

CompilationUnitTree

,

CompoundAssignmentTree

,

ConditionalExpressionTree

,

ContinueTree

,

DirectiveTree

,

DoWhileLoopTree

,

EmptyStatementTree

,

EnhancedForLoopTree

,

ErroneousTree

,

ExportsTree

,

ExpressionStatementTree

,

ExpressionTree

,

ForLoopTree

,

IdentifierTree

,

IfTree

,

ImportTree

,

InstanceOfTree

,

IntersectionTypeTree

,

LabeledStatementTree

,

LambdaExpressionTree

,

LiteralTree

,

MemberReferenceTree

,

MemberSelectTree

,

MethodInvocationTree

,

MethodTree

,

ModifiersTree

,

ModuleTree

,

NewArrayTree

,

NewClassTree

,

OpensTree

,

PackageTree

,

ParameterizedTypeTree

,

ParenthesizedTree

,

PrimitiveTypeTree

,

ProvidesTree

,

RequiresTree

,

ReturnTree

,

StatementTree

,

SwitchTree

,

SynchronizedTree

,

ThrowTree

,

TryTree

,

TypeCastTree

,

TypeParameterTree

,

UnaryTree

,

UnionTypeTree

,

UsesTree

,

VariableTree

,

WhileLoopTree

,

WildcardTree

```java
public interface
Tree
```

Common interface for all nodes in an abstract syntax tree.

WARNING:

This interface and its sub-interfaces are
subject to change as the Java™ programming language evolves.
These interfaces are implemented by the JDK Java compiler (javac)
and should not be implemented either directly or indirectly by
other applications.

**Since:** 1.6

public interface

Tree

Common interface for all nodes in an abstract syntax tree.

WARNING:

This interface and its sub-interfaces are
subject to change as the Java™ programming language evolves.
These interfaces are implemented by the JDK Java compiler (javac)
and should not be implemented either directly or indirectly by
other applications.

WARNING:

This interface and its sub-interfaces are
subject to change as the Java™ programming language evolves.
These interfaces are implemented by the JDK Java compiler (javac)
and should not be implemented either directly or indirectly by
other applications.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Tree.Kind

Enumerates all kinds of trees.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​D>

R

accept

​(

TreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern.

Tree.Kind

getKind

()

Returns the kind of this tree.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Tree.Kind

Enumerates all kinds of trees.

---

#### Nested Class Summary

Enumerates all kinds of trees.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​D>

R

accept

​(

TreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern.

Tree.Kind

getKind

()

Returns the kind of this tree.

---

#### Method Summary

Accept method used to implement the visitor pattern.

Returns the kind of this tree.

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
Tree.Kind
getKind()
```

Returns the kind of this tree.

**Returns:** the kind of this tree.

- accept

```java
<R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)
```

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- the visitor to be called
**Parameters:** data

- a value to be passed to the visitor
**Returns:** the result returned from calling the visitor

Method Detail

- getKind

```java
Tree.Kind
getKind()
```

Returns the kind of this tree.

**Returns:** the kind of this tree.

- accept

```java
<R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)
```

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- the visitor to be called
**Parameters:** data

- a value to be passed to the visitor
**Returns:** the result returned from calling the visitor

---

#### Method Detail

getKind

```java
Tree.Kind
getKind()
```

Returns the kind of this tree.

**Returns:** the kind of this tree.

---

#### getKind

Tree.Kind

getKind()

Returns the kind of this tree.

accept

```java
<R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)
```

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- the visitor to be called
**Parameters:** data

- a value to be passed to the visitor
**Returns:** the result returned from calling the visitor

---

#### accept

<R,​D> R accept​(

TreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

---

