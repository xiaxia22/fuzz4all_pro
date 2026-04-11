# Interface LambdaExpressionTree

**Source:** `jdk.compiler\com\sun\source\tree\LambdaExpressionTree.html`

### Class Description

```java
public interface
LambdaExpressionTree

extends
ExpressionTree
```

A tree node for a lambda expression.

For example:

```java
()->{}
(List<String> ls)->ls.size()
(x,y)-> { return x + y; }
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
VariableTree
> getParameters()

Returns the parameters of this lambda expression.

**Returns:**
- the parameters

---

#### Tree
getBody()

Returns the body of the lambda expression.

**Returns:**
- the body

---

#### LambdaExpressionTree.BodyKind
getBodyKind()

Returns the kind of the body of the lambda expression.

**Returns:**
- the kind of the body

---

### Additional Sections

#### Interface LambdaExpressionTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
LambdaExpressionTree

extends
ExpressionTree
```

A tree node for a lambda expression.

For example:

```java
()->{}
(List<String> ls)->ls.size()
(x,y)-> { return x + y; }
```

public interface

LambdaExpressionTree

extends

ExpressionTree

A tree node for a lambda expression.

For example:

```java
()->{}
(List<String> ls)->ls.size()
(x,y)-> { return x + y; }
```

()->{}
(List<String> ls)->ls.size()
(x,y)-> { return x + y; }

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

LambdaExpressionTree.BodyKind

Lambda expressions come in two forms:

expression lambdas, whose body is an expression, and
statement lambdas, whose body is a block

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

getBody

()

Returns the body of the lambda expression.

LambdaExpressionTree.BodyKind

getBodyKind

()

Returns the kind of the body of the lambda expression.

List

<? extends

VariableTree

>

getParameters

()

Returns the parameters of this lambda expression.

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

LambdaExpressionTree.BodyKind

Lambda expressions come in two forms:

expression lambdas, whose body is an expression, and
statement lambdas, whose body is a block

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Lambda expressions come in two forms:

expression lambdas, whose body is an expression, and
statement lambdas, whose body is a block

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

getBody

()

Returns the body of the lambda expression.

LambdaExpressionTree.BodyKind

getBodyKind

()

Returns the kind of the body of the lambda expression.

List

<? extends

VariableTree

>

getParameters

()

Returns the parameters of this lambda expression.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the body of the lambda expression.

Returns the kind of the body of the lambda expression.

Returns the parameters of this lambda expression.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getParameters

```java
List
<? extends
VariableTree
> getParameters()
```

Returns the parameters of this lambda expression.

**Returns:** the parameters

- getBody

```java
Tree
getBody()
```

Returns the body of the lambda expression.

**Returns:** the body

- getBodyKind

```java
LambdaExpressionTree.BodyKind
getBodyKind()
```

Returns the kind of the body of the lambda expression.

**Returns:** the kind of the body

Method Detail

- getParameters

```java
List
<? extends
VariableTree
> getParameters()
```

Returns the parameters of this lambda expression.

**Returns:** the parameters

- getBody

```java
Tree
getBody()
```

Returns the body of the lambda expression.

**Returns:** the body

- getBodyKind

```java
LambdaExpressionTree.BodyKind
getBodyKind()
```

Returns the kind of the body of the lambda expression.

**Returns:** the kind of the body

---

#### Method Detail

getParameters

```java
List
<? extends
VariableTree
> getParameters()
```

Returns the parameters of this lambda expression.

**Returns:** the parameters

---

#### getParameters

List

<? extends

VariableTree

> getParameters()

Returns the parameters of this lambda expression.

getBody

```java
Tree
getBody()
```

Returns the body of the lambda expression.

**Returns:** the body

---

#### getBody

Tree

getBody()

Returns the body of the lambda expression.

getBodyKind

```java
LambdaExpressionTree.BodyKind
getBodyKind()
```

Returns the kind of the body of the lambda expression.

**Returns:** the kind of the body

---

#### getBodyKind

LambdaExpressionTree.BodyKind

getBodyKind()

Returns the kind of the body of the lambda expression.

---

