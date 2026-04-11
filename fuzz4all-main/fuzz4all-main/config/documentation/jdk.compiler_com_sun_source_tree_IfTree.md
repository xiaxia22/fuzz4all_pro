# Interface IfTree

**Source:** `jdk.compiler\com\sun\source\tree\IfTree.html`

### Class Description

```java
public interface
IfTree

extends
StatementTree
```

A tree node for an

if

statement.

For example:

```java
if (
condition
)

thenStatement

if (
condition
)

thenStatement

else

elseStatement
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

Returns the condition of the if-statement.

**Returns:**
- the condition

---

#### StatementTree
getThenStatement()

Returns the statement to be executed if the condition is true

**Returns:**
- the statement to be executed if the condition is true

---

#### StatementTree
getElseStatement()

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

**Returns:**
- the statement to be executed if the condition is false

---

### Additional Sections

#### Interface IfTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
IfTree

extends
StatementTree
```

A tree node for an

if

statement.

For example:

```java
if (
condition
)

thenStatement

if (
condition
)

thenStatement

else

elseStatement
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.9

public interface

IfTree

extends

StatementTree

A tree node for an

if

statement.

For example:

```java
if (
condition
)

thenStatement

if (
condition
)

thenStatement

else

elseStatement
```

if (

condition

)

thenStatement

if (

condition

)

thenStatement

else

elseStatement

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

Returns the condition of the if-statement.

StatementTree

getElseStatement

()

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

StatementTree

getThenStatement

()

Returns the statement to be executed if the condition is true

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

Returns the condition of the if-statement.

StatementTree

getElseStatement

()

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

StatementTree

getThenStatement

()

Returns the statement to be executed if the condition is true

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the condition of the if-statement.

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

Returns the statement to be executed if the condition is true

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

Returns the condition of the if-statement.

**Returns:** the condition

- getThenStatement

```java
StatementTree
getThenStatement()
```

Returns the statement to be executed if the condition is true

**Returns:** the statement to be executed if the condition is true

- getElseStatement

```java
StatementTree
getElseStatement()
```

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

**Returns:** the statement to be executed if the condition is false

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the if-statement.

**Returns:** the condition

- getThenStatement

```java
StatementTree
getThenStatement()
```

Returns the statement to be executed if the condition is true

**Returns:** the statement to be executed if the condition is true

- getElseStatement

```java
StatementTree
getElseStatement()
```

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

**Returns:** the statement to be executed if the condition is false

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the if-statement.

**Returns:** the condition

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition of the if-statement.

getThenStatement

```java
StatementTree
getThenStatement()
```

Returns the statement to be executed if the condition is true

**Returns:** the statement to be executed if the condition is true

---

#### getThenStatement

StatementTree

getThenStatement()

Returns the statement to be executed if the condition is true

getElseStatement

```java
StatementTree
getElseStatement()
```

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

**Returns:** the statement to be executed if the condition is false

---

#### getElseStatement

StatementTree

getElseStatement()

Returns the statement to be executed if the condition is false,
or

null

if there is no such statement.

---

