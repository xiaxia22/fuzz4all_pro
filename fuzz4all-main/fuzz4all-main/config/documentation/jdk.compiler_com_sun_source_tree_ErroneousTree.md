# Interface ErroneousTree

**Source:** `jdk.compiler\com\sun\source\tree\ErroneousTree.html`

### Class Description

```java
public interface
ErroneousTree

extends
ExpressionTree
```

A tree node to stand in for a malformed expression.

**All Superinterfaces:** ExpressionTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
Tree
> getErrorTrees()

Returns any trees that were saved in this node.

**Returns:**
- the trees

---

### Additional Sections

#### Interface ErroneousTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
ErroneousTree

extends
ExpressionTree
```

A tree node to stand in for a malformed expression.

**Since:** 1.6

public interface

ErroneousTree

extends

ExpressionTree

A tree node to stand in for a malformed expression.

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

List

<? extends

Tree

>

getErrorTrees

()

Returns any trees that were saved in this node.

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

List

<? extends

Tree

>

getErrorTrees

()

Returns any trees that were saved in this node.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns any trees that were saved in this node.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getErrorTrees

```java
List
<? extends
Tree
> getErrorTrees()
```

Returns any trees that were saved in this node.

**Returns:** the trees

Method Detail

- getErrorTrees

```java
List
<? extends
Tree
> getErrorTrees()
```

Returns any trees that were saved in this node.

**Returns:** the trees

---

#### Method Detail

getErrorTrees

```java
List
<? extends
Tree
> getErrorTrees()
```

Returns any trees that were saved in this node.

**Returns:** the trees

---

#### getErrorTrees

List

<? extends

Tree

> getErrorTrees()

Returns any trees that were saved in this node.

---

