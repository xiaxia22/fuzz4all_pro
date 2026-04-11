# Interface TryTree

**Source:** `jdk.compiler\com\sun\source\tree\TryTree.html`

### Class Description

```java
public interface
TryTree

extends
StatementTree
```

A tree node for a

try

statement.

For example:

```java
try

block

catches

finally

finallyBlock
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

#### BlockTree
getBlock()

Returns the block of the

try

statement.

**Returns:**
- the block

---

#### List
<? extends
CatchTree
> getCatches()

Returns any catch blocks provided in the

try

statement.
The result will be an empty list if there are no
catch blocks.

**Returns:**
- the catch blocks

---

#### BlockTree
getFinallyBlock()

Returns the finally block provided in the

try

statement,
or

null

if there is none.

**Returns:**
- the finally block

---

#### List
<? extends
Tree
> getResources()

Returns any resource declarations provided in the

try

statement.
The result will be an empty list if there are no
resource declarations.

**Returns:**
- the resource declarations

---

### Additional Sections

#### Interface TryTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
TryTree

extends
StatementTree
```

A tree node for a

try

statement.

For example:

```java
try

block

catches

finally

finallyBlock
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.20

public interface

TryTree

extends

StatementTree

A tree node for a

try

statement.

For example:

```java
try

block

catches

finally

finallyBlock
```

try

block

catches

finally

finallyBlock

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

Returns the block of the

try

statement.

List

<? extends

CatchTree

>

getCatches

()

Returns any catch blocks provided in the

try

statement.

BlockTree

getFinallyBlock

()

Returns the finally block provided in the

try

statement,
or

null

if there is none.

List

<? extends

Tree

>

getResources

()

Returns any resource declarations provided in the

try

statement.

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

Returns the block of the

try

statement.

List

<? extends

CatchTree

>

getCatches

()

Returns any catch blocks provided in the

try

statement.

BlockTree

getFinallyBlock

()

Returns the finally block provided in the

try

statement,
or

null

if there is none.

List

<? extends

Tree

>

getResources

()

Returns any resource declarations provided in the

try

statement.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the block of the

try

statement.

Returns any catch blocks provided in the

try

statement.

Returns the finally block provided in the

try

statement,
or

null

if there is none.

Returns any resource declarations provided in the

try

statement.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getBlock

```java
BlockTree
getBlock()
```

Returns the block of the

try

statement.

**Returns:** the block

- getCatches

```java
List
<? extends
CatchTree
> getCatches()
```

Returns any catch blocks provided in the

try

statement.
The result will be an empty list if there are no
catch blocks.

**Returns:** the catch blocks

- getFinallyBlock

```java
BlockTree
getFinallyBlock()
```

Returns the finally block provided in the

try

statement,
or

null

if there is none.

**Returns:** the finally block

- getResources

```java
List
<? extends
Tree
> getResources()
```

Returns any resource declarations provided in the

try

statement.
The result will be an empty list if there are no
resource declarations.

**Returns:** the resource declarations

Method Detail

- getBlock

```java
BlockTree
getBlock()
```

Returns the block of the

try

statement.

**Returns:** the block

- getCatches

```java
List
<? extends
CatchTree
> getCatches()
```

Returns any catch blocks provided in the

try

statement.
The result will be an empty list if there are no
catch blocks.

**Returns:** the catch blocks

- getFinallyBlock

```java
BlockTree
getFinallyBlock()
```

Returns the finally block provided in the

try

statement,
or

null

if there is none.

**Returns:** the finally block

- getResources

```java
List
<? extends
Tree
> getResources()
```

Returns any resource declarations provided in the

try

statement.
The result will be an empty list if there are no
resource declarations.

**Returns:** the resource declarations

---

#### Method Detail

getBlock

```java
BlockTree
getBlock()
```

Returns the block of the

try

statement.

**Returns:** the block

---

#### getBlock

BlockTree

getBlock()

Returns the block of the

try

statement.

getCatches

```java
List
<? extends
CatchTree
> getCatches()
```

Returns any catch blocks provided in the

try

statement.
The result will be an empty list if there are no
catch blocks.

**Returns:** the catch blocks

---

#### getCatches

List

<? extends

CatchTree

> getCatches()

Returns any catch blocks provided in the

try

statement.
The result will be an empty list if there are no
catch blocks.

getFinallyBlock

```java
BlockTree
getFinallyBlock()
```

Returns the finally block provided in the

try

statement,
or

null

if there is none.

**Returns:** the finally block

---

#### getFinallyBlock

BlockTree

getFinallyBlock()

Returns the finally block provided in the

try

statement,
or

null

if there is none.

getResources

```java
List
<? extends
Tree
> getResources()
```

Returns any resource declarations provided in the

try

statement.
The result will be an empty list if there are no
resource declarations.

**Returns:** the resource declarations

---

#### getResources

List

<? extends

Tree

> getResources()

Returns any resource declarations provided in the

try

statement.
The result will be an empty list if there are no
resource declarations.

---

