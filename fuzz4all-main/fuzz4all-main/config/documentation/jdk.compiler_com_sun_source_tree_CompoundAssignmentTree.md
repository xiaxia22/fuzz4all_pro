# Interface CompoundAssignmentTree

**Source:** `jdk.compiler\com\sun\source\tree\CompoundAssignmentTree.html`

### Class Description

```java
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

Returns the variable on the left hand side of the compound assignment.

**Returns:**
- the variable

---

#### ExpressionTree
getExpression()

Returns the expression on the right hand side of the compound assignment.

**Returns:**
- the expression

---

### Additional Sections

#### Interface CompoundAssignmentTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
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

**Since:** 1.6
**See The Java™ Language Specification :** section 15.26.2

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

Returns the expression on the right hand side of the compound assignment.

ExpressionTree

getVariable

()

Returns the variable on the left hand side of the compound assignment.

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

Returns the expression on the right hand side of the compound assignment.

ExpressionTree

getVariable

()

Returns the variable on the left hand side of the compound assignment.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression on the right hand side of the compound assignment.

Returns the variable on the left hand side of the compound assignment.

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

Returns the variable on the left hand side of the compound assignment.

**Returns:** the variable

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression on the right hand side of the compound assignment.

**Returns:** the expression

Method Detail

- getVariable

```java
ExpressionTree
getVariable()
```

Returns the variable on the left hand side of the compound assignment.

**Returns:** the variable

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression on the right hand side of the compound assignment.

**Returns:** the expression

---

#### Method Detail

getVariable

```java
ExpressionTree
getVariable()
```

Returns the variable on the left hand side of the compound assignment.

**Returns:** the variable

---

#### getVariable

ExpressionTree

getVariable()

Returns the variable on the left hand side of the compound assignment.

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression on the right hand side of the compound assignment.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression on the right hand side of the compound assignment.

---

