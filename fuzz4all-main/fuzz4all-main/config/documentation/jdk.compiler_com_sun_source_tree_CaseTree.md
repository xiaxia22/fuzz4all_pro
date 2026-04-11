# Interface CaseTree

**Source:** `jdk.compiler\com\sun\source\tree\CaseTree.html`

### Class Description

```java
public interface
CaseTree

extends
Tree
```

A tree node for a

case

in a

switch

statement.

For example:

```java
case
expression
:

statements

default :

statements
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ExpressionTree
getExpression()

Returns the expression for the case, or

null

if this is the default case.

**Returns:**
- the expression for the case, or null

---

#### List
<? extends
StatementTree
> getStatements()

Returns the statements labeled by the case.

**Returns:**
- the statements labeled by the case

---

### Additional Sections

#### Interface CaseTree

**All Superinterfaces:** Tree

```java
public interface
CaseTree

extends
Tree
```

A tree node for a

case

in a

switch

statement.

For example:

```java
case
expression
:

statements

default :

statements
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.11

public interface

CaseTree

extends

Tree

A tree node for a

case

in a

switch

statement.

For example:

```java
case
expression
:

statements

default :

statements
```

case

expression

:

statements

default :

statements

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

getExpression

()

Returns the expression for the case, or

null

if this is the default case.

List

<? extends

StatementTree

>

getStatements

()

Returns the statements labeled by the case.

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

getExpression

()

Returns the expression for the case, or

null

if this is the default case.

List

<? extends

StatementTree

>

getStatements

()

Returns the statements labeled by the case.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the expression for the case, or

null

if this is the default case.

Returns the statements labeled by the case.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the case, or

null

if this is the default case.

**Returns:** the expression for the case, or null

- getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Returns the statements labeled by the case.

**Returns:** the statements labeled by the case

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the case, or

null

if this is the default case.

**Returns:** the expression for the case, or null

- getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Returns the statements labeled by the case.

**Returns:** the statements labeled by the case

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the case, or

null

if this is the default case.

**Returns:** the expression for the case, or null

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression for the case, or

null

if this is the default case.

getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Returns the statements labeled by the case.

**Returns:** the statements labeled by the case

---

#### getStatements

List

<? extends

StatementTree

> getStatements()

Returns the statements labeled by the case.

---

