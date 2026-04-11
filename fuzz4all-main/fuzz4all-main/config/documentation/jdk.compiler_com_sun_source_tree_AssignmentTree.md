# Interface AssignmentTree

**Source:** `jdk.compiler\com\sun\source\tree\AssignmentTree.html`

### Class Description

```java
public interface
AssignmentTree

extends
ExpressionTree
```

A tree node for an assignment expression.

For example:

```java
variable
=
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

Returns the variable being assigned to.

**Returns:**
- the variable

---

#### ExpressionTree
getExpression()

Returns the expression being assigned to the variable.

**Returns:**
- the expression

---

### Additional Sections

#### Interface AssignmentTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
AssignmentTree

extends
ExpressionTree
```

A tree node for an assignment expression.

For example:

```java
variable
=
expression
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.26.1

public interface

AssignmentTree

extends

ExpressionTree

A tree node for an assignment expression.

For example:

```java
variable
=
expression
```

variable

=

expression

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

Returns the expression being assigned to the variable.

ExpressionTree

getVariable

()

Returns the variable being assigned to.

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

Returns the expression being assigned to the variable.

ExpressionTree

getVariable

()

Returns the variable being assigned to.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression being assigned to the variable.

Returns the variable being assigned to.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getVariable

```java
ExpressionTree
getVariable()
```

Returns the variable being assigned to.

**Returns:** the variable

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression being assigned to the variable.

**Returns:** the expression

Method Detail

- getVariable

```java
ExpressionTree
getVariable()
```

Returns the variable being assigned to.

**Returns:** the variable

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression being assigned to the variable.

**Returns:** the expression

---

#### Method Detail

getVariable

```java
ExpressionTree
getVariable()
```

Returns the variable being assigned to.

**Returns:** the variable

---

#### getVariable

ExpressionTree

getVariable()

Returns the variable being assigned to.

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression being assigned to the variable.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression being assigned to the variable.

---

