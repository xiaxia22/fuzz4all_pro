# Interface ForOfLoopTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ForOfLoopTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ForOfLoopTree

extends
LoopTree
```

A tree node for

for..of statement

.

For example:

```java
for (
variable
of
expression
)

statement
```

**All Superinterfaces:** LoopTree

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
getVariable()

The for..of left hand side expression.

**Returns:**
- the left hand side expression

---

#### ExpressionTree
getExpression()

The object or array being whose properties are iterated.

**Returns:**
- the object or array expression being iterated

---

#### StatementTree
getStatement()

The statement contained in this for..of statement.

**Specified by:**
- getStatement

in interface

LoopTree

**Returns:**
- the statement

---

### Additional Sections

#### Interface ForOfLoopTree

**All Superinterfaces:** LoopTree

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
ForOfLoopTree

extends
LoopTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for

for..of statement

.

For example:

```java
for (
variable
of
expression
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

ForOfLoopTree

extends

LoopTree

A tree node for

for..of statement

.

For example:

```java
for (
variable
of
expression
)

statement
```

for (

variable

of

expression

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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

The object or array being whose properties are iterated.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this for..of statement.

ExpressionTree

getVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

The for..of left hand side expression.

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

The object or array being whose properties are iterated.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this for..of statement.

ExpressionTree

getVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

The for..of left hand side expression.

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

The object or array being whose properties are iterated.

The statement contained in this for..of statement.

The for..of left hand side expression.

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

The for..of left hand side expression.

**Returns:** the left hand side expression

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The object or array being whose properties are iterated.

**Returns:** the object or array expression being iterated

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this for..of statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

Method Detail

- getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The for..of left hand side expression.

**Returns:** the left hand side expression

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The object or array being whose properties are iterated.

**Returns:** the object or array expression being iterated

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this for..of statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### Method Detail

getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The for..of left hand side expression.

**Returns:** the left hand side expression

---

#### getVariable

ExpressionTree

getVariable()

The for..of left hand side expression.

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The object or array being whose properties are iterated.

**Returns:** the object or array expression being iterated

---

#### getExpression

ExpressionTree

getExpression()

The object or array being whose properties are iterated.

getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The statement contained in this for..of statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### getStatement

StatementTree

getStatement()

The statement contained in this for..of statement.

---

