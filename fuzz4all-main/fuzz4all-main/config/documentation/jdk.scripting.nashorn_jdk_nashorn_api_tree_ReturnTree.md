# Interface ReturnTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ReturnTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ReturnTree

extends
StatementTree
```

A tree node for a 'return' statement.

For example:

```java
return;
return
expression
;
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
getExpression()

Returns the expression being returned. This is null if no value
is being returned. i.e., empty return statement.

**Returns:**
- the returned expression

---

### Additional Sections

#### Interface ReturnTree

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
ReturnTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'return' statement.

For example:

```java
return;
return
expression
;
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ReturnTree

extends

StatementTree

A tree node for a 'return' statement.

For example:

```java
return;
return
expression
;
```

return;
return

expression

;

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

Returns the expression being returned.

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

Returns the expression being returned.

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

Returns the expression being returned.

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

Returns the expression being returned. This is null if no value
is being returned. i.e., empty return statement.

**Returns:** the returned expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression being returned. This is null if no value
is being returned. i.e., empty return statement.

**Returns:** the returned expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression being returned. This is null if no value
is being returned. i.e., empty return statement.

**Returns:** the returned expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression being returned. This is null if no value
is being returned. i.e., empty return statement.

---

