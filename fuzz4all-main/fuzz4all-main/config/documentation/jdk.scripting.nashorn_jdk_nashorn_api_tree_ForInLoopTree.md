# Interface ForInLoopTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ForInLoopTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ForInLoopTree

extends
LoopTree
```

A tree node for for..in statement

For example:

```java
for (
variable
in
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

The for..in left hand side expression.

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

The statement contained in this for..in statement.

**Specified by:**
- getStatement

in interface

LoopTree

**Returns:**
- the statement

---

#### boolean isForEach()

Returns if this is a for..each..in statement or not.

**Returns:**
- true if this is a for..each..in statement

---

### Additional Sections

#### Interface ForInLoopTree

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
ForInLoopTree

extends
LoopTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for for..in statement

For example:

```java
for (
variable
in
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

ForInLoopTree

extends

LoopTree

A tree node for for..in statement

For example:

```java
for (
variable
in
expression
)

statement
```

for (

variable

in

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

The statement contained in this for..in statement.

ExpressionTree

getVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

The for..in left hand side expression.

boolean

isForEach

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a for..each..in statement or not.

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

The statement contained in this for..in statement.

ExpressionTree

getVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

The for..in left hand side expression.

boolean

isForEach

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a for..each..in statement or not.

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

The statement contained in this for..in statement.

The for..in left hand side expression.

Returns if this is a for..each..in statement or not.

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

The for..in left hand side expression.

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

The statement contained in this for..in statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

- isForEach

```java
boolean isForEach()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a for..each..in statement or not.

**Returns:** true if this is a for..each..in statement

Method Detail

- getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The for..in left hand side expression.

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

The statement contained in this for..in statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

- isForEach

```java
boolean isForEach()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a for..each..in statement or not.

**Returns:** true if this is a for..each..in statement

---

#### Method Detail

getVariable

```java
ExpressionTree
getVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The for..in left hand side expression.

**Returns:** the left hand side expression

---

#### getVariable

ExpressionTree

getVariable()

The for..in left hand side expression.

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

The statement contained in this for..in statement.

**Specified by:** getStatement

in interface

LoopTree
**Returns:** the statement

---

#### getStatement

StatementTree

getStatement()

The statement contained in this for..in statement.

isForEach

```java
boolean isForEach()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a for..each..in statement or not.

**Returns:** true if this is a for..each..in statement

---

#### isForEach

boolean isForEach()

Returns if this is a for..each..in statement or not.

---

