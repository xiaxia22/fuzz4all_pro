# Interface ForLoopTree

**Source:** `jdk.compiler\com\sun\source\tree\ForLoopTree.html`

### Class Description

```java
public interface
ForLoopTree

extends
StatementTree
```

A tree node for a basic

for

loop statement.

For example:

```java
for (
initializer
;
condition
;
update
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

#### List
<? extends
StatementTree
> getInitializer()

Returns any initializers of the

for

statement.
The result will be an empty list if there are
no initializers

**Returns:**
- the initializers

---

#### ExpressionTree
getCondition()

Returns the condition of the

for

statement.
May be

null

if there is no condition.

**Returns:**
- the condition

---

#### List
<? extends
ExpressionStatementTree
> getUpdate()

Returns any update expressions of the

for

statement.

**Returns:**
- the update expressions

---

#### StatementTree
getStatement()

Returns the body of the

for

statement.

**Returns:**
- the body

---

### Additional Sections

#### Interface ForLoopTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
ForLoopTree

extends
StatementTree
```

A tree node for a basic

for

loop statement.

For example:

```java
for (
initializer
;
condition
;
update
)

statement
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.14.1

public interface

ForLoopTree

extends

StatementTree

A tree node for a basic

for

loop statement.

For example:

```java
for (
initializer
;
condition
;
update
)

statement
```

for (

initializer

;

condition

;

update

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

Returns the condition of the

for

statement.

List

<? extends

StatementTree

>

getInitializer

()

Returns any initializers of the

for

statement.

StatementTree

getStatement

()

Returns the body of the

for

statement.

List

<? extends

ExpressionStatementTree

>

getUpdate

()

Returns any update expressions of the

for

statement.

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

Returns the condition of the

for

statement.

List

<? extends

StatementTree

>

getInitializer

()

Returns any initializers of the

for

statement.

StatementTree

getStatement

()

Returns the body of the

for

statement.

List

<? extends

ExpressionStatementTree

>

getUpdate

()

Returns any update expressions of the

for

statement.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the condition of the

for

statement.

Returns any initializers of the

for

statement.

Returns the body of the

for

statement.

Returns any update expressions of the

for

statement.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getInitializer

```java
List
<? extends
StatementTree
> getInitializer()
```

Returns any initializers of the

for

statement.
The result will be an empty list if there are
no initializers

**Returns:** the initializers

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the

for

statement.
May be

null

if there is no condition.

**Returns:** the condition

- getUpdate

```java
List
<? extends
ExpressionStatementTree
> getUpdate()
```

Returns any update expressions of the

for

statement.

**Returns:** the update expressions

- getStatement

```java
StatementTree
getStatement()
```

Returns the body of the

for

statement.

**Returns:** the body

Method Detail

- getInitializer

```java
List
<? extends
StatementTree
> getInitializer()
```

Returns any initializers of the

for

statement.
The result will be an empty list if there are
no initializers

**Returns:** the initializers

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the

for

statement.
May be

null

if there is no condition.

**Returns:** the condition

- getUpdate

```java
List
<? extends
ExpressionStatementTree
> getUpdate()
```

Returns any update expressions of the

for

statement.

**Returns:** the update expressions

- getStatement

```java
StatementTree
getStatement()
```

Returns the body of the

for

statement.

**Returns:** the body

---

#### Method Detail

getInitializer

```java
List
<? extends
StatementTree
> getInitializer()
```

Returns any initializers of the

for

statement.
The result will be an empty list if there are
no initializers

**Returns:** the initializers

---

#### getInitializer

List

<? extends

StatementTree

> getInitializer()

Returns any initializers of the

for

statement.
The result will be an empty list if there are
no initializers

getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition of the

for

statement.
May be

null

if there is no condition.

**Returns:** the condition

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition of the

for

statement.
May be

null

if there is no condition.

getUpdate

```java
List
<? extends
ExpressionStatementTree
> getUpdate()
```

Returns any update expressions of the

for

statement.

**Returns:** the update expressions

---

#### getUpdate

List

<? extends

ExpressionStatementTree

> getUpdate()

Returns any update expressions of the

for

statement.

getStatement

```java
StatementTree
getStatement()
```

Returns the body of the

for

statement.

**Returns:** the body

---

#### getStatement

StatementTree

getStatement()

Returns the body of the

for

statement.

---

