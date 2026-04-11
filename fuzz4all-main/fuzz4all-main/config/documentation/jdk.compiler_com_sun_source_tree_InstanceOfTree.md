# Interface InstanceOfTree

**Source:** `jdk.compiler\com\sun\source\tree\InstanceOfTree.html`

### Class Description

```java
public interface
InstanceOfTree

extends
ExpressionTree
```

A tree node for an

instanceof

expression.

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

Returns the expression to be tested.

**Returns:**
- the expression

---

#### Tree
getType()

Returns the type for which to check.

**Returns:**
- the type

---

### Additional Sections

#### Interface InstanceOfTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
InstanceOfTree

extends
ExpressionTree
```

A tree node for an

instanceof

expression.

For example:

```java
expression
instanceof
type
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.20.2

public interface

InstanceOfTree

extends

ExpressionTree

A tree node for an

instanceof

expression.

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

Returns the expression to be tested.

Tree

getType

()

Returns the type for which to check.

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

Returns the expression to be tested.

Tree

getType

()

Returns the type for which to check.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression to be tested.

Returns the type for which to check.

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

Returns the expression to be tested.

**Returns:** the expression

- getType

```java
Tree
getType()
```

Returns the type for which to check.

**Returns:** the type

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression to be tested.

**Returns:** the expression

- getType

```java
Tree
getType()
```

Returns the type for which to check.

**Returns:** the type

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression to be tested.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression to be tested.

getType

```java
Tree
getType()
```

Returns the type for which to check.

**Returns:** the type

---

#### getType

Tree

getType()

Returns the type for which to check.

---

