# Interface MethodInvocationTree

**Source:** `jdk.compiler\com\sun\source\tree\MethodInvocationTree.html`

### Class Description

```java
public interface
MethodInvocationTree

extends
ExpressionTree
```

A tree node for a method invocation expression.

For example:

```java
identifier
(
arguments
)

this .
typeArguments

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

#### List
<? extends
Tree
> getTypeArguments()

Returns the type arguments for this method invocation.

**Returns:**
- the type arguments

---

#### ExpressionTree
getMethodSelect()

Returns the expression identifying the method to be invoked.

**Returns:**
- the method selection expression

---

#### List
<? extends
ExpressionTree
> getArguments()

Returns the arguments for the method invocation.

**Returns:**
- the arguments

---

### Additional Sections

#### Interface MethodInvocationTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
MethodInvocationTree

extends
ExpressionTree
```

A tree node for a method invocation expression.

For example:

```java
identifier
(
arguments
)

this .
typeArguments

identifier
(
arguments
)
```

**Since:** 1.6
**See The Java™ Language Specification :** section 15.12

public interface

MethodInvocationTree

extends

ExpressionTree

A tree node for a method invocation expression.

For example:

```java
identifier
(
arguments
)

this .
typeArguments

identifier
(
arguments
)
```

identifier

(

arguments

)

this .

typeArguments

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

Returns the arguments for the method invocation.

ExpressionTree

getMethodSelect

()

Returns the expression identifying the method to be invoked.

List

<? extends

Tree

>

getTypeArguments

()

Returns the type arguments for this method invocation.

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

Returns the arguments for the method invocation.

ExpressionTree

getMethodSelect

()

Returns the expression identifying the method to be invoked.

List

<? extends

Tree

>

getTypeArguments

()

Returns the type arguments for this method invocation.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the arguments for the method invocation.

Returns the expression identifying the method to be invoked.

Returns the type arguments for this method invocation.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments for this method invocation.

**Returns:** the type arguments

- getMethodSelect

```java
ExpressionTree
getMethodSelect()
```

Returns the expression identifying the method to be invoked.

**Returns:** the method selection expression

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments for the method invocation.

**Returns:** the arguments

Method Detail

- getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments for this method invocation.

**Returns:** the type arguments

- getMethodSelect

```java
ExpressionTree
getMethodSelect()
```

Returns the expression identifying the method to be invoked.

**Returns:** the method selection expression

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments for the method invocation.

**Returns:** the arguments

---

#### Method Detail

getTypeArguments

```java
List
<? extends
Tree
> getTypeArguments()
```

Returns the type arguments for this method invocation.

**Returns:** the type arguments

---

#### getTypeArguments

List

<? extends

Tree

> getTypeArguments()

Returns the type arguments for this method invocation.

getMethodSelect

```java
ExpressionTree
getMethodSelect()
```

Returns the expression identifying the method to be invoked.

**Returns:** the method selection expression

---

#### getMethodSelect

ExpressionTree

getMethodSelect()

Returns the expression identifying the method to be invoked.

getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Returns the arguments for the method invocation.

**Returns:** the arguments

---

#### getArguments

List

<? extends

ExpressionTree

> getArguments()

Returns the arguments for the method invocation.

---

