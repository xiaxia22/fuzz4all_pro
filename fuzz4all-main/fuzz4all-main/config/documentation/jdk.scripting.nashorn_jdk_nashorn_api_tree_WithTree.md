# Interface WithTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\WithTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
WithTree

extends
StatementTree
```

A tree node for a 'with' statement.

For example:

```java
with (
scope
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
getScope()

The scope object expression for this 'with' statement.

**Returns:**
- the scope object

---

#### StatementTree
getStatement()

The statement contained in this 'with' statement.

**Returns:**
- the statement contained

---

### Additional Sections

#### Interface WithTree

**All Superinterfaces:** StatementTree

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
WithTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'with' statement.

For example:

```java
with (
scope
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

WithTree

extends

StatementTree

A tree node for a 'with' statement.

For example:

```java
with (
scope
)

statement
```

with (

scope

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

getScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

The scope object expression for this 'with' statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this 'with' statement.

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

getScope

()

Deprecated, for removal: This API element is subject to removal in a future version.

The scope object expression for this 'with' statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this 'with' statement.

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

The scope object expression for this 'with' statement.

The statement contained in this 'with' statement.

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

- getScope

```java
ExpressionTree
getScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The scope object expression for this 'with' statement.

**Returns:** the scope object

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this 'with' statement.

**Returns:** the statement contained

Method Detail

- getScope

```java
ExpressionTree
getScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The scope object expression for this 'with' statement.

**Returns:** the scope object

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this 'with' statement.

**Returns:** the statement contained

---

#### Method Detail

getScope

```java
ExpressionTree
getScope()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The scope object expression for this 'with' statement.

**Returns:** the scope object

---

#### getScope

ExpressionTree

getScope()

The scope object expression for this 'with' statement.

getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this 'with' statement.

**Returns:** the statement contained

---

#### getStatement

StatementTree

getStatement()

The statement contained in this 'with' statement.

---

