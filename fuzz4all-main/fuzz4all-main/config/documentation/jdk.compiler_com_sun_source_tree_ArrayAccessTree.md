# Interface ArrayAccessTree

**Source:** `jdk.compiler\com\sun\source\tree\ArrayAccessTree.html`

### Class Description

```java
public interface
ArrayAccessTree

extends
ExpressionTree
```

A tree node for an array access expression.

For example:

```java
expression
[
index
]
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

Returns the expression for the array being accessed.

**Returns:**
- the array

---

#### ExpressionTree
getIndex()

Returns the expression for the index.

**Returns:**
- the index

---

### Additional Sections

#### Interface ArrayAccessTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
ArrayAccessTree

extends
ExpressionTree
```

A tree node for an array access expression.

For example:

```java
expression
[
index
]
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.13

public interface

ArrayAccessTree

extends

ExpressionTree

A tree node for an array access expression.

For example:

```java
expression
[
index
]
```

expression

[

index

]

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

Returns the expression for the array being accessed.

ExpressionTree

getIndex

()

Returns the expression for the index.

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

Returns the expression for the array being accessed.

ExpressionTree

getIndex

()

Returns the expression for the index.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression for the array being accessed.

Returns the expression for the index.

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

Returns the expression for the array being accessed.

**Returns:** the array

- getIndex

```java
ExpressionTree
getIndex()
```

Returns the expression for the index.

**Returns:** the index

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the array being accessed.

**Returns:** the array

- getIndex

```java
ExpressionTree
getIndex()
```

Returns the expression for the index.

**Returns:** the index

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the array being accessed.

**Returns:** the array

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression for the array being accessed.

getIndex

```java
ExpressionTree
getIndex()
```

Returns the expression for the index.

**Returns:** the index

---

#### getIndex

ExpressionTree

getIndex()

Returns the expression for the index.

---

