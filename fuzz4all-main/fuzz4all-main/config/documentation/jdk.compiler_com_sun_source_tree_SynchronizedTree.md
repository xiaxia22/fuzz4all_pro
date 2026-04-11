# Interface SynchronizedTree

**Source:** `jdk.compiler\com\sun\source\tree\SynchronizedTree.html`

### Class Description

```java
public interface
SynchronizedTree

extends
StatementTree
```

A tree node for a

synchronized

statement.

For example:

```java
synchronized (
expression
)

block
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

Returns the expression on which to synchronize.

**Returns:**
- the expression

---

#### BlockTree
getBlock()

Returns the block of the

synchronized

statement.

**Returns:**
- the block

---

### Additional Sections

#### Interface SynchronizedTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
SynchronizedTree

extends
StatementTree
```

A tree node for a

synchronized

statement.

For example:

```java
synchronized (
expression
)

block
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.19

public interface

SynchronizedTree

extends

StatementTree

A tree node for a

synchronized

statement.

For example:

```java
synchronized (
expression
)

block
```

synchronized (

expression

)

block

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

BlockTree

getBlock

()

Returns the block of the

synchronized

statement.

ExpressionTree

getExpression

()

Returns the expression on which to synchronize.

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

BlockTree

getBlock

()

Returns the block of the

synchronized

statement.

ExpressionTree

getExpression

()

Returns the expression on which to synchronize.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the block of the

synchronized

statement.

Returns the expression on which to synchronize.

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

Returns the expression on which to synchronize.

**Returns:** the expression

- getBlock

```java
BlockTree
getBlock()
```

Returns the block of the

synchronized

statement.

**Returns:** the block

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression on which to synchronize.

**Returns:** the expression

- getBlock

```java
BlockTree
getBlock()
```

Returns the block of the

synchronized

statement.

**Returns:** the block

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression on which to synchronize.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression on which to synchronize.

getBlock

```java
BlockTree
getBlock()
```

Returns the block of the

synchronized

statement.

**Returns:** the block

---

#### getBlock

BlockTree

getBlock()

Returns the block of the

synchronized

statement.

---

