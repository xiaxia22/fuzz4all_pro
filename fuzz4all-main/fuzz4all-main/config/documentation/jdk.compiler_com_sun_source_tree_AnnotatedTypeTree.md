# Interface AnnotatedTypeTree

**Source:** `jdk.compiler\com\sun\source\tree\AnnotatedTypeTree.html`

### Class Description

```java
public interface
AnnotatedTypeTree

extends
ExpressionTree
```

A tree node for an annotated type.

For example:

```java
@
annotationType String

@
annotationType
(
arguments
)
Date
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

#### List
<? extends
AnnotationTree
> getAnnotations()

Returns the annotations associated with this type expression.

**Returns:**
- the annotations

---

#### ExpressionTree
getUnderlyingType()

Returns the underlying type with which the annotations are associated.

**Returns:**
- the underlying type

---

### Additional Sections

#### Interface AnnotatedTypeTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
AnnotatedTypeTree

extends
ExpressionTree
```

A tree node for an annotated type.

For example:

```java
@
annotationType String

@
annotationType
(
arguments
)
Date
```

**Since:** 1.8
**See Also:** "JSR 308: Annotations on Java Types"

public interface

AnnotatedTypeTree

extends

ExpressionTree

A tree node for an annotated type.

For example:

```java
@
annotationType String

@
annotationType
(
arguments
)
Date
```

@

annotationType String

@

annotationType

(

arguments

)

Date

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

Returns the annotations associated with this type expression.

ExpressionTree

getUnderlyingType

()

Returns the underlying type with which the annotations are associated.

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

Returns the annotations associated with this type expression.

ExpressionTree

getUnderlyingType

()

Returns the underlying type with which the annotations are associated.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the annotations associated with this type expression.

Returns the underlying type with which the annotations are associated.

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

Returns the annotations associated with this type expression.

**Returns:** the annotations

- getUnderlyingType

```java
ExpressionTree
getUnderlyingType()
```

Returns the underlying type with which the annotations are associated.

**Returns:** the underlying type

Method Detail

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this type expression.

**Returns:** the annotations

- getUnderlyingType

```java
ExpressionTree
getUnderlyingType()
```

Returns the underlying type with which the annotations are associated.

**Returns:** the underlying type

---

#### Method Detail

getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this type expression.

**Returns:** the annotations

---

#### getAnnotations

List

<? extends

AnnotationTree

> getAnnotations()

Returns the annotations associated with this type expression.

getUnderlyingType

```java
ExpressionTree
getUnderlyingType()
```

Returns the underlying type with which the annotations are associated.

**Returns:** the underlying type

---

#### getUnderlyingType

ExpressionTree

getUnderlyingType()

Returns the underlying type with which the annotations are associated.

---

