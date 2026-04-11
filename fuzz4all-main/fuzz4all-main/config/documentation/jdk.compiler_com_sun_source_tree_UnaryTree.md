# Interface UnaryTree

**Source:** `jdk.compiler\com\sun\source\tree\UnaryTree.html`

### Class Description

```java
public interface
UnaryTree

extends
ExpressionTree
```

A tree node for postfix and unary expressions.
Use

getKind

to determine the kind of operator.

For example:

```java
operator

expression

expression

operator
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
getExpression()

Returns the expression that is the operand of the unary operator.

**Returns:**
- the expression

---

### Additional Sections

#### Interface UnaryTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
UnaryTree

extends
ExpressionTree
```

A tree node for postfix and unary expressions.
Use

getKind

to determine the kind of operator.

For example:

```java
operator

expression

expression

operator
```

**Since:** 1.6
**See The Java™ Language Specification :** sections 15.14 and 15.15

public interface

UnaryTree

extends

ExpressionTree

A tree node for postfix and unary expressions.
Use

getKind

to determine the kind of operator.

For example:

```java
operator

expression

expression

operator
```

operator

expression

expression

operator

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

getExpression

()

Returns the expression that is the operand of the unary operator.

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

getExpression

()

Returns the expression that is the operand of the unary operator.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression that is the operand of the unary operator.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression that is the operand of the unary operator.

**Returns:** the expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression that is the operand of the unary operator.

**Returns:** the expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression that is the operand of the unary operator.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression that is the operand of the unary operator.

---

