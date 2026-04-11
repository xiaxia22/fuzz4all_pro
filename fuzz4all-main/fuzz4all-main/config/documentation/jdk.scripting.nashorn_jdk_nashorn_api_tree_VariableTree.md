# Interface VariableTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\VariableTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
VariableTree

extends
StatementTree
```

A tree node for a

variable declaration statement

.

For example:

```java
var

name
[
initializer
] ;

var

binding_pattern
[
initializer
];
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

#### ExpressionTree
getBinding()

Returns the binding of this declaration. This is an

IdentifierTree

for a binding identifier case (simple variable declaration).
This is an

ObjectLiteralTree

or a

ArrayLiteralTree

for a
destructuring declaration.

**Returns:**
- the binding expression of this declaration

---

#### ExpressionTree
getInitializer()

Returns the initial value expression for this variable. This is
null if no initial value for this variable.

**Returns:**
- the initial value expression

---

#### boolean isConst()

Is this a const declaration?

**Returns:**
- true if this is a const declaration

---

#### boolean isLet()

Is this a let declaration?

**Returns:**
- true if this is a let declaration

---

### Additional Sections

#### Interface VariableTree

**All Superinterfaces:** StatementTree

,

Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
VariableTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a

variable declaration statement

.

For example:

```java
var

name
[
initializer
] ;

var

binding_pattern
[
initializer
];
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

VariableTree

extends

StatementTree

A tree node for a

variable declaration statement

.

For example:

```java
var

name
[
initializer
] ;

var

binding_pattern
[
initializer
];
```

var

name

[

initializer

] ;

var

binding_pattern

[

initializer

];

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ExpressionTree

getBinding

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the binding of this declaration.

ExpressionTree

getInitializer

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initial value expression for this variable.

boolean

isConst

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a const declaration?

boolean

isLet

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a let declaration?

- Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

Nested Class Summary

- Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface jdk.nashorn.api.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface jdk.nashorn.api.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ExpressionTree

getBinding

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the binding of this declaration.

ExpressionTree

getInitializer

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initial value expression for this variable.

boolean

isConst

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a const declaration?

boolean

isLet

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a let declaration?

- Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the binding of this declaration.

Returns the initial value expression for this variable.

Is this a const declaration?

Is this a let declaration?

Methods declared in interface jdk.nashorn.api.tree.

Tree

accept

,

getEndPosition

,

getKind

,

getStartPosition

---

#### Methods declared in interface jdk.nashorn.api.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getBinding

```java
ExpressionTree
getBinding()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the binding of this declaration. This is an

IdentifierTree

for a binding identifier case (simple variable declaration).
This is an

ObjectLiteralTree

or a

ArrayLiteralTree

for a
destructuring declaration.

**Returns:** the binding expression of this declaration

- getInitializer

```java
ExpressionTree
getInitializer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initial value expression for this variable. This is
null if no initial value for this variable.

**Returns:** the initial value expression

- isConst

```java
boolean isConst()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a const declaration?

**Returns:** true if this is a const declaration

- isLet

```java
boolean isLet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a let declaration?

**Returns:** true if this is a let declaration

Method Detail

- getBinding

```java
ExpressionTree
getBinding()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the binding of this declaration. This is an

IdentifierTree

for a binding identifier case (simple variable declaration).
This is an

ObjectLiteralTree

or a

ArrayLiteralTree

for a
destructuring declaration.

**Returns:** the binding expression of this declaration

- getInitializer

```java
ExpressionTree
getInitializer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initial value expression for this variable. This is
null if no initial value for this variable.

**Returns:** the initial value expression

- isConst

```java
boolean isConst()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a const declaration?

**Returns:** true if this is a const declaration

- isLet

```java
boolean isLet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a let declaration?

**Returns:** true if this is a let declaration

---

#### Method Detail

getBinding

```java
ExpressionTree
getBinding()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the binding of this declaration. This is an

IdentifierTree

for a binding identifier case (simple variable declaration).
This is an

ObjectLiteralTree

or a

ArrayLiteralTree

for a
destructuring declaration.

**Returns:** the binding expression of this declaration

---

#### getBinding

ExpressionTree

getBinding()

Returns the binding of this declaration. This is an

IdentifierTree

for a binding identifier case (simple variable declaration).
This is an

ObjectLiteralTree

or a

ArrayLiteralTree

for a
destructuring declaration.

getInitializer

```java
ExpressionTree
getInitializer()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the initial value expression for this variable. This is
null if no initial value for this variable.

**Returns:** the initial value expression

---

#### getInitializer

ExpressionTree

getInitializer()

Returns the initial value expression for this variable. This is
null if no initial value for this variable.

isConst

```java
boolean isConst()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a const declaration?

**Returns:** true if this is a const declaration

---

#### isConst

boolean isConst()

Is this a const declaration?

isLet

```java
boolean isLet()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a let declaration?

**Returns:** true if this is a let declaration

---

#### isLet

boolean isLet()

Is this a let declaration?

---

