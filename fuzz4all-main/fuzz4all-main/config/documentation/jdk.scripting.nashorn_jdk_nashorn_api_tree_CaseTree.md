# Interface CaseTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\CaseTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CaseTree

extends
Tree
```

A tree node for a 'case' in a 'switch' statement.

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

Case expression of this 'case' statement.

**Returns:**
- null if and only if this Case is

default:

---

#### List
<? extends
StatementTree
> getStatements()

Return the list of statements for this 'case'.

**Returns:**
- list of statements for this 'case'

---

### Additional Sections

#### Interface CaseTree

**All Superinterfaces:** Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
CaseTree

extends
Tree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'case' in a 'switch' statement.

For example:

```java
case
expression
:

statements

default :

statements
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

CaseTree

extends

Tree

A tree node for a 'case' in a 'switch' statement.

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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Case expression of this 'case' statement.

List

<? extends

StatementTree

>

getStatements

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of statements for this 'case'.

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

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Case expression of this 'case' statement.

List

<? extends

StatementTree

>

getStatements

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of statements for this 'case'.

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

Case expression of this 'case' statement.

Return the list of statements for this 'case'.

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

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Case expression of this 'case' statement.

**Returns:** null if and only if this Case is

default:

- getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of statements for this 'case'.

**Returns:** list of statements for this 'case'

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Case expression of this 'case' statement.

**Returns:** null if and only if this Case is

default:

- getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of statements for this 'case'.

**Returns:** list of statements for this 'case'

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Case expression of this 'case' statement.

**Returns:** null if and only if this Case is

default:

---

#### getExpression

ExpressionTree

getExpression()

Case expression of this 'case' statement.

getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the list of statements for this 'case'.

**Returns:** list of statements for this 'case'

---

#### getStatements

List

<? extends

StatementTree

> getStatements()

Return the list of statements for this 'case'.

---

