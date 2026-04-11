# Interface Tree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\Tree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
Tree
```

Common interface for all nodes in an abstract syntax tree.

WARNING:

This interface and its sub-interfaces are
subject to change as the ECMAScript programming language evolves.

**All Known Subinterfaces:** ArrayAccessTree

,

ArrayLiteralTree

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

ClassDeclarationTree

,

ClassExpressionTree

,

CompilationUnitTree

,

CompoundAssignmentTree

,

ConditionalExpressionTree

,

ConditionalLoopTree

,

ContinueTree

,

DebuggerTree

,

DoWhileLoopTree

,

EmptyStatementTree

,

ErroneousTree

,

ExportEntryTree

,

ExpressionStatementTree

,

ExpressionTree

,

ForInLoopTree

,

ForLoopTree

,

ForOfLoopTree

,

FunctionCallTree

,

FunctionDeclarationTree

,

FunctionExpressionTree

,

GotoTree

,

IdentifierTree

,

IfTree

,

ImportEntryTree

,

InstanceOfTree

,

LabeledStatementTree

,

LiteralTree

,

LoopTree

,

MemberSelectTree

,

ModuleTree

,

NewTree

,

ObjectLiteralTree

,

ParenthesizedTree

,

PropertyTree

,

RegExpLiteralTree

,

ReturnTree

,

SpreadTree

,

StatementTree

,

SwitchTree

,

TemplateLiteralTree

,

ThrowTree

,

TryTree

,

UnaryTree

,

VariableTree

,

WhileLoopTree

,

WithTree

,

YieldTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getStartPosition()

Start character offset of this Tree within the source.

**Returns:**
- the position

---

#### long getEndPosition()

End character offset of this Tree within the source.

**Returns:**
- the position

---

#### Tree.Kind
getKind()

Gets the kind of this tree.

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

- tree visitor
- data

- additional data passed to visitor methods

**Returns:**
- the value from visitor's visit methods

**Type Parameters:**
- R

- result type of this operation.
- D

- type of additional data.

---

### Additional Sections

#### Interface Tree

**All Known Subinterfaces:** ArrayAccessTree

,

ArrayLiteralTree

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

ClassDeclarationTree

,

ClassExpressionTree

,

CompilationUnitTree

,

CompoundAssignmentTree

,

ConditionalExpressionTree

,

ConditionalLoopTree

,

ContinueTree

,

DebuggerTree

,

DoWhileLoopTree

,

EmptyStatementTree

,

ErroneousTree

,

ExportEntryTree

,

ExpressionStatementTree

,

ExpressionTree

,

ForInLoopTree

,

ForLoopTree

,

ForOfLoopTree

,

FunctionCallTree

,

FunctionDeclarationTree

,

FunctionExpressionTree

,

GotoTree

,

IdentifierTree

,

IfTree

,

ImportEntryTree

,

InstanceOfTree

,

LabeledStatementTree

,

LiteralTree

,

LoopTree

,

MemberSelectTree

,

ModuleTree

,

NewTree

,

ObjectLiteralTree

,

ParenthesizedTree

,

PropertyTree

,

RegExpLiteralTree

,

ReturnTree

,

SpreadTree

,

StatementTree

,

SwitchTree

,

TemplateLiteralTree

,

ThrowTree

,

TryTree

,

UnaryTree

,

VariableTree

,

WhileLoopTree

,

WithTree

,

YieldTree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
Tree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Common interface for all nodes in an abstract syntax tree.

WARNING:

This interface and its sub-interfaces are
subject to change as the ECMAScript programming language evolves.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

Tree

Common interface for all nodes in an abstract syntax tree.

WARNING:

This interface and its sub-interfaces are
subject to change as the ECMAScript programming language evolves.

WARNING:

This interface and its sub-interfaces are
subject to change as the ECMAScript programming language evolves.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Tree.Kind

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

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

Deprecated, for removal: This API element is subject to removal in a future version.

Accept method used to implement the visitor pattern.

long

getEndPosition

()

Deprecated, for removal: This API element is subject to removal in a future version.

End character offset of this Tree within the source.

Tree.Kind

getKind

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this tree.

long

getStartPosition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Start character offset of this Tree within the source.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Tree.Kind

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

---

#### Nested Class Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

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

Deprecated, for removal: This API element is subject to removal in a future version.

Accept method used to implement the visitor pattern.

long

getEndPosition

()

Deprecated, for removal: This API element is subject to removal in a future version.

End character offset of this Tree within the source.

Tree.Kind

getKind

()

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this tree.

long

getStartPosition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Start character offset of this Tree within the source.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Accept method used to implement the visitor pattern.

End character offset of this Tree within the source.

Gets the kind of this tree.

Start character offset of this Tree within the source.

============ METHOD DETAIL ==========

- Method Detail

- getStartPosition

```java
long getStartPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Start character offset of this Tree within the source.

**Returns:** the position

- getEndPosition

```java
long getEndPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

End character offset of this Tree within the source.

**Returns:** the position

- getKind

```java
Tree.Kind
getKind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this tree.

**Returns:** the kind of this tree.

- accept

```java
<R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- tree visitor
**Parameters:** data

- additional data passed to visitor methods
**Returns:** the value from visitor's visit methods

Method Detail

- getStartPosition

```java
long getStartPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Start character offset of this Tree within the source.

**Returns:** the position

- getEndPosition

```java
long getEndPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

End character offset of this Tree within the source.

**Returns:** the position

- getKind

```java
Tree.Kind
getKind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this tree.

**Returns:** the kind of this tree.

- accept

```java
<R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- tree visitor
**Parameters:** data

- additional data passed to visitor methods
**Returns:** the value from visitor's visit methods

---

#### Method Detail

getStartPosition

```java
long getStartPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Start character offset of this Tree within the source.

**Returns:** the position

---

#### getStartPosition

long getStartPosition()

Start character offset of this Tree within the source.

getEndPosition

```java
long getEndPosition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

End character offset of this Tree within the source.

**Returns:** the position

---

#### getEndPosition

long getEndPosition()

End character offset of this Tree within the source.

getKind

```java
Tree.Kind
getKind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Gets the kind of this tree.

**Returns:** the kind of this tree.

---

#### getKind

Tree.Kind

getKind()

Gets the kind of this tree.

accept

```java
<R,​D> R accept​(
TreeVisitor
<R,​D> visitor,
D data)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- tree visitor
**Parameters:** data

- additional data passed to visitor methods
**Returns:** the value from visitor's visit methods

---

#### accept

<R,​D> R accept​(

TreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

---

