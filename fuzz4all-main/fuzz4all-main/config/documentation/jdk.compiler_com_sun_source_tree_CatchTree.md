# Interface CatchTree

**Source:** `jdk.compiler\com\sun\source\tree\CatchTree.html`

### Class Description

```java
public interface
CatchTree

extends
Tree
```

A tree node for a

catch

block in a

try

statement.

For example:

```java
catch (
parameter
)

block
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### VariableTree
getParameter()

Returns the catch variable.
A multi-catch variable will have a

UnionTypeTree

as the type of the variable.

**Returns:**
- the catch variable

---

#### BlockTree
getBlock()

Returns the catch block.

**Returns:**
- the catch block

---

### Additional Sections

#### Interface CatchTree

**All Superinterfaces:** Tree

```java
public interface
CatchTree

extends
Tree
```

A tree node for a

catch

block in a

try

statement.

For example:

```java
catch (
parameter
)

block
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.20

public interface

CatchTree

extends

Tree

A tree node for a

catch

block in a

try

statement.

For example:

```java
catch (
parameter
)

block
```

catch (

parameter

)

block

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

BlockTree

getBlock

()

Returns the catch block.

VariableTree

getParameter

()

Returns the catch variable.

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

BlockTree

getBlock

()

Returns the catch block.

VariableTree

getParameter

()

Returns the catch variable.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the catch block.

Returns the catch variable.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getParameter

```java
VariableTree
getParameter()
```

Returns the catch variable.
A multi-catch variable will have a

UnionTypeTree

as the type of the variable.

**Returns:** the catch variable

- getBlock

```java
BlockTree
getBlock()
```

Returns the catch block.

**Returns:** the catch block

Method Detail

- getParameter

```java
VariableTree
getParameter()
```

Returns the catch variable.
A multi-catch variable will have a

UnionTypeTree

as the type of the variable.

**Returns:** the catch variable

- getBlock

```java
BlockTree
getBlock()
```

Returns the catch block.

**Returns:** the catch block

---

#### Method Detail

getParameter

```java
VariableTree
getParameter()
```

Returns the catch variable.
A multi-catch variable will have a

UnionTypeTree

as the type of the variable.

**Returns:** the catch variable

---

#### getParameter

VariableTree

getParameter()

Returns the catch variable.
A multi-catch variable will have a

UnionTypeTree

as the type of the variable.

getBlock

```java
BlockTree
getBlock()
```

Returns the catch block.

**Returns:** the catch block

---

#### getBlock

BlockTree

getBlock()

Returns the catch block.

---

