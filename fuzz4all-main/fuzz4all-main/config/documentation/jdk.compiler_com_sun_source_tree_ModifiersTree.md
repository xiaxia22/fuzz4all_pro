# Interface ModifiersTree

**Source:** `jdk.compiler\com\sun\source\tree\ModifiersTree.html`

### Class Description

```java
public interface
ModifiersTree

extends
Tree
```

A tree node for the modifiers, including annotations, for a declaration.

For example:

```java
flags

flags

annotations
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Set
<
Modifier
> getFlags()

Returns the flags in this modifiers tree.

**Returns:**
- the flags

---

#### List
<? extends
AnnotationTree
> getAnnotations()

Returns the annotations in this modifiers tree.

**Returns:**
- the annotations

---

### Additional Sections

#### Interface ModifiersTree

**All Superinterfaces:** Tree

```java
public interface
ModifiersTree

extends
Tree
```

A tree node for the modifiers, including annotations, for a declaration.

For example:

```java
flags

flags

annotations
```

**Since:** 1.6
**See The Java™ Language Specification :** sections 8.1.1, 8.3.1, 8.4.3, 8.5.1, 8.8.3, 9.1.1, and 9.7

public interface

ModifiersTree

extends

Tree

A tree node for the modifiers, including annotations, for a declaration.

For example:

```java
flags

flags

annotations
```

flags

flags

annotations

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

Returns the annotations in this modifiers tree.

Set

<

Modifier

>

getFlags

()

Returns the flags in this modifiers tree.

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

Returns the annotations in this modifiers tree.

Set

<

Modifier

>

getFlags

()

Returns the flags in this modifiers tree.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the annotations in this modifiers tree.

Returns the flags in this modifiers tree.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getFlags

```java
Set
<
Modifier
> getFlags()
```

Returns the flags in this modifiers tree.

**Returns:** the flags

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations in this modifiers tree.

**Returns:** the annotations

Method Detail

- getFlags

```java
Set
<
Modifier
> getFlags()
```

Returns the flags in this modifiers tree.

**Returns:** the flags

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations in this modifiers tree.

**Returns:** the annotations

---

#### Method Detail

getFlags

```java
Set
<
Modifier
> getFlags()
```

Returns the flags in this modifiers tree.

**Returns:** the flags

---

#### getFlags

Set

<

Modifier

> getFlags()

Returns the flags in this modifiers tree.

getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations in this modifiers tree.

**Returns:** the annotations

---

#### getAnnotations

List

<? extends

AnnotationTree

> getAnnotations()

Returns the annotations in this modifiers tree.

---

