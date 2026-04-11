# Interface BreakTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\BreakTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
BreakTree

extends
GotoTree
```

A tree node for a 'break' statement.

For example:

```java
break;

break
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

Label associated with this break statement. This is null
if there is no label associated with this break statement.

**Specified by:**
- getLabel

in interface

GotoTree

**Returns:**
- label associated with this break statement.

---

### Additional Sections

#### Interface BreakTree

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
BreakTree

extends
GotoTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'break' statement.

For example:

```java
break;

break
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

BreakTree

extends

GotoTree

A tree node for a 'break' statement.

For example:

```java
break;

break
label
;
```

break;

break

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

Label associated with this break statement.

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

Label associated with this break statement.

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

Label associated with this break statement.

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

Label associated with this break statement. This is null
if there is no label associated with this break statement.

**Specified by:** getLabel

in interface

GotoTree
**Returns:** label associated with this break statement.

Method Detail

- getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this break statement. This is null
if there is no label associated with this break statement.

**Specified by:** getLabel

in interface

GotoTree
**Returns:** label associated with this break statement.

---

#### Method Detail

getLabel

```java
String
getLabel()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Label associated with this break statement. This is null
if there is no label associated with this break statement.

**Specified by:** getLabel

in interface

GotoTree
**Returns:** label associated with this break statement.

---

#### getLabel

String

getLabel()

Label associated with this break statement. This is null
if there is no label associated with this break statement.

---

