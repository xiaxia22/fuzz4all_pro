# Interface CompilationUnitTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\CompilationUnitTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CompilationUnitTree

extends
Tree
```

Represents the abstract syntax tree for compilation units (source
files)

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
Tree
> getSourceElements()

Return the list of source elements in this compilation unit.

**Returns:**
- the list of source elements in this compilation unit

---

#### String
getSourceName()

Return the source name of this script compilation unit.

**Returns:**
- the source name of this script compilation unit

---

#### boolean isStrict()

Returns if this is a ECMAScript "strict" compilation unit or not.

**Returns:**
- true if this compilation unit is declared "strict"

---

#### LineMap
getLineMap()

Returns the line map for this compilation unit, if available.
Returns null if the line map is not available.

**Returns:**
- the line map for this compilation unit

---

#### ModuleTree
getModule()

Return the

ModuleTree

associated with this compilation unit. This is null,
if there is no module information from this compilation unit.

**Returns:**
- the Module info or null

---

### Additional Sections

#### Interface CompilationUnitTree

**All Superinterfaces:** Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CompilationUnitTree

extends
Tree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Represents the abstract syntax tree for compilation units (source
files)

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

CompilationUnitTree

extends

Tree

Represents the abstract syntax tree for compilation units (source
files)

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

LineMap

getLineMap

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the line map for this compilation unit, if available.

ModuleTree

getModule

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

ModuleTree

associated with this compilation unit.

List

<? extends

Tree

>

getSourceElements

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of source elements in this compilation unit.

String

getSourceName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source name of this script compilation unit.

boolean

isStrict

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a ECMAScript "strict" compilation unit or not.

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

LineMap

getLineMap

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the line map for this compilation unit, if available.

ModuleTree

getModule

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

ModuleTree

associated with this compilation unit.

List

<? extends

Tree

>

getSourceElements

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of source elements in this compilation unit.

String

getSourceName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source name of this script compilation unit.

boolean

isStrict

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a ECMAScript "strict" compilation unit or not.

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

Returns the line map for this compilation unit, if available.

Return the

ModuleTree

associated with this compilation unit.

Return the list of source elements in this compilation unit.

Return the source name of this script compilation unit.

Returns if this is a ECMAScript "strict" compilation unit or not.

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

- getSourceElements

```java
List
<? extends
Tree
> getSourceElements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of source elements in this compilation unit.

**Returns:** the list of source elements in this compilation unit

- getSourceName

```java
String
getSourceName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source name of this script compilation unit.

**Returns:** the source name of this script compilation unit

- isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a ECMAScript "strict" compilation unit or not.

**Returns:** true if this compilation unit is declared "strict"

- getLineMap

```java
LineMap
getLineMap()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the line map for this compilation unit, if available.
Returns null if the line map is not available.

**Returns:** the line map for this compilation unit

- getModule

```java
ModuleTree
getModule()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

ModuleTree

associated with this compilation unit. This is null,
if there is no module information from this compilation unit.

**Returns:** the Module info or null

Method Detail

- getSourceElements

```java
List
<? extends
Tree
> getSourceElements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of source elements in this compilation unit.

**Returns:** the list of source elements in this compilation unit

- getSourceName

```java
String
getSourceName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source name of this script compilation unit.

**Returns:** the source name of this script compilation unit

- isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a ECMAScript "strict" compilation unit or not.

**Returns:** true if this compilation unit is declared "strict"

- getLineMap

```java
LineMap
getLineMap()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the line map for this compilation unit, if available.
Returns null if the line map is not available.

**Returns:** the line map for this compilation unit

- getModule

```java
ModuleTree
getModule()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

ModuleTree

associated with this compilation unit. This is null,
if there is no module information from this compilation unit.

**Returns:** the Module info or null

---

#### Method Detail

getSourceElements

```java
List
<? extends
Tree
> getSourceElements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of source elements in this compilation unit.

**Returns:** the list of source elements in this compilation unit

---

#### getSourceElements

List

<? extends

Tree

> getSourceElements()

Return the list of source elements in this compilation unit.

getSourceName

```java
String
getSourceName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source name of this script compilation unit.

**Returns:** the source name of this script compilation unit

---

#### getSourceName

String

getSourceName()

Return the source name of this script compilation unit.

isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns if this is a ECMAScript "strict" compilation unit or not.

**Returns:** true if this compilation unit is declared "strict"

---

#### isStrict

boolean isStrict()

Returns if this is a ECMAScript "strict" compilation unit or not.

getLineMap

```java
LineMap
getLineMap()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the line map for this compilation unit, if available.
Returns null if the line map is not available.

**Returns:** the line map for this compilation unit

---

#### getLineMap

LineMap

getLineMap()

Returns the line map for this compilation unit, if available.
Returns null if the line map is not available.

getModule

```java
ModuleTree
getModule()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the

ModuleTree

associated with this compilation unit. This is null,
if there is no module information from this compilation unit.

**Returns:** the Module info or null

---

#### getModule

ModuleTree

getModule()

Return the

ModuleTree

associated with this compilation unit. This is null,
if there is no module information from this compilation unit.

---

