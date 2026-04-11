# Interface ContinueTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ContinueTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ContinueTree

extends
GotoTree
```

A tree node for a 'continue' statement.

For example:

```java
continue;
continue
label
;
```

**All Superinterfaces:** GotoTree

,

StatementTree

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

Label associated with this continue statement. This is null
if there is no label associated with this continue statement.

**Specified by:**
- getLabel

in interface

GotoTree

**Returns:**
- label associated with this continue statement.

---

### Additional Sections

#### Interface ContinueTree

**All Superinterfaces:** GotoTree

,

StatementTree

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
ContinueTree

extends
GotoTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'continue' statement.

For example:

```java
continue;
continue
label
;
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ContinueTree

extends

GotoTree

A tree node for a 'continue' statement.

For example:

```java
continue;
continue
label
;
```

continue;
continue

label

;

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

Label associated with this continue statement.

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

Label associated with this continue statement.

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

Label associated with this continue statement.

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

Label associated with this continue statement. This is null
if there is no label associated with this continue statement.

**Specified by:** getLabel

in interface

GotoTree
**Returns:** label associated with this continue statement.

Method Detail

- getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this continue statement. This is null
if there is no label associated with this continue statement.

**Specified by:** getLabel

in interface

GotoTree
**Returns:** label associated with this continue statement.

---

#### Method Detail

getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this continue statement. This is null
if there is no label associated with this continue statement.

**Specified by:** getLabel

in interface

GotoTree
**Returns:** label associated with this continue statement.

---

#### getLabel

String

getLabel()

Label associated with this continue statement. This is null
if there is no label associated with this continue statement.

---

