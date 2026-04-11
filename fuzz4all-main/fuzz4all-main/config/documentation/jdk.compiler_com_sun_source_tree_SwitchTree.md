# Interface SwitchTree

**Source:** `jdk.compiler\com\sun\source\tree\SwitchTree.html`

### Class Description

```java
public interface
SwitchTree

extends
StatementTree
```

A tree node for a

switch

statement.

For example:

```java
switch (
expression
) {

cases

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

#### ExpressionTree
getExpression()

Returns the expression for the

switch

statement.

**Returns:**
- the expression

---

#### List
<? extends
CaseTree
> getCases()

Returns the cases for the

switch

statement.

**Returns:**
- the cases

---

### Additional Sections

#### Interface SwitchTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
SwitchTree

extends
StatementTree
```

A tree node for a

switch

statement.

For example:

```java
switch (
expression
) {

cases

}
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.11

public interface

SwitchTree

extends

StatementTree

A tree node for a

switch

statement.

For example:

```java
switch (
expression
) {

cases

}
```

switch (

expression

) {

cases

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

List

<? extends

CaseTree

>

getCases

()

Returns the cases for the

switch

statement.

ExpressionTree

getExpression

()

Returns the expression for the

switch

statement.

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

CaseTree

>

getCases

()

Returns the cases for the

switch

statement.

ExpressionTree

getExpression

()

Returns the expression for the

switch

statement.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the cases for the

switch

statement.

Returns the expression for the

switch

statement.

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

Returns the expression for the

switch

statement.

**Returns:** the expression

- getCases

```java
List
<? extends
CaseTree
> getCases()
```

Returns the cases for the

switch

statement.

**Returns:** the cases

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the

switch

statement.

**Returns:** the expression

- getCases

```java
List
<? extends
CaseTree
> getCases()
```

Returns the cases for the

switch

statement.

**Returns:** the cases

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Returns the expression for the

switch

statement.

**Returns:** the expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression for the

switch

statement.

getCases

```java
List
<? extends
CaseTree
> getCases()
```

Returns the cases for the

switch

statement.

**Returns:** the cases

---

#### getCases

List

<? extends

CaseTree

> getCases()

Returns the cases for the

switch

statement.

---

