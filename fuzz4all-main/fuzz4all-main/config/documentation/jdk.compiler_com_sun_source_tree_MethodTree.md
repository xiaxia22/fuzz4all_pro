# Interface MethodTree

**Source:** `jdk.compiler\com\sun\source\tree\MethodTree.html`

### Class Description

```java
public interface
MethodTree

extends
Tree
```

A tree node for a method or annotation type element declaration.

For example:

```java
modifiers

typeParameters

type

name

(
parameters
)

body

modifiers

type

name
() default
defaultValue
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ModifiersTree
getModifiers()

Returns the modifiers, including any annotations for the method being declared.

**Returns:**
- the modifiers

---

#### Name
getName()

Returns the name of the method being declared.

**Returns:**
- the name

---

#### Tree
getReturnType()

Returns the return type of the method being declared.
Returns

null

for a constructor.

**Returns:**
- the return type

---

#### List
<? extends
TypeParameterTree
> getTypeParameters()

Returns the type parameters of the method being declared.

**Returns:**
- the type parameters

---

#### List
<? extends
VariableTree
> getParameters()

Returns the parameters of the method being declared.

**Returns:**
- the parameters

---

#### VariableTree
getReceiverParameter()

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

**Returns:**
- an explicit receiver parameter ("this" parameter)

**Since:**
- 1.8

---

#### List
<? extends
ExpressionTree
> getThrows()

Returns the exceptions listed as being thrown by this method.

**Returns:**
- the exceptions

---

#### BlockTree
getBody()

Returns the method body, or

null

if this is an abstract or native method.

**Returns:**
- the method body

---

#### Tree
getDefaultValue()

Returns the default value, if this is an element within
an annotation type declaration.
Returns

null

otherwise.

**Returns:**
- the default value

---

### Additional Sections

#### Interface MethodTree

**All Superinterfaces:** Tree

```java
public interface
MethodTree

extends
Tree
```

A tree node for a method or annotation type element declaration.

For example:

```java
modifiers

typeParameters

type

name

(
parameters
)

body

modifiers

type

name
() default
defaultValue
```

**Since:** 1.6
**See The Java™ Language Specification :** sections 8.4, 8.6, 8.7, 9.4, and 9.6

public interface

MethodTree

extends

Tree

A tree node for a method or annotation type element declaration.

For example:

```java
modifiers

typeParameters

type

name

(
parameters
)

body

modifiers

type

