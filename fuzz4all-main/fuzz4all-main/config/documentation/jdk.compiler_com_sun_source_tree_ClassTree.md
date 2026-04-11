# Interface ClassTree

**Source:** `jdk.compiler\com\sun\source\tree\ClassTree.html`

### Class Description

```java
public interface
ClassTree

extends
StatementTree
```

A tree node for a class, interface, enum, or annotation
type declaration.

For example:

```java
modifiers
class
simpleName

typeParameters

extends
extendsClause

implements
implementsClause

{

members

}
```

**All Superinterfaces:** StatementTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ModifiersTree
getModifiers()

Returns the modifiers, including any annotations,
for this type declaration.

**Returns:**
- the modifiers

---

#### Name
getSimpleName()

Returns the simple name of this type declaration.

**Returns:**
- the simple name

---

#### List
<? extends
TypeParameterTree
> getTypeParameters()

Returns any type parameters of this type declaration.

**Returns:**
- the type parameters

---

#### Tree
getExtendsClause()

Returns the supertype of this type declaration,
or

null

if none is provided.

**Returns:**
- the supertype

---

#### List
<? extends
Tree
> getImplementsClause()

Returns the interfaces implemented by this type declaration.

**Returns:**
- the interfaces

---

#### List
<? extends
Tree
> getMembers()

Returns the members declared in this type declaration.

**Returns:**
- the members

---

### Additional Sections

#### Interface ClassTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
ClassTree

extends
StatementTree
```

A tree node for a class, interface, enum, or annotation
type declaration.

For example:

```java
modifiers
class
simpleName

typeParameters

extends
extendsClause

implements
implementsClause

{

members

}
```

**Since:** 1.6
**See The Java™ Language Specification :** sections 8.1, 8.9, 9.1, and 9.6

public interface

ClassTree

extends

StatementTree

A tree node for a class, interface, enum, or annotation
type declaration.

For example:

```java
modifiers
class
simpleName

typeParameters

extends
extendsClause

implements
implementsClause

{

members

}
```

modifiers

class

simpleName

typeParameters

extends

extendsClause

implements

implementsClause

{

members

}

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

getExtendsClause

()

Returns the supertype of this type declaration,
or

null

if none is provided.

List

<? extends

Tree

>

getImplementsClause

()

Returns the interfaces implemented by this type declaration.

List

<? extends

Tree

>

getMembers

()

Returns the members declared in this type declaration.

ModifiersTree

getModifiers

()

Returns the modifiers, including any annotations,
for this type declaration.

Name

getSimpleName

()

Returns the simple name of this type declaration.

List

<? extends

TypeParameterTree

>

getTypeParameters

()

Returns any type parameters of this type declaration.

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

getExtendsClause

()

Returns the supertype of this type declaration,
or

null

if none is provided.

List

<? extends

Tree

>

getImplementsClause

()

Returns the interfaces implemented by this type declaration.

List

<? extends

Tree

>

getMembers

()

Returns the members declared in this type declaration.

ModifiersTree

getModifiers

()

Returns the modifiers, including any annotations,
for this type declaration.

Name

getSimpleName

()

Returns the simple name of this type declaration.

List

<? extends

TypeParameterTree

>

getTypeParameters

()

Returns any type parameters of this type declaration.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the supertype of this type declaration,
or

null

if none is provided.

Returns the interfaces implemented by this type declaration.

Returns the members declared in this type declaration.

Returns the modifiers, including any annotations,
for this type declaration.

Returns the simple name of this type declaration.

Returns any type parameters of this type declaration.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations,
for this type declaration.

**Returns:** the modifiers

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this type declaration.

**Returns:** the simple name

- getTypeParameters

```java
List
<? extends
TypeParameterTree
> getTypeParameters()
```

Returns any type parameters of this type declaration.

**Returns:** the type parameters

- getExtendsClause

```java
Tree
getExtendsClause()
```

Returns the supertype of this type declaration,
or

null

if none is provided.

**Returns:** the supertype

- getImplementsClause

```java
List
<? extends
Tree
> getImplementsClause()
```

Returns the interfaces implemented by this type declaration.

**Returns:** the interfaces

- getMembers

```java
List
<? extends
Tree
> getMembers()
```

Returns the members declared in this type declaration.

**Returns:** the members

Method Detail

- getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations,
for this type declaration.

**Returns:** the modifiers

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this type declaration.

**Returns:** the simple name

- getTypeParameters

```java
List
<? extends
TypeParameterTree
> getTypeParameters()
```

Returns any type parameters of this type declaration.

**Returns:** the type parameters

- getExtendsClause

```java
Tree
getExtendsClause()
```

Returns the supertype of this type declaration,
or

null

if none is provided.

**Returns:** the supertype

- getImplementsClause

```java
List
<? extends
Tree
> getImplementsClause()
```

Returns the interfaces implemented by this type declaration.

**Returns:** the interfaces

- getMembers

```java
List
<? extends
Tree
> getMembers()
```

Returns the members declared in this type declaration.

**Returns:** the members

---

#### Method Detail

getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations,
for this type declaration.

**Returns:** the modifiers

---

#### getModifiers

ModifiersTree

getModifiers()

Returns the modifiers, including any annotations,
for this type declaration.

getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this type declaration.

**Returns:** the simple name

---

#### getSimpleName

Name

getSimpleName()

Returns the simple name of this type declaration.

getTypeParameters

```java
List
<? extends
TypeParameterTree
> getTypeParameters()
```

Returns any type parameters of this type declaration.

**Returns:** the type parameters

---

#### getTypeParameters

List

<? extends

TypeParameterTree

> getTypeParameters()

Returns any type parameters of this type declaration.

getExtendsClause

```java
Tree
getExtendsClause()
```

Returns the supertype of this type declaration,
or

null

if none is provided.

**Returns:** the supertype

---

#### getExtendsClause

Tree

getExtendsClause()

Returns the supertype of this type declaration,
or

null

if none is provided.

getImplementsClause

```java
List
<? extends
Tree
> getImplementsClause()
```

Returns the interfaces implemented by this type declaration.

**Returns:** the interfaces

---

#### getImplementsClause

List

<? extends

Tree

> getImplementsClause()

Returns the interfaces implemented by this type declaration.

getMembers

```java
List
<? extends
Tree
> getMembers()
```

Returns the members declared in this type declaration.

**Returns:** the members

---

#### getMembers

List

<? extends

Tree

> getMembers()

Returns the members declared in this type declaration.

---

