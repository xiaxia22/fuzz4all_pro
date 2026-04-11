# Interface SwitchTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\SwitchTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
SwitchTree

extends
StatementTree
```

A tree node for a 'switch' statement.

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

Returns the expression on which this statement switches.

**Returns:**
- the switch expression

---

#### List
<? extends
CaseTree
> getCases()

Returns the list of 'case' statements.

**Returns:**
- the 'case' statements

---

### Additional Sections

#### Interface SwitchTree

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
SwitchTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a 'switch' statement.

For example:

```java
switch (
expression
) {

cases

}
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

SwitchTree

extends

StatementTree

A tree node for a 'switch' statement.

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

List

<? extends

CaseTree

>

getCases

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'case' statements.

ExpressionTree

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression on which this statement switches.

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

List

<? extends

CaseTree

>

getCases

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'case' statements.

ExpressionTree

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression on which this statement switches.

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

Returns the list of 'case' statements.

Returns the expression on which this statement switches.

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

Returns the expression on which this statement switches.

**Returns:** the switch expression

- getCases

```java
List
<? extends
CaseTree
> getCases()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'case' statements.

**Returns:** the 'case' statements

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression on which this statement switches.

**Returns:** the switch expression

- getCases

```java
List
<? extends
CaseTree
> getCases()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'case' statements.

**Returns:** the 'case' statements

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression on which this statement switches.

**Returns:** the switch expression

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression on which this statement switches.

getCases

```java
List
<? extends
CaseTree
> getCases()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of 'case' statements.

**Returns:** the 'case' statements

---

#### getCases

List

<? extends

CaseTree

> getCases()

Returns the list of 'case' statements.

---

