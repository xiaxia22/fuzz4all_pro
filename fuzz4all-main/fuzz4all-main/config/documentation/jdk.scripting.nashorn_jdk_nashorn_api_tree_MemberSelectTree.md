# Interface MemberSelectTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\MemberSelectTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
MemberSelectTree

extends
ExpressionTree
```

A tree node for a member access expression.

For example:

```java
expression
.
identifier
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

The object expression whose member is being selected.

**Returns:**
- the object whose member is selected

---

#### String
getIdentifier()

Returns the name of the property.

**Returns:**
- the name of the property

---

### Additional Sections

#### Interface MemberSelectTree

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
MemberSelectTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a member access expression.

For example:

```java
expression
.
identifier
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

MemberSelectTree

extends

ExpressionTree

A tree node for a member access expression.

For example:

```java
expression
.
identifier
```

expression

.

identifier

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

The object expression whose member is being selected.

String

getIdentifier

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the property.

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

The object expression whose member is being selected.

String

getIdentifier

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the property.

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

The object expression whose member is being selected.

Returns the name of the property.

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

The object expression whose member is being selected.

**Returns:** the object whose member is selected

- getIdentifier

```java
String
getIdentifier()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the property.

**Returns:** the name of the property

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The object expression whose member is being selected.

**Returns:** the object whose member is selected

- getIdentifier

```java
String
getIdentifier()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the property.

**Returns:** the name of the property

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The object expression whose member is being selected.

**Returns:** the object whose member is selected

---

#### getExpression

ExpressionTree

getExpression()

The object expression whose member is being selected.

getIdentifier

```java
String
getIdentifier()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the property.

**Returns:** the name of the property

---

#### getIdentifier

String

getIdentifier()

Returns the name of the property.

---

