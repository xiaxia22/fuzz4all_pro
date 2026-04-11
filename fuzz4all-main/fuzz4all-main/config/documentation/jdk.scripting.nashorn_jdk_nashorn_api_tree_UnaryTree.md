# Interface UnaryTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\UnaryTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
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

Returns the expression operated by the unary operator.

**Returns:**
- The expression operated by the unary operator.

---

### Additional Sections

#### Interface UnaryTree

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
UnaryTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

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

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression operated by the unary operator.

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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression operated by the unary operator.

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

Returns the expression operated by the unary operator.

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

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression operated by the unary operator.

**Returns:** The expression operated by the unary operator.

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression operated by the unary operator.

**Returns:** The expression operated by the unary operator.

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression operated by the unary operator.

**Returns:** The expression operated by the unary operator.

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression operated by the unary operator.

---

