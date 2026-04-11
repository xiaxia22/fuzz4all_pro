# Interface ConditionalExpressionTree

**Source:** `jdk.compiler\com\sun\source\tree\ConditionalExpressionTree.html`

### Class Description

```java
public interface
ConditionalExpressionTree

extends
ExpressionTree
```

A tree node for the conditional operator ? :.

For example:

```java
condition
?
trueExpression
:
falseExpression
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
getCondition()

Returns the condition.

**Returns:**
- the condition

---

#### ExpressionTree
getTrueExpression()

Returns the expression to be evaluated if the condition is true.

**Returns:**
- the expression to be evaluated if the condition is true

---

#### ExpressionTree
getFalseExpression()

Returns the expression to be evaluated if the condition is false.

**Returns:**
- the expression to be evaluated if the condition is false

---

### Additional Sections

#### Interface ConditionalExpressionTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
ConditionalExpressionTree

extends
ExpressionTree
```

A tree node for the conditional operator ? :.

For example:

```java
condition
?
trueExpression
:
falseExpression
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.25

public interface

ConditionalExpressionTree

extends

ExpressionTree

A tree node for the conditional operator ? :.

For example:

```java
condition
?
trueExpression
:
falseExpression
```

condition

?

trueExpression

:

falseExpression

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

getCondition

()

Returns the condition.

ExpressionTree

getFalseExpression

()

Returns the expression to be evaluated if the condition is false.

ExpressionTree

getTrueExpression

()

Returns the expression to be evaluated if the condition is true.

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

getCondition

()

Returns the condition.

ExpressionTree

getFalseExpression

()

Returns the expression to be evaluated if the condition is false.

ExpressionTree

getTrueExpression

()

Returns the expression to be evaluated if the condition is true.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the condition.

Returns the expression to be evaluated if the condition is false.

Returns the expression to be evaluated if the condition is true.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition.

**Returns:** the condition

- getTrueExpression

```java
ExpressionTree
getTrueExpression()
```

Returns the expression to be evaluated if the condition is true.

**Returns:** the expression to be evaluated if the condition is true

- getFalseExpression

```java
ExpressionTree
getFalseExpression()
```

Returns the expression to be evaluated if the condition is false.

**Returns:** the expression to be evaluated if the condition is false

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition.

**Returns:** the condition

- getTrueExpression

```java
ExpressionTree
getTrueExpression()
```

Returns the expression to be evaluated if the condition is true.

**Returns:** the expression to be evaluated if the condition is true

- getFalseExpression

```java
ExpressionTree
getFalseExpression()
```

Returns the expression to be evaluated if the condition is false.

**Returns:** the expression to be evaluated if the condition is false

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition.

**Returns:** the condition

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition.

getTrueExpression

```java
ExpressionTree
getTrueExpression()
```

Returns the expression to be evaluated if the condition is true.

**Returns:** the expression to be evaluated if the condition is true

---

#### getTrueExpression

ExpressionTree

getTrueExpression()

Returns the expression to be evaluated if the condition is true.

getFalseExpression

```java
ExpressionTree
getFalseExpression()
```

Returns the expression to be evaluated if the condition is false.

**Returns:** the expression to be evaluated if the condition is false

---

#### getFalseExpression

ExpressionTree

getFalseExpression()

Returns the expression to be evaluated if the condition is false.

---

