# Interface ForLoopTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ForLoopTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ForLoopTree

extends
ConditionalLoopTree
```

A tree node for a basic 'for' loop statement.

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
getInitializer()

Returns the initializer expression of this 'for' statement.

**Returns:**
- the initializer expression

---

#### ExpressionTree
getCondition()

Returns the condition expression of this 'for' statement.

**Specified by:**
- getCondition

in interface

ConditionalLoopTree

**Returns:**
- the condition expression

---

#### ExpressionTree
getUpdate()

Returns the update expression of this 'for' statement.

**Returns:**
- the update expression

---

#### StatementTree
getStatement()

Returns the statement contained in this 'for' statement.

**Specified by:**
- getStatement

in interface

LoopTree

**Returns:**
- the statement

---

### Additional Sections

#### Interface ForLoopTree

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
ForLoopTree

extends
ConditionalLoopTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a basic 'for' loop statement.

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

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ForLoopTree

extends

ConditionalLoopTree

A tree node for a basic 'for' loop statement.

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

Returns the condition expression of this 'for' statement.

ExpressionTree

getInitializer

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initializer expression of this 'for' statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement contained in this 'for' statement.

ExpressionTree

getUpdate

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the update expression of this 'for' statement.

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

Returns the condition expression of this 'for' statement.

ExpressionTree

getInitializer

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initializer expression of this 'for' statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement contained in this 'for' statement.

ExpressionTree

getUpdate

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the update expression of this 'for' statement.

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

Returns the condition expression of this 'for' statement.

Returns the initializer expression of this 'for' statement.

Returns the statement contained in this 'for' statement.

Returns the update expression of this 'for' statement.

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

- getInitializer

```java
ExpressionTree
getInitializer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initializer expression of this 'for' statement.

**Returns:** the initializer expression

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this 'for' statement.

**Specified by:** getCondition

in interface

ConditionalLoopTree
**Returns:** the condition expression

- getUpdate

```java
ExpressionTree
getUpdate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the update expression of this 'for' statement.

**Returns:** the update expression

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement contained in this 'for' statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

Method Detail

- getInitializer

```java
ExpressionTree
getInitializer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initializer expression of this 'for' statement.

**Returns:** the initializer expression

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this 'for' statement.

**Specified by:** getCondition

in interface

ConditionalLoopTree
**Returns:** the condition expression

- getUpdate

```java
ExpressionTree
getUpdate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the update expression of this 'for' statement.

**Returns:** the update expression

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement contained in this 'for' statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### Method Detail

getInitializer

```java
ExpressionTree
getInitializer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initializer expression of this 'for' statement.

**Returns:** the initializer expression

---

#### getInitializer

ExpressionTree

getInitializer()

Returns the initializer expression of this 'for' statement.

getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this 'for' statement.

**Specified by:** getCondition

in interface

ConditionalLoopTree
**Returns:** the condition expression

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition expression of this 'for' statement.

getUpdate

```java
ExpressionTree
getUpdate()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the update expression of this 'for' statement.

**Returns:** the update expression

---

#### getUpdate

ExpressionTree

getUpdate()

Returns the update expression of this 'for' statement.

getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement contained in this 'for' statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### getStatement

StatementTree

getStatement()

Returns the statement contained in this 'for' statement.

---

