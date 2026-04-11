# Interface GotoTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\GotoTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
GotoTree

extends
StatementTree
```

A tree node for a statement that jumps to a target. Note that
ECMAScript does not support a goto statement. But, this Tree
type serves as a super interface for

BreakTree

and

ContinueTree

.

**All Superinterfaces:** StatementTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getLabel()

Label associated with this goto statement. This is null
if there is no label associated with this goto statement.

**Returns:**
- label associated with this goto statement.

---

### Additional Sections

#### Interface GotoTree

**All Superinterfaces:** StatementTree

,

Tree

**All Known Subinterfaces:** BreakTree

,

ContinueTree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
GotoTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a statement that jumps to a target. Note that
ECMAScript does not support a goto statement. But, this Tree
type serves as a super interface for

BreakTree

and

ContinueTree

.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

GotoTree

extends

StatementTree

A tree node for a statement that jumps to a target. Note that
ECMAScript does not support a goto statement. But, this Tree
type serves as a super interface for

BreakTree

and

ContinueTree

.

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

String

getLabel

()

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this goto statement.

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

String

getLabel

()

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this goto statement.

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

Label associated with this goto statement.

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

- getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this goto statement. This is null
if there is no label associated with this goto statement.

**Returns:** label associated with this goto statement.

Method Detail

- getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this goto statement. This is null
if there is no label associated with this goto statement.

**Returns:** label associated with this goto statement.

---

#### Method Detail

getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this goto statement. This is null
if there is no label associated with this goto statement.

**Returns:** label associated with this goto statement.

---

#### getLabel

String

getLabel()

Label associated with this goto statement. This is null
if there is no label associated with this goto statement.

---

