# Interface ParameterizedTypeTree

**Source:** `jdk.compiler\com\sun\source\tree\ParameterizedTypeTree.html`

### Class Description

```java
public interface
ParameterizedTypeTree

extends
Tree
```

A tree node for a type expression involving type parameters.

For example:

```java
type
<
typeArguments
>
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Tree
getType()

Returns the base type.

**Returns:**
- the base type

---

#### List
<? extends
Tree
> getTypeArguments()

Returns the type arguments.

**Returns:**
- the type arguments

---

### Additional Sections

#### Interface ParameterizedTypeTree

**All Superinterfaces:** Tree

```java
public interface
ParameterizedTypeTree

extends
Tree
```

A tree node for a type expression involving type parameters.

For example:

```java
type
<
typeArguments
>
```

**Since:** 1.6
**See The Java™ Language Specification :** section 4.5.1

public interface

ParameterizedTypeTree

extends

Tree

A tree node for a type expression involving type parameters.

For example:

```java
type
<
typeArguments
>
```

type

<

typeArguments

>

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

getType

()

Returns the base type.

List

<? extends

Tree

>

getTypeArguments

()

Returns the type arguments.

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

getType

()

Returns the base type.

List

<? extends

Tree

>

getTypeArguments

()

Returns the type arguments.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the base type.

Returns the type arguments.

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

Returns the base type.

**Returns:** the base type

- getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments.

**Returns:** the type arguments

Method Detail

- getType

```java
Tree
getType()
```

Returns the base type.

**Returns:** the base type

- getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments.

**Returns:** the type arguments

---

#### Method Detail

getType

```java
Tree
getType()
```

Returns the base type.

**Returns:** the base type

---

#### getType

Tree

getType()

Returns the base type.

getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments.

**Returns:** the type arguments

---

#### getTypeArguments

List

<? extends

Tree

> getTypeArguments()

Returns the type arguments.

---

