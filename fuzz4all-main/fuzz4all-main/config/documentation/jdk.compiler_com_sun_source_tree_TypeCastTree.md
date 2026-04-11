# Interface TypeCastTree

**Source:** `jdk.compiler\com\sun\source\tree\TypeCastTree.html`

### Class Description

```java
public interface
TypeCastTree

extends
ExpressionTree
```

A tree node for a type cast expression.

For example:

```java
(
type
)
expression
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

#### Tree
getType()

Returns the target type of the cast.

**Returns:**
- the cast

---

#### ExpressionTree
getExpression()

Returns the expression being cast.

**Returns:**
- the expression

---

### Additional Sections

#### Interface TypeCastTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
TypeCastTree

extends
ExpressionTree
```

A tree node for a type cast expression.

For example:

```java
(
type
)
expression
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.16

public interface

TypeCastTree

extends

ExpressionTree

A tree node for a type cast expression.

For example:

```java
(
type
)
expression
```

(

type

)

expression

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

Returns the expression being cast.

Tree

getType

()

Returns the target type of the cast.

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

Returns the expression being cast.

Tree

getType

()

Returns the target type of the cast.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression being cast.

Returns the target type of the cast.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
Tree
getType()
```

Returns the target type of the cast.

**Returns:** the cast

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression being cast.

**Returns:** the expression

Method Detail

- getType

```java
Tree
getType()
```

Returns the target type of the cast.

**Returns:** the cast

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression being cast.

**Returns:** the expression

---

#### Method Detail

getType

```java
Tree
getType()
```

Returns the target type of the cast.

**Returns:** the cast

---

#### getType

Tree

getType()

Returns the target type of the cast.

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression being cast.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression being cast.

---

