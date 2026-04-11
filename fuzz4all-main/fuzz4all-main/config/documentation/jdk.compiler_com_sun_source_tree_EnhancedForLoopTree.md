# Interface EnhancedForLoopTree

**Source:** `jdk.compiler\com\sun\source\tree\EnhancedForLoopTree.html`

### Class Description

```java
public interface
EnhancedForLoopTree

extends
StatementTree
```

A tree node for an "enhanced"

for

loop statement.

For example:

```java
for (
variable
:
expression
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

#### VariableTree
getVariable()

Returns the control variable for the loop.

**Returns:**
- the control variable

---

#### ExpressionTree
getExpression()

Returns the expression yielding the values for the control variable.

**Returns:**
- the expression

---

#### StatementTree
getStatement()

Returns the body of the loop.

**Returns:**
- the body of the loop

---

### Additional Sections

#### Interface EnhancedForLoopTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
EnhancedForLoopTree

extends
StatementTree
```

A tree node for an "enhanced"

for

loop statement.

For example:

```java
for (
variable
:
expression
)

statement
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.14.2

public interface

EnhancedForLoopTree

extends

StatementTree

A tree node for an "enhanced"

for

loop statement.

For example:

```java
for (
variable
:
expression
)

statement
```

for (

variable

:

expression

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

getExpression

()

Returns the expression yielding the values for the control variable.

StatementTree

getStatement

()

Returns the body of the loop.

VariableTree

getVariable

()

Returns the control variable for the loop.

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

Returns the expression yielding the values for the control variable.

StatementTree

getStatement

()

Returns the body of the loop.

VariableTree

getVariable

()

Returns the control variable for the loop.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression yielding the values for the control variable.

Returns the body of the loop.

Returns the control variable for the loop.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getVariable

```java
VariableTree
getVariable()
```

Returns the control variable for the loop.

**Returns:** the control variable

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression yielding the values for the control variable.

**Returns:** the expression

- getStatement

```java
StatementTree
getStatement()
```

Returns the body of the loop.

**Returns:** the body of the loop

Method Detail

- getVariable

```java
VariableTree
getVariable()
```

Returns the control variable for the loop.

**Returns:** the control variable

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression yielding the values for the control variable.

**Returns:** the expression

- getStatement

```java
StatementTree
getStatement()
```

Returns the body of the loop.

**Returns:** the body of the loop

---

#### Method Detail

getVariable

```java
VariableTree
getVariable()
```

Returns the control variable for the loop.

**Returns:** the control variable

---

#### getVariable

VariableTree

getVariable()

Returns the control variable for the loop.

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression yielding the values for the control variable.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression yielding the values for the control variable.

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

