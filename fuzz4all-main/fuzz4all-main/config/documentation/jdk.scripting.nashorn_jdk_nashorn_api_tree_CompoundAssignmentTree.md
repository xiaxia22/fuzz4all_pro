# Interface CompoundAssignmentTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\CompoundAssignmentTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CompoundAssignmentTree

extends
ExpressionTree
```

A tree node for compound assignment operator.
Use

getKind

to determine the kind of operator.

For example:

```java
variable

operator

expression
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
getVariable()

Returns the left hand side (LHS) of this assignment.

**Returns:**
- left hand side (LHS) expression

---

#### ExpressionTree
getExpression()

Returns the right hand side (RHS) of this assignment.

**Returns:**
- right hand side (RHS) expression

---

### Additional Sections

#### Interface CompoundAssignmentTree

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
CompoundAssignmentTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for compound assignment operator.
Use

getKind

to determine the kind of operator.

For example:

```java
variable

operator

expression
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

CompoundAssignmentTree

extends

ExpressionTree

A tree node for compound assignment operator.
Use

getKind

to determine the kind of operator.

For example:

```java
variable

operator

expression
```

variable

operator

expression

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

Returns the right hand side (RHS) of this assignment.

ExpressionTree

getVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the left hand side (LHS) of this assignment.

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

Returns the right hand side (RHS) of this assignment.

ExpressionTree

getVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the left hand side (LHS) of this assignment.

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

Returns the right hand side (RHS) of this assignment.

Returns the left hand side (LHS) of this assignment.

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

- getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the left hand side (LHS) of this assignment.

**Returns:** left hand side (LHS) expression

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the right hand side (RHS) of this assignment.

**Returns:** right hand side (RHS) expression

Method Detail

- getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the left hand side (LHS) of this assignment.

**Returns:** left hand side (LHS) expression

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the right hand side (RHS) of this assignment.

**Returns:** right hand side (RHS) expression

---

#### Method Detail

getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the left hand side (LHS) of this assignment.

**Returns:** left hand side (LHS) expression

---

#### getVariable

ExpressionTree

getVariable()

Returns the left hand side (LHS) of this assignment.

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the right hand side (RHS) of this assignment.

**Returns:** right hand side (RHS) expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the right hand side (RHS) of this assignment.

---

