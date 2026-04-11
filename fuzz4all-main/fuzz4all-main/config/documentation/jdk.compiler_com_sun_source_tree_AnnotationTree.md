# Interface AnnotationTree

**Source:** `jdk.compiler\com\sun\source\tree\AnnotationTree.html`

### Class Description

```java
public interface
AnnotationTree

extends
ExpressionTree
```

A tree node for an annotation.

For example:

```java
@
annotationType

@
annotationType
(
arguments
)
```

**All Superinterfaces:** ExpressionTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Tree
getAnnotationType()

Returns the annotation type.

**Returns:**
- the annotation type

---

#### List
<? extends
ExpressionTree
> getArguments()

Returns the arguments, if any, for the annotation.

**Returns:**
- the arguments for the annotation type

---

### Additional Sections

#### Interface AnnotationTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
AnnotationTree

extends
ExpressionTree
```

A tree node for an annotation.

For example:

```java
@
annotationType

@
annotationType
(
arguments
)
```

**Since:** 1.6
**See The Java™ Language Specification :** section 9.7

public interface

AnnotationTree

extends

ExpressionTree

A tree node for an annotation.

For example:

```java
@
annotationType

@
annotationType
(
arguments
)
```

@

annotationType

@

annotationType

(

arguments

)

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

Tree

getAnnotationType

()

Returns the annotation type.

List

<? extends

ExpressionTree

>

getArguments

()

Returns the arguments, if any, for the annotation.

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

Tree

getAnnotationType

()

Returns the annotation type.

List

<? extends

ExpressionTree

>

getArguments

()

Returns the arguments, if any, for the annotation.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the annotation type.

Returns the arguments, if any, for the annotation.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getAnnotationType

```java
Tree
getAnnotationType()
```

Returns the annotation type.

**Returns:** the annotation type

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments, if any, for the annotation.

**Returns:** the arguments for the annotation type

Method Detail

- getAnnotationType

```java
Tree
getAnnotationType()
```

Returns the annotation type.

**Returns:** the annotation type

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments, if any, for the annotation.

**Returns:** the arguments for the annotation type

---

#### Method Detail

getAnnotationType

```java
Tree
getAnnotationType()
```

Returns the annotation type.

**Returns:** the annotation type

---

#### getAnnotationType

Tree

getAnnotationType()

Returns the annotation type.

getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments, if any, for the annotation.

**Returns:** the arguments for the annotation type

---

#### getArguments

List

<? extends

ExpressionTree

> getArguments()

Returns the arguments, if any, for the annotation.

---

