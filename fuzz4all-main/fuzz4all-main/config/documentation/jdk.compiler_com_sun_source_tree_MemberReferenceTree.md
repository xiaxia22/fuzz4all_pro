# Interface MemberReferenceTree

**Source:** `jdk.compiler\com\sun\source\tree\MemberReferenceTree.html`

### Class Description

```java
public interface
MemberReferenceTree

extends
ExpressionTree
```

A tree node for a member reference expression.

For example:

```java
expression
#
[ identifier | new ]
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

#### MemberReferenceTree.ReferenceMode
getMode()

Returns the mode of the reference.

**Returns:**
- the mode

---

#### ExpressionTree
getQualifierExpression()

Returns the qualifier expression for the reference.

**Returns:**
- the qualifier expression

---

#### Name
getName()

Returns the name of the reference.

**Returns:**
- the name

---

#### List
<? extends
ExpressionTree
> getTypeArguments()

Returns the type arguments for the reference.

**Returns:**
- the type arguments

---

### Additional Sections

#### Interface MemberReferenceTree

**All Superinterfaces:** ExpressionTree

,

Tree

```java
public interface
MemberReferenceTree

extends
ExpressionTree
```

A tree node for a member reference expression.

For example:

```java
expression
#
[ identifier | new ]
```

**Since:** 1.8

public interface

MemberReferenceTree

extends

ExpressionTree

A tree node for a member reference expression.

For example:

```java
expression
#
[ identifier | new ]
```

expression

#

[ identifier | new ]

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

MemberReferenceTree.ReferenceMode

There are two kinds of member references: (i) method references and
(ii) constructor references

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

MemberReferenceTree.ReferenceMode

getMode

()

Returns the mode of the reference.

Name

getName

()

Returns the name of the reference.

ExpressionTree

getQualifierExpression

()

Returns the qualifier expression for the reference.

List

<? extends

ExpressionTree

>

getTypeArguments

()

Returns the type arguments for the reference.

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

MemberReferenceTree.ReferenceMode

There are two kinds of member references: (i) method references and
(ii) constructor references

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

There are two kinds of member references: (i) method references and
(ii) constructor references

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

MemberReferenceTree.ReferenceMode

getMode

()

Returns the mode of the reference.

Name

getName

()

Returns the name of the reference.

ExpressionTree

getQualifierExpression

()

Returns the qualifier expression for the reference.

List

<? extends

ExpressionTree

>

getTypeArguments

()

Returns the type arguments for the reference.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the mode of the reference.

Returns the name of the reference.

Returns the qualifier expression for the reference.

Returns the type arguments for the reference.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getMode

```java
MemberReferenceTree.ReferenceMode
getMode()
```

Returns the mode of the reference.

**Returns:** the mode

- getQualifierExpression

```java
ExpressionTree
getQualifierExpression()
```

Returns the qualifier expression for the reference.

**Returns:** the qualifier expression

- getName

```java
Name
getName()
```

Returns the name of the reference.

**Returns:** the name

- getTypeArguments

```java
List
<? extends
ExpressionTree
> getTypeArguments()
```

Returns the type arguments for the reference.

**Returns:** the type arguments

Method Detail

- getMode

```java
MemberReferenceTree.ReferenceMode
getMode()
```

Returns the mode of the reference.

**Returns:** the mode

- getQualifierExpression

```java
ExpressionTree
getQualifierExpression()
```

Returns the qualifier expression for the reference.

**Returns:** the qualifier expression

- getName

```java
Name
getName()
```

Returns the name of the reference.

**Returns:** the name

- getTypeArguments

```java
List
<? extends
ExpressionTree
> getTypeArguments()
```

Returns the type arguments for the reference.

**Returns:** the type arguments

---

#### Method Detail

getMode

```java
MemberReferenceTree.ReferenceMode
getMode()
```

Returns the mode of the reference.

**Returns:** the mode

---

#### getMode

MemberReferenceTree.ReferenceMode

getMode()

Returns the mode of the reference.

getQualifierExpression

```java
ExpressionTree
getQualifierExpression()
```

Returns the qualifier expression for the reference.

**Returns:** the qualifier expression

---

#### getQualifierExpression

ExpressionTree

getQualifierExpression()

Returns the qualifier expression for the reference.

getName

```java
Name
getName()
```

Returns the name of the reference.

**Returns:** the name

---

#### getName

Name

getName()

Returns the name of the reference.

getTypeArguments

```java
List
<? extends
ExpressionTree
> getTypeArguments()
```

Returns the type arguments for the reference.

**Returns:** the type arguments

---

#### getTypeArguments

List

<? extends

ExpressionTree

> getTypeArguments()

Returns the type arguments for the reference.

---