name
() default
defaultValue
```

modifiers

typeParameters

type

name

(

parameters

)

body

modifiers

type

name

() default

defaultValue

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

BlockTree

getBody

()

Returns the method body, or

null

if this is an abstract or native method.

Tree

getDefaultValue

()

Returns the default value, if this is an element within
an annotation type declaration.

ModifiersTree

getModifiers

()

Returns the modifiers, including any annotations for the method being declared.

Name

getName

()

Returns the name of the method being declared.

List

<? extends

VariableTree

>

getParameters

()

Returns the parameters of the method being declared.

VariableTree

getReceiverParameter

()

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

Tree

getReturnType

()

Returns the return type of the method being declared.

List

<? extends

ExpressionTree

>

getThrows

()

Returns the exceptions listed as being thrown by this method.

List

<? extends

TypeParameterTree

>

getTypeParameters

()

Returns the type parameters of the method being declared.

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

BlockTree

getBody

()

Returns the method body, or

null

if this is an abstract or native method.

Tree

getDefaultValue

()

Returns the default value, if this is an element within
an annotation type declaration.

ModifiersTree

getModifiers

()

Returns the modifiers, including any annotations for the method being declared.

Name

getName

()

Returns the name of the method being declared.

List

<? extends

VariableTree

>

getParameters

()

Returns the parameters of the method being declared.

VariableTree

getReceiverParameter

()

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

Tree

getReturnType

()

Returns the return type of the method being declared.

List

<? extends

ExpressionTree

>

getThrows

()

Returns the exceptions listed as being thrown by this method.

List

<? extends

TypeParameterTree

>

getTypeParameters

()

Returns the type parameters of the method being declared.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the method body, or

null

if this is an abstract or native method.

Returns the default value, if this is an element within
an annotation type declaration.

Returns the modifiers, including any annotations for the method being declared.

Returns the name of the method being declared.

Returns the parameters of the method being declared.

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

Returns the return type of the method being declared.

Returns the exceptions listed as being thrown by this method.

Returns the type parameters of the method being declared.

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

Returns the modifiers, including any annotations for the method being declared.

**Returns:** the modifiers

- getName

```java
Name
getName()
```

Returns the name of the method being declared.

**Returns:** the name

- getReturnType

```java
Tree
getReturnType()
```

Returns the return type of the method being declared.
Returns

null

for a constructor.

**Returns:** the return type

- getTypeParameters

```java
List
<? extends
TypeParameterTree
> getTypeParameters()
```

Returns the type parameters of the method being declared.

**Returns:** the type parameters

- getParameters

```java
List
<? extends
VariableTree
> getParameters()
```

Returns the parameters of the method being declared.

**Returns:** the parameters

- getReceiverParameter

```java
VariableTree
getReceiverParameter()
```

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

**Returns:** an explicit receiver parameter ("this" parameter)
**Since:** 1.8

- getThrows

```java
List
<? extends
ExpressionTree
> getThrows()
```

Returns the exceptions listed as being thrown by this method.

**Returns:** the exceptions

- getBody

```java
BlockTree
getBody()
```

Returns the method body, or

null

if this is an abstract or native method.

**Returns:** the method body

- getDefaultValue

```java
Tree
getDefaultValue()
```

Returns the default value, if this is an element within
an annotation type declaration.
Returns

null

otherwise.

**Returns:** the default value

Method Detail

- getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations for the method being declared.

**Returns:** the modifiers

- getName

```java
Name
getName()
```

Returns the name of the method being declared.

**Returns:** the name

- getReturnType

```java
Tree
getReturnType()
```

Returns the return type of the method being declared.
Returns

null

for a constructor.

**Returns:** the return type

- getTypeParameters

```java
List
<? extends
TypeParameterTree
> getTypeParameters()
```

Returns the type parameters of the method being declared.

**Returns:** the type parameters

- getParameters

```java
List
<? extends
VariableTree
> getParameters()
```

Returns the parameters of the method being declared.

**Returns:** the parameters

- getReceiverParameter

```java
VariableTree
getReceiverParameter()
```

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

**Returns:** an explicit receiver parameter ("this" parameter)
**Since:** 1.8

- getThrows

```java
List
<? extends
ExpressionTree
> getThrows()
```

Returns the exceptions listed as being thrown by this method.

**Returns:** the exceptions

- getBody

```java
BlockTree
getBody()
```

Returns the method body, or

null

if this is an abstract or native method.

**Returns:** the method body

- getDefaultValue

```java
Tree
getDefaultValue()
```

Returns the default value, if this is an element within
an annotation type declaration.
Returns

null

otherwise.

**Returns:** the default value

---

#### Method Detail

getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations for the method being declared.

**Returns:** the modifiers

---

#### getModifiers

ModifiersTree

getModifiers()

Returns the modifiers, including any annotations for the method being declared.

getName

```java
Name
getName()
```

Returns the name of the method being declared.

**Returns:** the name

---

#### getName

Name

getName()

Returns the name of the method being declared.

getReturnType

```java
Tree
getReturnType()
```

Returns the return type of the method being declared.
Returns

null

for a constructor.

**Returns:** the return type

---

#### getReturnType

Tree

getReturnType()

Returns the return type of the method being declared.
Returns

null

for a constructor.

getTypeParameters

```java
List
<? extends
TypeParameterTree
> getTypeParameters()
```

Returns the type parameters of the method being declared.

**Returns:** the type parameters

---

#### getTypeParameters

List

<? extends

TypeParameterTree

> getTypeParameters()

Returns the type parameters of the method being declared.

getParameters

```java
List
<? extends
VariableTree
> getParameters()
```

Returns the parameters of the method being declared.

**Returns:** the parameters

---

#### getParameters

List

<? extends

VariableTree

> getParameters()

Returns the parameters of the method being declared.

getReceiverParameter

```java
VariableTree
getReceiverParameter()
```

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

**Returns:** an explicit receiver parameter ("this" parameter)
**Since:** 1.8

---

#### getReceiverParameter

VariableTree

getReceiverParameter()

Return an explicit receiver parameter ("this" parameter),
or

null

if none.

getThrows

```java
List
<? extends
ExpressionTree
> getThrows()
```

Returns the exceptions listed as being thrown by this method.

**Returns:** the exceptions

---

#### getThrows

List

<? extends

ExpressionTree

> getThrows()

Returns the exceptions listed as being thrown by this method.

getBody

```java
BlockTree
getBody()
```

Returns the method body, or

null

if this is an abstract or native method.

**Returns:** the method body

---

#### getBody

BlockTree

getBody()

Returns the method body, or

null

if this is an abstract or native method.

getDefaultValue

```java
Tree
getDefaultValue()
```

Returns the default value, if this is an element within
an annotation type declaration.
Returns

null

otherwise.

**Returns:** the default value

---

#### getDefaultValue

Tree

getDefaultValue()

Returns the default value, if this is an element within
an annotation type declaration.
Returns

null

otherwise.

---

