# Interface ModuleTree

**Source:** `jdk.compiler\com\sun\source\tree\ModuleTree.html`

### Class Description

```java
public interface
ModuleTree

extends
Tree
```

A tree node for a module declaration.

For example:

```java
annotations

[open] module
module-name
{

directives

}
```

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

Returns the annotations associated with this module declaration.

**Returns:**
- the annotations

---

#### ModuleTree.ModuleKind
getModuleType()

Returns the type of this module.

**Returns:**
- the type of this module

---

#### ExpressionTree
getName()

Returns the name of the module.

**Returns:**
- the name of the module

---

#### List
<? extends
DirectiveTree
> getDirectives()

Returns the directives in the module declaration.

**Returns:**
- the directives in the module declaration

---

### Additional Sections

#### Interface ModuleTree

**All Superinterfaces:** Tree

```java
public interface
ModuleTree

extends
Tree
```

A tree node for a module declaration.

For example:

```java
annotations

[open] module
module-name
{

directives

}
```

**Since:** 9

public interface

ModuleTree

extends

Tree

A tree node for a module declaration.

For example:

```java
annotations

[open] module
module-name
{

directives

}
```

annotations

[open] module

module-name

{

directives

}

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ModuleTree.ModuleKind

The kind of the module.

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

Returns the annotations associated with this module declaration.

List

<? extends

DirectiveTree

>

getDirectives

()

Returns the directives in the module declaration.

ModuleTree.ModuleKind

getModuleType

()

Returns the type of this module.

ExpressionTree

getName

()

Returns the name of the module.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

ModuleTree.ModuleKind

The kind of the module.

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

The kind of the module.

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

Returns the annotations associated with this module declaration.

List

<? extends

DirectiveTree

>

getDirectives

()

Returns the directives in the module declaration.

ModuleTree.ModuleKind

getModuleType

()

Returns the type of this module.

ExpressionTree

getName

()

Returns the name of the module.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the annotations associated with this module declaration.

Returns the directives in the module declaration.

Returns the type of this module.

Returns the name of the module.

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

Returns the annotations associated with this module declaration.

**Returns:** the annotations

- getModuleType

```java
ModuleTree.ModuleKind
getModuleType()
```

Returns the type of this module.

**Returns:** the type of this module

- getName

```java
ExpressionTree
getName()
```

Returns the name of the module.

**Returns:** the name of the module

- getDirectives

```java
List
<? extends
DirectiveTree
> getDirectives()
```

Returns the directives in the module declaration.

**Returns:** the directives in the module declaration

Method Detail

- getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this module declaration.

**Returns:** the annotations

- getModuleType

```java
ModuleTree.ModuleKind
getModuleType()
```

Returns the type of this module.

**Returns:** the type of this module

- getName

```java
ExpressionTree
getName()
```

Returns the name of the module.

**Returns:** the name of the module

- getDirectives

```java
List
<? extends
DirectiveTree
> getDirectives()
```

Returns the directives in the module declaration.

**Returns:** the directives in the module declaration

---

#### Method Detail

getAnnotations

```java
List
<? extends
AnnotationTree
> getAnnotations()
```

Returns the annotations associated with this module declaration.

**Returns:** the annotations

---

#### getAnnotations

List

<? extends

AnnotationTree

> getAnnotations()

Returns the annotations associated with this module declaration.

getModuleType

```java
ModuleTree.ModuleKind
getModuleType()
```

Returns the type of this module.

**Returns:** the type of this module

---

#### getModuleType

ModuleTree.ModuleKind

getModuleType()

Returns the type of this module.

getName

```java
ExpressionTree
getName()
```

Returns the name of the module.

**Returns:** the name of the module

---

#### getName

ExpressionTree

getName()

Returns the name of the module.

getDirectives

```java
List
<? extends
DirectiveTree
> getDirectives()
```

Returns the directives in the module declaration.

**Returns:** the directives in the module declaration

---

#### getDirectives

List

<? extends

DirectiveTree

> getDirectives()

Returns the directives in the module declaration.

---

