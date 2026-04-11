# Interface VariableTree

**Source:** `jdk.compiler\com\sun\source\tree\VariableTree.html`

### Class Description

```java
public interface
VariableTree

extends
StatementTree
```

A tree node for a variable declaration.

For example:

```java
modifiers

type

name

initializer
;

modifiers

type

qualified-name
.this
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

Returns the modifiers, including any annotations, on the declaration.

**Returns:**
- the modifiers

---

#### Name
getName()

Returns the name of the variable being declared.

**Returns:**
- the name

---

#### ExpressionTree
getNameExpression()

Returns the qualified identifier for the name being "declared".
This is only used in certain cases for the receiver of a
method declaration. Returns

null

in all other cases.

**Returns:**
- the qualified identifier of a receiver declaration

---

#### Tree
getType()

Returns the type of the variable being declared.

**Returns:**
- the type

---

#### ExpressionTree
getInitializer()

Returns the initializer for the variable, or

null

if none.

**Returns:**
- the initializer

---

### Additional Sections

#### Interface VariableTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
VariableTree

extends
StatementTree
```

A tree node for a variable declaration.

For example:

```java
modifiers

type

name

initializer
;

modifiers

type

qualified-name
.this
```

**Since:** 1.6
**See The Java™ Language Specification :** sections 8.3 and 14.4

public interface

VariableTree

extends

StatementTree

A tree node for a variable declaration.

For example:

```java
modifiers

type

name

initializer
;

modifiers

type

qualified-name
.this
```

modifiers

type

name

initializer

;

modifiers

type

qualified-name

.this

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

ExpressionTree

getInitializer

()

Returns the initializer for the variable, or

null

if none.

ModifiersTree

getModifiers

()

Returns the modifiers, including any annotations, on the declaration.

Name

getName

()

Returns the name of the variable being declared.

ExpressionTree

getNameExpression

()

Returns the qualified identifier for the name being "declared".

Tree

getType

()

Returns the type of the variable being declared.

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

ExpressionTree

getInitializer

()

Returns the initializer for the variable, or

null

if none.

ModifiersTree

getModifiers

()

Returns the modifiers, including any annotations, on the declaration.

Name

getName

()

Returns the name of the variable being declared.

ExpressionTree

getNameExpression

()

Returns the qualified identifier for the name being "declared".

Tree

getType

()

Returns the type of the variable being declared.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the initializer for the variable, or

null

if none.

Returns the modifiers, including any annotations, on the declaration.

Returns the name of the variable being declared.

Returns the qualified identifier for the name being "declared".

Returns the type of the variable being declared.

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

Returns the modifiers, including any annotations, on the declaration.

**Returns:** the modifiers

- getName

```java
Name
getName()
```

Returns the name of the variable being declared.

**Returns:** the name

- getNameExpression

```java
ExpressionTree
getNameExpression()
```

Returns the qualified identifier for the name being "declared".
This is only used in certain cases for the receiver of a
method declaration. Returns

null

in all other cases.

**Returns:** the qualified identifier of a receiver declaration

- getType

```java
Tree
getType()
```

Returns the type of the variable being declared.

**Returns:** the type

- getInitializer

```java
ExpressionTree
getInitializer()
```

Returns the initializer for the variable, or

null

if none.

**Returns:** the initializer

Method Detail

- getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations, on the declaration.

**Returns:** the modifiers

- getName

```java
Name
getName()
```

Returns the name of the variable being declared.

**Returns:** the name

- getNameExpression

```java
ExpressionTree
getNameExpression()
```

Returns the qualified identifier for the name being "declared".
This is only used in certain cases for the receiver of a
method declaration. Returns

null

in all other cases.

**Returns:** the qualified identifier of a receiver declaration

- getType

```java
Tree
getType()
```

Returns the type of the variable being declared.

**Returns:** the type

- getInitializer

```java
ExpressionTree
getInitializer()
```

Returns the initializer for the variable, or

null

if none.

**Returns:** the initializer

---

#### Method Detail

getModifiers

```java
ModifiersTree
getModifiers()
```

Returns the modifiers, including any annotations, on the declaration.

**Returns:** the modifiers

---

#### getModifiers

ModifiersTree

getModifiers()

Returns the modifiers, including any annotations, on the declaration.

getName

```java
Name
getName()
```

Returns the name of the variable being declared.

**Returns:** the name

---

#### getName

Name

getName()

Returns the name of the variable being declared.

getNameExpression

```java
ExpressionTree
getNameExpression()
```

Returns the qualified identifier for the name being "declared".
This is only used in certain cases for the receiver of a
method declaration. Returns

null

in all other cases.

**Returns:** the qualified identifier of a receiver declaration

---

#### getNameExpression

ExpressionTree

getNameExpression()

Returns the qualified identifier for the name being "declared".
This is only used in certain cases for the receiver of a
method declaration. Returns

null

in all other cases.

getType

```java
Tree
getType()
```

Returns the type of the variable being declared.

**Returns:** the type

---

#### getType

Tree

getType()

Returns the type of the variable being declared.

getInitializer

```java
ExpressionTree
getInitializer()
```

Returns the initializer for the variable, or

null

if none.

**Returns:** the initializer

---

#### getInitializer

ExpressionTree

getInitializer()

Returns the initializer for the variable, or

null

if none.

---

