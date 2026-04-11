# Interface ModuleTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ModuleTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ModuleTree

extends
Tree
```

A Tree node for

Module information

.

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
ImportEntryTree
> getImportEntries()

Returns the list of import entries.

**Returns:**
- the import entries

---

#### List
<? extends
ExportEntryTree
> getLocalExportEntries()

Returns the list of local export entries.

**Returns:**
- the local export entries

---

#### List
<? extends
ExportEntryTree
> getIndirectExportEntries()

Returns the list of indirect export entries.

**Returns:**
- the indirect export entries

---

#### List
<? extends
ExportEntryTree
> getStarExportEntries()

Returns the list of star export entries.

**Returns:**
- the star export entries

---

### Additional Sections

#### Interface ModuleTree

**All Superinterfaces:** Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ModuleTree

extends
Tree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A Tree node for

Module information

.

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ModuleTree

extends

Tree

A Tree node for

Module information

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

List

<? extends

ImportEntryTree

>

getImportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of import entries.

List

<? extends

ExportEntryTree

>

getIndirectExportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of indirect export entries.

List

<? extends

ExportEntryTree

>

getLocalExportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of local export entries.

List

<? extends

ExportEntryTree

>

getStarExportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of star export entries.

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

List

<? extends

ImportEntryTree

>

getImportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of import entries.

List

<? extends

ExportEntryTree

>

getIndirectExportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of indirect export entries.

List

<? extends

ExportEntryTree

>

getLocalExportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of local export entries.

List

<? extends

ExportEntryTree

>

getStarExportEntries

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of star export entries.

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

Returns the list of import entries.

Returns the list of indirect export entries.

Returns the list of local export entries.

Returns the list of star export entries.

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

- getImportEntries

```java
List
<? extends
ImportEntryTree
> getImportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of import entries.

**Returns:** the import entries

- getLocalExportEntries

```java
List
<? extends
ExportEntryTree
> getLocalExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of local export entries.

**Returns:** the local export entries

- getIndirectExportEntries

```java
List
<? extends
ExportEntryTree
> getIndirectExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of indirect export entries.

**Returns:** the indirect export entries

- getStarExportEntries

```java
List
<? extends
ExportEntryTree
> getStarExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of star export entries.

**Returns:** the star export entries

Method Detail

- getImportEntries

```java
List
<? extends
ImportEntryTree
> getImportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of import entries.

**Returns:** the import entries

- getLocalExportEntries

```java
List
<? extends
ExportEntryTree
> getLocalExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of local export entries.

**Returns:** the local export entries

- getIndirectExportEntries

```java
List
<? extends
ExportEntryTree
> getIndirectExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of indirect export entries.

**Returns:** the indirect export entries

- getStarExportEntries

```java
List
<? extends
ExportEntryTree
> getStarExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of star export entries.

**Returns:** the star export entries

---

#### Method Detail

getImportEntries

```java
List
<? extends
ImportEntryTree
> getImportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of import entries.

**Returns:** the import entries

---

#### getImportEntries

List

<? extends

ImportEntryTree

> getImportEntries()

Returns the list of import entries.

getLocalExportEntries

```java
List
<? extends
ExportEntryTree
> getLocalExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of local export entries.

**Returns:** the local export entries

---

#### getLocalExportEntries

List

<? extends

ExportEntryTree

> getLocalExportEntries()

Returns the list of local export entries.

getIndirectExportEntries

```java
List
<? extends
ExportEntryTree
> getIndirectExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of indirect export entries.

**Returns:** the indirect export entries

---

#### getIndirectExportEntries

List

<? extends

ExportEntryTree

> getIndirectExportEntries()

Returns the list of indirect export entries.

getStarExportEntries

```java
List
<? extends
ExportEntryTree
> getStarExportEntries()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of star export entries.

**Returns:** the star export entries

---

#### getStarExportEntries

List

<? extends

ExportEntryTree

> getStarExportEntries()

Returns the list of star export entries.

---

