# Interface ArrayAccessTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ArrayAccessTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ArrayAccessTree

extends
ExpressionTree
```

A tree node for an array access expression.

For example:

```java
expression
[
index
]
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

Returns the array that is accessed.

**Returns:**
- the array that is accessed

---

#### ExpressionTree
getIndex()

Returns the index of the array element accessed.

**Returns:**
- the index expression

---

### Additional Sections

#### Interface ArrayAccessTree

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
ArrayAccessTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for an array access expression.

For example:

```java
expression
[
index
]
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ArrayAccessTree

extends

ExpressionTree

A tree node for an array access expression.

For example:

```java
expression
[
index
]
```

expression

[

index

]

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

Returns the array that is accessed.

ExpressionTree

getIndex

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the index of the array element accessed.

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

Returns the array that is accessed.

ExpressionTree

getIndex

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the index of the array element accessed.

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

Returns the array that is accessed.

Returns the index of the array element accessed.

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

Returns the array that is accessed.

**Returns:** the array that is accessed

- getIndex

```java
ExpressionTree
getIndex()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the index of the array element accessed.

**Returns:** the index expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the array that is accessed.

**Returns:** the array that is accessed

- getIndex

```java
ExpressionTree
getIndex()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the index of the array element accessed.

**Returns:** the index expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the array that is accessed.

**Returns:** the array that is accessed

---

#### getExpression

ExpressionTree

getExpression()

Returns the array that is accessed.

getIndex

```java
ExpressionTree
getIndex()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the index of the array element accessed.

**Returns:** the index expression

---

#### getIndex

ExpressionTree

getIndex()

Returns the index of the array element accessed.

---

