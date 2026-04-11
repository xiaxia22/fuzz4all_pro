# Interface BinaryTree

**Source:** `jdk.compiler\com\sun\source\tree\BinaryTree.html`

### Class Description

```java
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

Returns the left (first) operand of the expression.

**Returns:**
- the left operand

---

#### ExpressionTree
getRightOperand()

Returns the right (second) operand of the expression.

**Returns:**
- the right operand

---

### Additional Sections

#### Interface BinaryTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
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

**Since:** 1.6
**See The Java™ Language Specification :** sections 15.17 to 15.24

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

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ExpressionTree

getLeftOperand

()

Returns the left (first) operand of the expression.

ExpressionTree

getRightOperand

()

Returns the right (second) operand of the expression.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ExpressionTree

getLeftOperand

()

Returns the left (first) operand of the expression.

ExpressionTree

getRightOperand

()

Returns the right (second) operand of the expression.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the left (first) operand of the expression.

Returns the right (second) operand of the expression.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getLeftOperand

```java
ExpressionTree
getLeftOperand()
```

Returns the left (first) operand of the expression.

**Returns:** the left operand

- getRightOperand

```java
ExpressionTree
getRightOperand()
```

Returns the right (second) operand of the expression.

**Returns:** the right operand

Method Detail

- getLeftOperand

```java
ExpressionTree
getLeftOperand()
```

Returns the left (first) operand of the expression.

**Returns:** the left operand

- getRightOperand

```java
ExpressionTree
getRightOperand()
```

Returns the right (second) operand of the expression.

**Returns:** the right operand

---

#### Method Detail

getLeftOperand

```java
ExpressionTree
getLeftOperand()
```

Returns the left (first) operand of the expression.

**Returns:** the left operand

---

#### getLeftOperand

ExpressionTree

getLeftOperand()

Returns the left (first) operand of the expression.

getRightOperand

```java
ExpressionTree
getRightOperand()
```

Returns the right (second) operand of the expression.

**Returns:** the right operand

---

#### getRightOperand

ExpressionTree

getRightOperand()

Returns the right (second) operand of the expression.

---

