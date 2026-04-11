# Interface NewArrayTree

**Source:** `jdk.compiler\com\sun\source\tree\NewArrayTree.html`

### Class Description

```java
public interface
NewArrayTree

extends
ExpressionTree
```

A tree node for an expression to create a new instance of an array.

For example:

```java
new
type

dimensions

initializers

new
type

dimensions
[ ]
initializers
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
getType()

Returns the base type of the expression.
May be

null

for an array initializer expression.

**Returns:**
- the base type

---

#### List
<? extends
ExpressionTree
> getDimensions()

Returns the dimension expressions for the type.

**Returns:**
- the dimension expressions

---

#### List
<? extends
ExpressionTree
> getInitializers()

Returns the initializer expressions.

**Returns:**
- the initializer expressions

---

#### List
<? extends
AnnotationTree
> getAnnotations()

Returns the annotations on the base type.

**Returns:**
- the annotations

---

#### List
<? extends
List
<? extends
AnnotationTree
>> getDimAnnotations()

Returns the annotations on each of the dimension
expressions.

**Returns:**
- the annotations on the dimensions expressions

---

### Additional Sections

#### Interface NewArrayTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
NewArrayTree

extends
ExpressionTree
```

A tree node for an expression to create a new instance of an array.

For example:

```java
new
type

dimensions

initializers

new
type

dimensions
[ ]
initializers
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.10

public interface

NewArrayTree

extends

ExpressionTree

A tree node for an expression to create a new instance of an array.

For example:

```java
new
type

dimensions

initializers

new
type

dimensions
[ ]
initializers
```

new

type

dimensions

initializers

new

type

dimensions

[ ]

initializers

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

Returns the annotations on the base type.

List

<? extends

List

<? extends

AnnotationTree

>>

getDimAnnotations

()

Returns the annotations on each of the dimension
expressions.

List

<? extends

ExpressionTree

>

getDimensions

()

Returns the dimension expressions for the type.

List

<? extends

ExpressionTree

>

getInitializers

()

Returns the initializer expressions.

Tree

getType

()

Returns the base type of the expression.

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

Returns the annotations on the base type.

List

<? extends

List

<? extends

AnnotationTree

>>

getDimAnnotations

()

Returns the annotations on each of the dimension
expressions.

List

<? extends

ExpressionTree

>

getDimensions

()

Returns the dimension expressions for the type.

List

<? extends

ExpressionTree

>

getInitializers

()

Returns the initializer expressions.

Tree

getType

()

Returns the base type of the expression.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the annotations on the base type.

Returns the annotations on each of the dimension
expressions.

Returns the dimension expressions for the type.

Returns the initializer expressions.

Returns the base type of the expression.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
Tree
getType()
```

Returns the base type of the expression.
May be

null

for an array initializer expression.

**Returns:** the base type

- getDimensions

```java
List
<? extends
ExpressionTree
> getDimensions()
```

Returns the dimension expressions for the type.

**Returns:** the dimension expressions

- getInitializers

```java
List
<? extends
ExpressionTree
> getInitializers()
```

Returns the initializer expressions.

**Returns:** the initializer expressions

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations on the base type.

**Returns:** the annotations

- getDimAnnotations

```java
List
<? extends
List
<? extends
AnnotationTree
>> getDimAnnotations()
```

Returns the annotations on each of the dimension
expressions.

**Returns:** the annotations on the dimensions expressions

Method Detail

- getType

```java
Tree
getType()
```

Returns the base type of the expression.
May be

null

for an array initializer expression.

**Returns:** the base type

- getDimensions

```java
List
<? extends
ExpressionTree
> getDimensions()
```

Returns the dimension expressions for the type.

**Returns:** the dimension expressions

- getInitializers

```java
List
<? extends
ExpressionTree
> getInitializers()
```

Returns the initializer expressions.

**Returns:** the initializer expressions

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations on the base type.

**Returns:** the annotations

- getDimAnnotations

```java
List
<? extends
List
<? extends
AnnotationTree
>> getDimAnnotations()
```

Returns the annotations on each of the dimension
expressions.

**Returns:** the annotations on the dimensions expressions

---

#### Method Detail

getType

```java
Tree
getType()
```

Returns the base type of the expression.
May be

null

for an array initializer expression.

**Returns:** the base type

---

#### getType

Tree

getType()

Returns the base type of the expression.
May be

null

for an array initializer expression.

getDimensions

```java
List
<? extends
ExpressionTree
> getDimensions()
```

Returns the dimension expressions for the type.

**Returns:** the dimension expressions

---

#### getDimensions

List

<? extends

ExpressionTree

> getDimensions()

Returns the dimension expressions for the type.

getInitializers

```java
List
<? extends
ExpressionTree
> getInitializers()
```

Returns the initializer expressions.

**Returns:** the initializer expressions

---

#### getInitializers

List

<? extends

ExpressionTree

> getInitializers()

Returns the initializer expressions.

getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations on the base type.

**Returns:** the annotations

---

#### getAnnotations

List

<? extends

AnnotationTree

> getAnnotations()

Returns the annotations on the base type.

getDimAnnotations

```java
List
<? extends
List
<? extends
AnnotationTree
>> getDimAnnotations()
```

Returns the annotations on each of the dimension
expressions.

**Returns:** the annotations on the dimensions expressions

---

#### getDimAnnotations

List

<? extends

List

<? extends

AnnotationTree

>> getDimAnnotations()

Returns the annotations on each of the dimension
expressions.

---

