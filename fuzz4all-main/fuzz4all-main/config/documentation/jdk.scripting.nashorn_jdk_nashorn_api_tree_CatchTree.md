# Interface CatchTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\CatchTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CatchTree

extends
Tree
```

A tree node for a 'catch' block in a 'try' statement.

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

#### ExpressionTree
getParameter()

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

**Returns:**
- the catch parameter identifier or parameter binding pattern

---

#### BlockTree
getBlock()

Returns the code block of this catch block.

**Returns:**
- the code block

---

#### ExpressionTree
getCondition()

Returns the optional catch condition expression. This is null
if this is an unconditional catch statement.

**Returns:**
- the optional catch condition expression.

---

### Additional Sections

#### Interface CatchTree

**All Superinterfaces:** Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CatchTree

extends
Tree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'catch' block in a 'try' statement.

For example:

```java
catch (
parameter
)

block
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

CatchTree

extends

Tree

A tree node for a 'catch' block in a 'try' statement.

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

- Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

BlockTree

getBlock

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the code block of this catch block.

ExpressionTree

getCondition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the optional catch condition expression.

ExpressionTree

getParameter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

- Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

Nested Class Summary

- Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface jdk.nashorn.api.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

BlockTree

getBlock

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the code block of this catch block.

ExpressionTree

getCondition

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the optional catch condition expression.

ExpressionTree

getParameter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

- Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the code block of this catch block.

Returns the optional catch condition expression.

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

---

#### Methods declared in interface jdk.nashorn.api.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getParameter

```java
ExpressionTree
getParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

**Returns:** the catch parameter identifier or parameter binding pattern

- getBlock

```java
BlockTree
getBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the code block of this catch block.

**Returns:** the code block

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the optional catch condition expression. This is null
if this is an unconditional catch statement.

**Returns:** the optional catch condition expression.

Method Detail

- getParameter

```java
ExpressionTree
getParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

**Returns:** the catch parameter identifier or parameter binding pattern

- getBlock

```java
BlockTree
getBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the code block of this catch block.

**Returns:** the code block

- getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the optional catch condition expression. This is null
if this is an unconditional catch statement.

**Returns:** the optional catch condition expression.

---

#### Method Detail

getParameter

```java
ExpressionTree
getParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

**Returns:** the catch parameter identifier or parameter binding pattern

---

#### getParameter

ExpressionTree

getParameter()

Returns the catch parameter identifier or parameter binding pattern of the exception caught.

getBlock

```java
BlockTree
getBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the code block of this catch block.

**Returns:** the code block

---

#### getBlock

BlockTree

getBlock()

Returns the code block of this catch block.

getCondition

```java
ExpressionTree
getCondition()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the optional catch condition expression. This is null
if this is an unconditional catch statement.

**Returns:** the optional catch condition expression.

---

#### getCondition

ExpressionTree

getCondition()

Returns the optional catch condition expression. This is null
if this is an unconditional catch statement.

---

