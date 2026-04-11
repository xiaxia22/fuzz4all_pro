# Interface MemberSelectTree

**Source:** `jdk.compiler\com\sun\source\tree\MemberSelectTree.html`

### Class Description

```java
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

Returns the expression for which a member is to be selected.

**Returns:**
- the expression.

---

#### Name
getIdentifier()

Returns the name of the member to be selected.

**Returns:**
- the member

---

### Additional Sections

#### Interface MemberSelectTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
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

**Since:** 1.6
**See The Java™ Language Specification :** sections 6.5, 15.11,and 15.12

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

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ExpressionTree

getExpression

()

Returns the expression for which a member is to be selected.

Name

getIdentifier

()

Returns the name of the member to be selected.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ExpressionTree

getExpression

()

Returns the expression for which a member is to be selected.

Name

getIdentifier

()

Returns the name of the member to be selected.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression for which a member is to be selected.

Returns the name of the member to be selected.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for which a member is to be selected.

**Returns:** the expression.

- getIdentifier

```java
Name
getIdentifier()
```

Returns the name of the member to be selected.

**Returns:** the member

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for which a member is to be selected.

**Returns:** the expression.

- getIdentifier

```java
Name
getIdentifier()
```

Returns the name of the member to be selected.

**Returns:** the member

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for which a member is to be selected.

**Returns:** the expression.

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression for which a member is to be selected.

getIdentifier

```java
Name
getIdentifier()
```

Returns the name of the member to be selected.

**Returns:** the member

---

#### getIdentifier

Name

getIdentifier()

Returns the name of the member to be selected.

---

