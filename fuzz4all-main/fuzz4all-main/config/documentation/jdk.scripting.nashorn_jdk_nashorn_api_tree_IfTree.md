# Interface IfTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\IfTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
IfTree

extends
StatementTree
```

A tree node for an 'if' statement.

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

Returns the condition expression of this 'if' statement.

**Returns:**
- the condition expression

---

#### StatementTree
getThenStatement()

Returns the 'then' statement of this 'if' statement.

**Returns:**
- the 'then' statement

---

#### StatementTree
getElseStatement()

Returns the then statement of this 'if' statement.
null if this if statement has no else branch.

**Returns:**
- the 'else' statement

---

### Additional Sections

#### Interface IfTree

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
IfTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for an 'if' statement.

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

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

IfTree

extends

StatementTree

A tree node for an 'if' statement.

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

Returns the condition expression of this 'if' statement.

StatementTree

getElseStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the then statement of this 'if' statement.

StatementTree

getThenStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'then' statement of this 'if' statement.

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

Returns the condition expression of this 'if' statement.

StatementTree

getElseStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the then statement of this 'if' statement.

StatementTree

getThenStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'then' statement of this 'if' statement.

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

Returns the condition expression of this 'if' statement.

Returns the then statement of this 'if' statement.

Returns the 'then' statement of this 'if' statement.

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

Returns the condition expression of this 'if' statement.

**Returns:** the condition expression

- getThenStatement

```java
StatementTree
getThenStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'then' statement of this 'if' statement.

**Returns:** the 'then' statement

- getElseStatement

```java
StatementTree
getElseStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the then statement of this 'if' statement.
null if this if statement has no else branch.

**Returns:** the 'else' statement

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this 'if' statement.

**Returns:** the condition expression

- getThenStatement

```java
StatementTree
getThenStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'then' statement of this 'if' statement.

**Returns:** the 'then' statement

- getElseStatement

```java
StatementTree
getElseStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the then statement of this 'if' statement.
null if this if statement has no else branch.

**Returns:** the 'else' statement

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the condition expression of this 'if' statement.

**Returns:** the condition expression

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition expression of this 'if' statement.

getThenStatement

```java
StatementTree
getThenStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'then' statement of this 'if' statement.

**Returns:** the 'then' statement

---

#### getThenStatement

StatementTree

getThenStatement()

Returns the 'then' statement of this 'if' statement.

getElseStatement

```java
StatementTree
getElseStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the then statement of this 'if' statement.
null if this if statement has no else branch.

**Returns:** the 'else' statement

---

#### getElseStatement

StatementTree

getElseStatement()

Returns the then statement of this 'if' statement.
null if this if statement has no else branch.

---

