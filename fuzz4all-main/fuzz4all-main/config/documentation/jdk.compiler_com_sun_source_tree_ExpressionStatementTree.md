# Interface ExpressionStatementTree

**Source:** `jdk.compiler\com\sun\source\tree\ExpressionStatementTree.html`

### Class Description

```java
public interface
ExpressionStatementTree

extends
StatementTree
```

A tree node for an expression statement.

For example:

```java
expression
;
```

**All Superinterfaces:** StatementTree

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

Returns the expression constituting this statement.

**Returns:**
- the expression

---

### Additional Sections

#### Interface ExpressionStatementTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
ExpressionStatementTree

extends
StatementTree
```

A tree node for an expression statement.

For example:

```java
expression
;
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.8

public interface

ExpressionStatementTree

extends

StatementTree

A tree node for an expression statement.

For example:

```java
expression
;
```

expression

;

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

Returns the expression constituting this statement.

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

Returns the expression constituting this statement.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression constituting this statement.

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

Returns the expression constituting this statement.

**Returns:** the expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression constituting this statement.

**Returns:** the expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression constituting this statement.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression constituting this statement.

---

