# Interface AssertTree

**Source:** `jdk.compiler\com\sun\source\tree\AssertTree.html`

### Class Description

```java
public interface
AssertTree

extends
StatementTree
```

A tree node for an

assert

statement.

For example:

```java
assert
condition
;

assert
condition
:
detail
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
getCondition()

Returns the condition being asserted.

**Returns:**
- the condition

---

#### ExpressionTree
getDetail()

Returns the detail expression.

**Returns:**
- the detail expression

---

### Additional Sections

#### Interface AssertTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
AssertTree

extends
StatementTree
```

A tree node for an

assert

statement.

For example:

```java
assert
condition
;

assert
condition
:
detail
;
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.10

public interface

AssertTree

extends

StatementTree

A tree node for an

assert

statement.

For example:

```java
assert
condition
;

assert
condition
:
detail
;
```

assert

condition

;

assert

condition

:

detail

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

getCondition

()

Returns the condition being asserted.

ExpressionTree

getDetail

()

Returns the detail expression.

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

getCondition

()

Returns the condition being asserted.

ExpressionTree

getDetail

()

Returns the detail expression.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the condition being asserted.

Returns the detail expression.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition being asserted.

**Returns:** the condition

- getDetail

```java
ExpressionTree
getDetail()
```

Returns the detail expression.

**Returns:** the detail expression

Method Detail

- getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition being asserted.

**Returns:** the condition

- getDetail

```java
ExpressionTree
getDetail()
```

Returns the detail expression.

**Returns:** the detail expression

---

#### Method Detail

getCondition

```java
ExpressionTree
getCondition()
```

Returns the condition being asserted.

**Returns:** the condition

---

#### getCondition

ExpressionTree

getCondition()

Returns the condition being asserted.

getDetail

```java
ExpressionTree
getDetail()
```

Returns the detail expression.

**Returns:** the detail expression

---

#### getDetail

ExpressionTree

getDetail()

Returns the detail expression.

---

