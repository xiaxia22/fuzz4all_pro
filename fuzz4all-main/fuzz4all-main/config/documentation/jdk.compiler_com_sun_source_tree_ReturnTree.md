# Interface ReturnTree

**Source:** `jdk.compiler\com\sun\source\tree\ReturnTree.html`

### Class Description

```java
public interface
ReturnTree

extends
StatementTree
```

A tree node for a

return

statement.

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

Returns the expression to be returned.

**Returns:**
- the expression

---

### Additional Sections

#### Interface ReturnTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
ReturnTree

extends
StatementTree
```

A tree node for a

return

statement.

For example:

```java
return;
return
expression
;
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.17

public interface

ReturnTree

extends

StatementTree

A tree node for a

return

statement.

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

Returns the expression to be returned.

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

Returns the expression to be returned.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression to be returned.

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

Returns the expression to be returned.

**Returns:** the expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression to be returned.

**Returns:** the expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression to be returned.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression to be returned.

---

