# Interface LabeledStatementTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\LabeledStatementTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
LabeledStatementTree

extends
StatementTree
```

A tree node for a labeled statement.

For example:

```java
label
:
statement
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

#### String
getLabel()

Returns the label associated with this statement.

**Returns:**
- the label

---

#### StatementTree
getStatement()

Returns the statement being labeled.

**Returns:**
- the statement labeled

---

### Additional Sections

#### Interface LabeledStatementTree

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
LabeledStatementTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a labeled statement.

For example:

```java
label
:
statement
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

LabeledStatementTree

extends

StatementTree

A tree node for a labeled statement.

For example:

```java
label
:
statement
```

label

:

statement

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

Returns the label associated with this statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement being labeled.

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

Returns the label associated with this statement.

StatementTree

getStatement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement being labeled.

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

Returns the label associated with this statement.

Returns the statement being labeled.

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

Returns the label associated with this statement.

**Returns:** the label

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement being labeled.

**Returns:** the statement labeled

Method Detail

- getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the label associated with this statement.

**Returns:** the label

- getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement being labeled.

**Returns:** the statement labeled

---

#### Method Detail

getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the label associated with this statement.

**Returns:** the label

---

#### getLabel

String

getLabel()

Returns the label associated with this statement.

getStatement

```java
StatementTree
getStatement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the statement being labeled.

**Returns:** the statement labeled

---

#### getStatement

StatementTree

getStatement()

Returns the statement being labeled.

---

