# Interface BinaryTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\BinaryTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
BinaryTree

extends
ExpressionTree
```

A tree node for a binary expression.
Use

getKind

to determine the kind of operator.

For example:

```java
leftOperand

operator

rightOperand
```

**All Superinterfaces:** ExpressionTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ExpressionTree
getLeftOperand()

Returns left hand side (LHS) of this binary expression.

**Returns:**
- left hand side (LHS) of this binary expression

---

#### ExpressionTree
getRightOperand()

Returns right hand side (RHS) of this binary expression.

**Returns:**
- right hand side (RHS) of this binary expression

---

### Additional Sections

#### Interface BinaryTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
BinaryTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a binary expression.
Use

getKind

to determine the kind of operator.

For example:

```java
leftOperand

operator

rightOperand
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

BinaryTree

extends

ExpressionTree

A tree node for a binary expression.
Use

getKind

to determine the kind of operator.

For example:

```java
leftOperand

operator

rightOperand
```

leftOperand

operator

rightOperand

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ExpressionTree

getLeftOperand

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns left hand side (LHS) of this binary expression.

ExpressionTree

getRightOperand

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns right hand side (RHS) of this binary expression.

- Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

Nested Class Summary

- Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface jdk.nashorn.api.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ExpressionTree

getLeftOperand

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns left hand side (LHS) of this binary expression.

ExpressionTree

getRightOperand

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns right hand side (RHS) of this binary expression.

- Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns left hand side (LHS) of this binary expression.

Returns right hand side (RHS) of this binary expression.

Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

---

#### Methods declared in interface jdk.nashorn.api.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getLeftOperand

```java
ExpressionTree
getLeftOperand()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns left hand side (LHS) of this binary expression.

**Returns:** left hand side (LHS) of this binary expression

- getRightOperand

```java
ExpressionTree
getRightOperand()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns right hand side (RHS) of this binary expression.

**Returns:** right hand side (RHS) of this binary expression

Method Detail

- getLeftOperand

```java
ExpressionTree
getLeftOperand()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns left hand side (LHS) of this binary expression.

**Returns:** left hand side (LHS) of this binary expression

- getRightOperand

```java
ExpressionTree
getRightOperand()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns right hand side (RHS) of this binary expression.

**Returns:** right hand side (RHS) of this binary expression

---

#### Method Detail

getLeftOperand

```java
ExpressionTree
getLeftOperand()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns left hand side (LHS) of this binary expression.

**Returns:** left hand side (LHS) of this binary expression

---

#### getLeftOperand

ExpressionTree

getLeftOperand()

Returns left hand side (LHS) of this binary expression.

getRightOperand

```java
ExpressionTree
getRightOperand()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns right hand side (RHS) of this binary expression.

**Returns:** right hand side (RHS) of this binary expression

---

#### getRightOperand

ExpressionTree

getRightOperand()

Returns right hand side (RHS) of this binary expression.

---

