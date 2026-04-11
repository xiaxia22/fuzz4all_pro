# Interface TypeParameterTree

**Source:** `jdk.compiler\com\sun\source\tree\TypeParameterTree.html`

### Class Description

```java
public interface
TypeParameterTree

extends
Tree
```

A tree node for a type parameter.

For example:

```java
name

name
extends
bounds

annotations

name
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Name
getName()

Returns the name of the type parameter.

**Returns:**
- the name

---

#### List
<? extends
Tree
> getBounds()

Returns the bounds of the type parameter.

**Returns:**
- the bounds

---

#### List
<? extends
AnnotationTree
> getAnnotations()

Returns annotations on the type parameter declaration.

Annotations need Target meta-annotations of

ElementType.TYPE_PARAMETER

or

ElementType.TYPE_USE

to appear in this position.

**Returns:**
- annotations on the type parameter declaration

**Since:**
- 1.8

---

### Additional Sections

#### Interface TypeParameterTree

**All Superinterfaces:** Tree

```java
public interface
TypeParameterTree

extends
Tree
```

A tree node for a type parameter.

For example:

```java
name

name
extends
bounds

annotations

name
```

**Since:** 1.6
**See The Java™ Language Specification :** section 4.4

public interface

TypeParameterTree

extends

Tree

A tree node for a type parameter.

For example:

```java
name

name
extends
bounds

annotations

name
```

name

name

extends

bounds

annotations

name

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

Returns annotations on the type parameter declaration.

List

<? extends

Tree

>

getBounds

()

Returns the bounds of the type parameter.

Name

getName

()

Returns the name of the type parameter.

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

Returns annotations on the type parameter declaration.

List

<? extends

Tree

>

getBounds

()

Returns the bounds of the type parameter.

Name

getName

()

Returns the name of the type parameter.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns annotations on the type parameter declaration.

Returns the bounds of the type parameter.

Returns the name of the type parameter.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
Name
getName()
```

Returns the name of the type parameter.

**Returns:** the name

- getBounds

```java
List
<? extends
Tree
> getBounds()
```

Returns the bounds of the type parameter.

**Returns:** the bounds

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns annotations on the type parameter declaration.

Annotations need Target meta-annotations of

ElementType.TYPE_PARAMETER

or

ElementType.TYPE_USE

to appear in this position.

**Returns:** annotations on the type parameter declaration
**Since:** 1.8

Method Detail

- getName

```java
Name
getName()
```

Returns the name of the type parameter.

**Returns:** the name

- getBounds

```java
List
<? extends
Tree
> getBounds()
```

Returns the bounds of the type parameter.

**Returns:** the bounds

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns annotations on the type parameter declaration.

Annotations need Target meta-annotations of

ElementType.TYPE_PARAMETER

or

ElementType.TYPE_USE

to appear in this position.

**Returns:** annotations on the type parameter declaration
**Since:** 1.8

---

#### Method Detail

getName

```java
Name
getName()
```

Returns the name of the type parameter.

**Returns:** the name

---

#### getName

Name

getName()

Returns the name of the type parameter.

getBounds

```java
List
<? extends
Tree
> getBounds()
```

Returns the bounds of the type parameter.

**Returns:** the bounds

---

#### getBounds

List

<? extends

Tree

> getBounds()

Returns the bounds of the type parameter.

getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns annotations on the type parameter declaration.

Annotations need Target meta-annotations of

ElementType.TYPE_PARAMETER

or

ElementType.TYPE_USE

to appear in this position.

**Returns:** annotations on the type parameter declaration
**Since:** 1.8

---

#### getAnnotations

List

<? extends

AnnotationTree

> getAnnotations()

Returns annotations on the type parameter declaration.

Annotations need Target meta-annotations of

ElementType.TYPE_PARAMETER

or

ElementType.TYPE_USE

to appear in this position.

---

