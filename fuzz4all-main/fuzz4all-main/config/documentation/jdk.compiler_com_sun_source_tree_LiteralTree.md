# Interface LiteralTree

**Source:** `jdk.compiler\com\sun\source\tree\LiteralTree.html`

### Class Description

```java
public interface
LiteralTree

extends
ExpressionTree
```

A tree node for a literal expression.
Use

getKind

to determine the kind of literal.

For example:

```java
value
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

#### Object
getValue()

Returns the value of the literal expression.
The value will be a boxed primitive value, a String, or

null

.

**Returns:**
- the value

---

### Additional Sections

#### Interface LiteralTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
LiteralTree

extends
ExpressionTree
```

A tree node for a literal expression.
Use

getKind

to determine the kind of literal.

For example:

```java
value
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.28

public interface

LiteralTree

extends

ExpressionTree

A tree node for a literal expression.
Use

getKind

to determine the kind of literal.

For example:

```java
value
```

value

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

Object

getValue

()

Returns the value of the literal expression.

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

Object

getValue

()

Returns the value of the literal expression.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the value of the literal expression.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
Object
getValue()
```

Returns the value of the literal expression.
The value will be a boxed primitive value, a String, or

null

.

**Returns:** the value

Method Detail

- getValue

```java
Object
getValue()
```

Returns the value of the literal expression.
The value will be a boxed primitive value, a String, or

null

.

**Returns:** the value

---

#### Method Detail

getValue

```java
Object
getValue()
```

Returns the value of the literal expression.
The value will be a boxed primitive value, a String, or

null

.

**Returns:** the value

---

#### getValue

Object

getValue()

Returns the value of the literal expression.
The value will be a boxed primitive value, a String, or

null

.

---

