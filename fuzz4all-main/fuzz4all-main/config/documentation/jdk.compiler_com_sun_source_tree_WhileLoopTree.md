# Interface WhileLoopTree

**Source:** `jdk.compiler\com\sun\source\tree\WhileLoopTree.html`

### Class Description

```java
public interface
WhileLoopTree

extends
StatementTree
```

A tree node for a

while

loop statement.

For example:

```java
while (
condition
)

statement
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

#### Interface WhileLoopTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
WhileLoopTree

extends
StatementTree
```

A tree node for a

while

loop statement.

For example:

```java
while (
condition
)

statement
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.12

public interface

WhileLoopTree

extends

StatementTree

A tree node for a

while

loop statement.

For example:

```java
while (
condition
)

statement
```

while (

condition

)

statement

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

