# Interface PackageTree

**Source:** `jdk.compiler\com\sun\source\tree\PackageTree.html`

### Class Description

```java
public interface
PackageTree

extends
Tree
```

Represents the package declaration.

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
> getAnnotations()

Returns the annotations associated with this package declaration.

**Returns:**
- the annotations

---

#### ExpressionTree
getPackageName()

Returns the name of the package being declared.

**Returns:**
- the name

---

### Additional Sections

#### Interface PackageTree

**All Superinterfaces:** Tree

```java
public interface
PackageTree

extends
Tree
```

Represents the package declaration.

**Since:** 9
**See The Java™ Language Specification :** sections 7.3, and 7.4

public interface

PackageTree

extends

Tree

Represents the package declaration.

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

AnnotationTree

>

getAnnotations

()

Returns the annotations associated with this package declaration.

ExpressionTree

getPackageName

()

Returns the name of the package being declared.

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

AnnotationTree

>

getAnnotations

()

Returns the annotations associated with this package declaration.

ExpressionTree

getPackageName

()

Returns the name of the package being declared.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the annotations associated with this package declaration.

Returns the name of the package being declared.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this package declaration.

**Returns:** the annotations

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package being declared.

**Returns:** the name

Method Detail

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this package declaration.

**Returns:** the annotations

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package being declared.

**Returns:** the name

---

#### Method Detail

getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this package declaration.

**Returns:** the annotations

---

#### getAnnotations

List

<? extends

AnnotationTree

> getAnnotations()

Returns the annotations associated with this package declaration.

getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package being declared.

**Returns:** the name

---

#### getPackageName

ExpressionTree

getPackageName()

Returns the name of the package being declared.

---

