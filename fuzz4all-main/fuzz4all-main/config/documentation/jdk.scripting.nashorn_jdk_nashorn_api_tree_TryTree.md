# Interface TryTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\TryTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
TryTree

extends
StatementTree
```

A tree node for a 'try' statement.

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

Returns the 'try' block of this 'try' statement.

**Returns:**
- the 'try' block

---

#### List
<? extends
CatchTree
> getCatches()

Returns the list of 'catch' statements associated with this 'try'.

**Returns:**
- the list of 'catch' statements associated with this 'try'.

---

#### BlockTree
getFinallyBlock()

Returns the 'finally' block associated with this 'try'. This is
null if there is no 'finally' block associated with this 'try'.

**Returns:**
- the 'finally' block associated with this 'try'.

---

### Additional Sections

#### Interface TryTree

**All Superinterfaces:** StatementTree

,

Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
TryTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'try' statement.

For example:

```java
try

block

catches

finally

finallyBlock
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

TryTree

extends

StatementTree

A tree node for a 'try' statement.

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

Returns the 'try' block of this 'try' statement.

List

<? extends

CatchTree

>

getCatches

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'catch' statements associated with this 'try'.

BlockTree

getFinallyBlock

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'finally' block associated with this 'try'.

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

Returns the 'try' block of this 'try' statement.

List

<? extends

CatchTree

>

getCatches

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'catch' statements associated with this 'try'.

BlockTree

getFinallyBlock

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'finally' block associated with this 'try'.

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

Returns the 'try' block of this 'try' statement.

Returns the list of 'catch' statements associated with this 'try'.

Returns the 'finally' block associated with this 'try'.

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

- getBlock

```java
BlockTree
getBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'try' block of this 'try' statement.

**Returns:** the 'try' block

- getCatches

```java
List
<? extends
CatchTree
> getCatches()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'catch' statements associated with this 'try'.

**Returns:** the list of 'catch' statements associated with this 'try'.

- getFinallyBlock

```java
BlockTree
getFinallyBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'finally' block associated with this 'try'. This is
null if there is no 'finally' block associated with this 'try'.

**Returns:** the 'finally' block associated with this 'try'.

Method Detail

- getBlock

```java
BlockTree
getBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'try' block of this 'try' statement.

**Returns:** the 'try' block

- getCatches

```java
List
<? extends
CatchTree
> getCatches()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'catch' statements associated with this 'try'.

**Returns:** the list of 'catch' statements associated with this 'try'.

- getFinallyBlock

```java
BlockTree
getFinallyBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'finally' block associated with this 'try'. This is
null if there is no 'finally' block associated with this 'try'.

**Returns:** the 'finally' block associated with this 'try'.

---

#### Method Detail

getBlock

```java
BlockTree
getBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'try' block of this 'try' statement.

**Returns:** the 'try' block

---

#### getBlock

BlockTree

getBlock()

Returns the 'try' block of this 'try' statement.

getCatches

```java
List
<? extends
CatchTree
> getCatches()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'catch' statements associated with this 'try'.

**Returns:** the list of 'catch' statements associated with this 'try'.

---

#### getCatches

List

<? extends

CatchTree

> getCatches()

Returns the list of 'catch' statements associated with this 'try'.

getFinallyBlock

```java
BlockTree
getFinallyBlock()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the 'finally' block associated with this 'try'. This is
null if there is no 'finally' block associated with this 'try'.

**Returns:** the 'finally' block associated with this 'try'.

---

#### getFinallyBlock

BlockTree

getFinallyBlock()

Returns the 'finally' block associated with this 'try'. This is
null if there is no 'finally' block associated with this 'try'.

---

