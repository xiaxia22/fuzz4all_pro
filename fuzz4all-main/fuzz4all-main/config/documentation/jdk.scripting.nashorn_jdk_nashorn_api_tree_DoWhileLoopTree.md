# Interface DoWhileLoopTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\DoWhileLoopTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
DoWhileLoopTree

extends
ConditionalLoopTree
```

A tree node for a 'do' statement.

For example:

```java
do

statement

while (
expression
);
```

**All Superinterfaces:** ConditionalLoopTree

,

LoopTree

,

StatementTree

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

Returns the condition expression of this do-while statement.

**Specified by:**
- getCondition

in interface

ConditionalLoopTree

**Returns:**
- the condition expression

---

#### StatementTree
getStatement()

The statement contained within this do-while statement.

**Specified by:**
- getStatement

in interface

LoopTree

**Returns:**
- the statement

---

### Additional Sections

#### Interface DoWhileLoopTree

**All Superinterfaces:** ConditionalLoopTree

,

LoopTree

,

StatementTree

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
DoWhileLoopTree

extends
ConditionalLoopTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'do' statement.

For example:

```java
do

statement

while (
expression
);
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

DoWhileLoopTree

extends

ConditionalLoopTree

A tree node for a 'do' statement.

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

getCondition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this do-while statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained within this do-while statement.

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

getCondition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this do-while statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained within this do-while statement.

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

Returns the condition expression of this do-while statement.

The statement contained within this do-while statement.

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

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this do-while statement.

**Specified by:** getCondition

in interface

ConditionalLoopTree
**Returns:** the condition expression

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained within this do-while statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this do-while statement.

**Specified by:** getCondition

in interface

ConditionalLoopTree
**Returns:** the condition expression

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained within this do-while statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this do-while statement.

**Specified by:** getCondition

in interface

ConditionalLoopTree
**Returns:** the condition expression

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition expression of this do-while statement.

getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained within this do-while statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### getStatement

StatementTree

getStatement()

The statement contained within this do-while statement.

---

