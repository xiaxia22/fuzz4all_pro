# Interface NewClassTree

**Source:** `jdk.compiler\com\sun\source\tree\NewClassTree.html`

### Class Description

```java
public interface
NewClassTree

extends
ExpressionTree
```

A tree node to declare a new instance of a class.

For example:

```java
new
identifier
( )

new
identifier
(
arguments
)

new
typeArguments

identifier
(
arguments
)

classBody

enclosingExpression
.new
identifier
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

#### ExpressionTree
getEnclosingExpression()

Returns the enclosing expression, or

null

if none.

**Returns:**
- the enclosing expression

---

#### List
<? extends
Tree
> getTypeArguments()

Returns the type arguments for the object being created.

**Returns:**
- the type arguments

---

#### ExpressionTree
getIdentifier()

Returns the name of the class being instantiated.

**Returns:**
- the name

---

#### List
<? extends
ExpressionTree
> getArguments()

Returns the arguments for the constructor to be invoked.

**Returns:**
- the arguments

---

#### ClassTree
getClassBody()

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

**Returns:**
- the class body

---

### Additional Sections

#### Interface NewClassTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
NewClassTree

extends
ExpressionTree
```

A tree node to declare a new instance of a class.

For example:

```java
new
identifier
( )

new
identifier
(
arguments
)

new
typeArguments

identifier
(
arguments
)

classBody

enclosingExpression
.new
identifier
(
arguments
)
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.9

public interface

NewClassTree

extends

ExpressionTree

A tree node to declare a new instance of a class.

For example:

```java
new
identifier
( )

new
identifier
(
arguments
)

new
typeArguments

identifier
(
arguments
)

classBody

enclosingExpression
.new
identifier
(
arguments
)
```

new

identifier

( )

new

identifier

(

arguments

)

new

typeArguments

identifier

(

arguments

)

classBody

enclosingExpression

.new

identifier

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

List

<? extends

ExpressionTree

>

getArguments

()

Returns the arguments for the constructor to be invoked.

ClassTree

getClassBody

()

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

ExpressionTree

getEnclosingExpression

()

Returns the enclosing expression, or

null

if none.

ExpressionTree

getIdentifier

()

Returns the name of the class being instantiated.

List

<? extends

Tree

>

getTypeArguments

()

Returns the type arguments for the object being created.

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

ExpressionTree

>

getArguments

()

Returns the arguments for the constructor to be invoked.

ClassTree

getClassBody

()

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

ExpressionTree

getEnclosingExpression

()

Returns the enclosing expression, or

null

if none.

ExpressionTree

getIdentifier

()

Returns the name of the class being instantiated.

List

<? extends

Tree

>

getTypeArguments

()

Returns the type arguments for the object being created.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the arguments for the constructor to be invoked.

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

Returns the enclosing expression, or

null

if none.

Returns the name of the class being instantiated.

Returns the type arguments for the object being created.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getEnclosingExpression

```java
ExpressionTree
getEnclosingExpression()
```

Returns the enclosing expression, or

null

if none.

**Returns:** the enclosing expression

- getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments for the object being created.

**Returns:** the type arguments

- getIdentifier

```java
ExpressionTree
getIdentifier()
```

Returns the name of the class being instantiated.

**Returns:** the name

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments for the constructor to be invoked.

**Returns:** the arguments

- getClassBody

```java
ClassTree
getClassBody()
```

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

**Returns:** the class body

Method Detail

- getEnclosingExpression

```java
ExpressionTree
getEnclosingExpression()
```

Returns the enclosing expression, or

null

if none.

**Returns:** the enclosing expression

- getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments for the object being created.

**Returns:** the type arguments

- getIdentifier

```java
ExpressionTree
getIdentifier()
```

Returns the name of the class being instantiated.

**Returns:** the name

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments for the constructor to be invoked.

**Returns:** the arguments

- getClassBody

```java
ClassTree
getClassBody()
```

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

**Returns:** the class body

---

#### Method Detail

getEnclosingExpression

```java
ExpressionTree
getEnclosingExpression()
```

Returns the enclosing expression, or

null

if none.

**Returns:** the enclosing expression

---

#### getEnclosingExpression

ExpressionTree

getEnclosingExpression()

Returns the enclosing expression, or

null

if none.

getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments for the object being created.

**Returns:** the type arguments

---

#### getTypeArguments

List

<? extends

Tree

> getTypeArguments()

Returns the type arguments for the object being created.

getIdentifier

```java
ExpressionTree
getIdentifier()
```

Returns the name of the class being instantiated.

**Returns:** the name

---

#### getIdentifier

ExpressionTree

getIdentifier()

Returns the name of the class being instantiated.

getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments for the constructor to be invoked.

**Returns:** the arguments

---

#### getArguments

List

<? extends

ExpressionTree

> getArguments()

Returns the arguments for the constructor to be invoked.

getClassBody

```java
ClassTree
getClassBody()
```

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

**Returns:** the class body

---

#### getClassBody

ClassTree

getClassBody()

Returns the class body if an anonymous class is being
instantiated, and

null

otherwise.

---

