# Interface CompilationUnitTree

**Source:** `jdk.compiler\com\sun\source\tree\CompilationUnitTree.html`

### Class Description

```java
public interface
CompilationUnitTree

extends
Tree
```

Represents the abstract syntax tree for compilation units (source
files) and package declarations (package-info.java).

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
AnnotationTree
> getPackageAnnotations()

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:**
- the package annotations

---

#### ExpressionTree
getPackageName()

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:**
- the package name

---

#### PackageTree
getPackage()

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

**Returns:**
- the package tree

**Since:**
- 9

---

#### List
<? extends
ImportTree
> getImports()

Returns the import declarations appearing in this compilation unit.

**Returns:**
- the import declarations

---

#### List
<? extends
Tree
> getTypeDecls()

Returns the type declarations appearing in this compilation unit.
The list may also include empty statements resulting from
extraneous semicolons.

**Returns:**
- the type declarations

---

#### JavaFileObject
getSourceFile()

Returns the file object containing the source for this compilation unit.

**Returns:**
- the file object

---

#### LineMap
getLineMap()

Returns the line map for this compilation unit, if available.
Returns

null

if the line map is not available.

**Returns:**
- the line map for this compilation unit

---

### Additional Sections

#### Interface CompilationUnitTree

**All Superinterfaces:** Tree

```java
public interface
CompilationUnitTree

extends
Tree
```

Represents the abstract syntax tree for compilation units (source
files) and package declarations (package-info.java).

**Since:** 1.6
**See The Java™ Language Specification :** sections 7.3, and 7.4

public interface

CompilationUnitTree

extends

Tree

Represents the abstract syntax tree for compilation units (source
files) and package declarations (package-info.java).

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

List

<? extends

ImportTree

>

getImports

()

Returns the import declarations appearing in this compilation unit.

LineMap

getLineMap

()

Returns the line map for this compilation unit, if available.

PackageTree

getPackage

()

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

List

<? extends

AnnotationTree

>

getPackageAnnotations

()

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

ExpressionTree

getPackageName

()

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

JavaFileObject

getSourceFile

()

Returns the file object containing the source for this compilation unit.

List

<? extends

Tree

>

getTypeDecls

()

Returns the type declarations appearing in this compilation unit.

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

List

<? extends

ImportTree

>

getImports

()

Returns the import declarations appearing in this compilation unit.

LineMap

getLineMap

()

Returns the line map for this compilation unit, if available.

PackageTree

getPackage

()

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

List

<? extends

AnnotationTree

>

getPackageAnnotations

()

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

ExpressionTree

getPackageName

()

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

JavaFileObject

getSourceFile

()

Returns the file object containing the source for this compilation unit.

List

<? extends

Tree

>

getTypeDecls

()

Returns the type declarations appearing in this compilation unit.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the import declarations appearing in this compilation unit.

Returns the line map for this compilation unit, if available.

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

Returns the file object containing the source for this compilation unit.

Returns the type declarations appearing in this compilation unit.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getPackageAnnotations

```java
List
<? extends
AnnotationTree
> getPackageAnnotations()
```

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:** the package annotations

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:** the package name

- getPackage

```java
PackageTree
getPackage()
```

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

**Returns:** the package tree
**Since:** 9

- getImports

```java
List
<? extends
ImportTree
> getImports()
```

Returns the import declarations appearing in this compilation unit.

**Returns:** the import declarations

- getTypeDecls

```java
List
<? extends
Tree
> getTypeDecls()
```

Returns the type declarations appearing in this compilation unit.
The list may also include empty statements resulting from
extraneous semicolons.

**Returns:** the type declarations

- getSourceFile

```java
JavaFileObject
getSourceFile()
```

Returns the file object containing the source for this compilation unit.

**Returns:** the file object

- getLineMap

```java
LineMap
getLineMap()
```

Returns the line map for this compilation unit, if available.
Returns

null

if the line map is not available.

**Returns:** the line map for this compilation unit

Method Detail

- getPackageAnnotations

```java
List
<? extends
AnnotationTree
> getPackageAnnotations()
```

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:** the package annotations

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:** the package name

- getPackage

```java
PackageTree
getPackage()
```

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

**Returns:** the package tree
**Since:** 9

- getImports

```java
List
<? extends
ImportTree
> getImports()
```

Returns the import declarations appearing in this compilation unit.

**Returns:** the import declarations

- getTypeDecls

```java
List
<? extends
Tree
> getTypeDecls()
```

Returns the type declarations appearing in this compilation unit.
The list may also include empty statements resulting from
extraneous semicolons.

**Returns:** the type declarations

- getSourceFile

```java
JavaFileObject
getSourceFile()
```

Returns the file object containing the source for this compilation unit.

**Returns:** the file object

- getLineMap

```java
LineMap
getLineMap()
```

Returns the line map for this compilation unit, if available.
Returns

null

if the line map is not available.

**Returns:** the line map for this compilation unit

---

#### Method Detail

getPackageAnnotations

```java
List
<? extends
AnnotationTree
> getPackageAnnotations()
```

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:** the package annotations

---

#### getPackageAnnotations

List

<? extends

AnnotationTree

> getPackageAnnotations()

Returns the annotations listed on any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

**Returns:** the package name

---

#### getPackageName

ExpressionTree

getPackageName()

Returns the name contained in any package declaration
at the head of this compilation unit, or

null

if there
is no package declaration.

getPackage

```java
PackageTree
getPackage()
```

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

**Returns:** the package tree
**Since:** 9

---

#### getPackage

PackageTree

getPackage()

Returns the package tree associated with this compilation unit,
or

null

if there is no package declaration.

getImports

```java
List
<? extends
ImportTree
> getImports()
```

Returns the import declarations appearing in this compilation unit.

**Returns:** the import declarations

---

#### getImports

List

<? extends

ImportTree

> getImports()

Returns the import declarations appearing in this compilation unit.

getTypeDecls

```java
List
<? extends
Tree
> getTypeDecls()
```

Returns the type declarations appearing in this compilation unit.
The list may also include empty statements resulting from
extraneous semicolons.

**Returns:** the type declarations

---

#### getTypeDecls

List

<? extends

Tree

> getTypeDecls()

Returns the type declarations appearing in this compilation unit.
The list may also include empty statements resulting from
extraneous semicolons.

getSourceFile

```java
JavaFileObject
getSourceFile()
```

Returns the file object containing the source for this compilation unit.

**Returns:** the file object

---

#### getSourceFile

JavaFileObject

getSourceFile()

Returns the file object containing the source for this compilation unit.

getLineMap

```java
LineMap
getLineMap()
```

Returns the line map for this compilation unit, if available.
Returns

null

if the line map is not available.

**Returns:** the line map for this compilation unit

---

#### getLineMap

LineMap

getLineMap()

Returns the line map for this compilation unit, if available.
Returns

null

if the line map is not available.

---

