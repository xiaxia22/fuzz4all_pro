# Interface DoWhileLoopTree

**Source:** `jdk.compiler\com\sun\source\tree\DoWhileLoopTree.html`

### Class Description

```java
public interface
DoWhileLoopTree

extends
StatementTree
```

A tree node for a

do

statement.

For example:

```java
do

statement

while (
expression
);
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
getCondition()

Returns the condition of the loop.

**Returns:**
- the condition

---

#### StatementTree
getStatement()

Returns the body of the loop.

**Returns:**
- the body of the loop

---

### Additional Sections

#### Interface DoWhileLoopTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
DoWhileLoopTree

extends
StatementTree
```

A tree node for a

do

statement.

For example:

```java
do

statement

while (
expression
);
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.13

public interface

DoWhileLoopTree

extends

StatementTree

A tree node for a

do

statement.

For example:

```java
do

statement

while (
expression
);
```

do

statement

while (

expression

);

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

Returns the condition of the loop.

StatementTree

getStatement

()

Returns the body of the loop.

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

Returns the condition of the loop.

StatementTree

getStatement

()

Returns the body of the loop.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the condition of the loop.

Returns the body of the loop.

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

Returns the condition of the loop.

**Returns:** the condition

- getStatement

```java
StatementTree
getStatement()
```

Returns the body of the loop.

**Returns:** the body of the loop

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the loop.

**Returns:** the condition

- getStatement

```java
StatementTree
getStatement()
```

Returns the body of the loop.

**Returns:** the body of the loop

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the loop.

**Returns:** the condition

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition of the loop.

getStatement

```java
StatementTree
getStatement()
```

Returns the body of the loop.

**Returns:** the body of the loop

---

#### getStatement

StatementTree

getStatement()

Returns the body of the loop.

---

