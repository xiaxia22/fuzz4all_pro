# Interface InstanceOfTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\InstanceOfTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
InstanceOfTree

extends
ExpressionTree
```

A tree node for an 'instanceof' expression.

For example:

```java
expression
instanceof
type
```

**All Superinterfaces:** ExpressionTree

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

Returns the expression whose type is being checked.

**Returns:**
- the expression whose type is being checked

---

#### Tree
getType()

Returns the type expression.

**Returns:**
- the type expression

---

### Additional Sections

#### Interface InstanceOfTree

**All Superinterfaces:** ExpressionTree

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
InstanceOfTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for an 'instanceof' expression.

For example:

```java
expression
instanceof
type
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

InstanceOfTree

extends

ExpressionTree

A tree node for an 'instanceof' expression.

For example:

```java
expression
instanceof
type
```

expression

instanceof

type

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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression whose type is being checked.

Tree

getType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the type expression.

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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression whose type is being checked.

Tree

getType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the type expression.

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

Returns the expression whose type is being checked.

Returns the type expression.

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

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression whose type is being checked.

**Returns:** the expression whose type is being checked

- getType

```java
Tree
getType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the type expression.

**Returns:** the type expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression whose type is being checked.

**Returns:** the expression whose type is being checked

- getType

```java
Tree
getType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the type expression.

**Returns:** the type expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression whose type is being checked.

**Returns:** the expression whose type is being checked

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression whose type is being checked.

getType

```java
Tree
getType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the type expression.

**Returns:** the type expression

---

#### getType

Tree

getType()

Returns the type expression.

---

