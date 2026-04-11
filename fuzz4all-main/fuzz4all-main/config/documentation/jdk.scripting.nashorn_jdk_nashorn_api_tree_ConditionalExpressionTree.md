# Interface ConditionalExpressionTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ConditionalExpressionTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
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

Returns the condition expression of this ternary expression.

**Returns:**
- the condition expression

---

#### ExpressionTree
getTrueExpression()

Returns the true part of this ternary expression.

**Returns:**
- the 'true' part expression

---

#### ExpressionTree
getFalseExpression()

Returns the false part of this ternary expression.

**Returns:**
- the 'false' part expression

---

### Additional Sections

#### Interface ConditionalExpressionTree

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
ConditionalExpressionTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for the conditional operator ? :.

For example:

```java
condition
?
trueExpression
:
falseExpression
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
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

getCondition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this ternary expression.

ExpressionTree

getFalseExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the false part of this ternary expression.

ExpressionTree

getTrueExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the true part of this ternary expression.

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

getCondition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this ternary expression.

ExpressionTree

getFalseExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the false part of this ternary expression.

ExpressionTree

getTrueExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the true part of this ternary expression.

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

Returns the condition expression of this ternary expression.

Returns the false part of this ternary expression.

Returns the true part of this ternary expression.

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

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this ternary expression.

**Returns:** the condition expression

- getTrueExpression

```java
ExpressionTree
getTrueExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the true part of this ternary expression.

**Returns:** the 'true' part expression

- getFalseExpression

```java
ExpressionTree
getFalseExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the false part of this ternary expression.

**Returns:** the 'false' part expression

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this ternary expression.

**Returns:** the condition expression

- getTrueExpression

```java
ExpressionTree
getTrueExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the true part of this ternary expression.

**Returns:** the 'true' part expression

- getFalseExpression

```java
ExpressionTree
getFalseExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the false part of this ternary expression.

**Returns:** the 'false' part expression

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this ternary expression.

**Returns:** the condition expression

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition expression of this ternary expression.

getTrueExpression

```java
ExpressionTree
getTrueExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the true part of this ternary expression.

**Returns:** the 'true' part expression

---

#### getTrueExpression

ExpressionTree

getTrueExpression()

Returns the true part of this ternary expression.

getFalseExpression

```java
ExpressionTree
getFalseExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the false part of this ternary expression.

**Returns:** the 'false' part expression

---

#### getFalseExpression

ExpressionTree

getFalseExpression()

Returns the false part of this ternary expression.

---

