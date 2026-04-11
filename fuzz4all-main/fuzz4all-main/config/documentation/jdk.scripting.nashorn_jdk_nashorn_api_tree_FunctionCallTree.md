# Interface FunctionCallTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\FunctionCallTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
FunctionCallTree

extends
ExpressionTree
```

A tree node for a function call expression.

For example:

```java
identifier
(
arguments
)

this .
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
getFunctionSelect()

Returns the function being called.

**Returns:**
- the function being called

---

#### List
<? extends
ExpressionTree
> getArguments()

Returns the list of arguments being passed to this function call.

**Returns:**
- the list of argument expressions

---

### Additional Sections

#### Interface FunctionCallTree

**All Superinterfaces:** ExpressionTree

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
FunctionCallTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a function call expression.

For example:

```java
identifier
(
arguments
)

this .
identifier
(
arguments
)
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

FunctionCallTree

extends

ExpressionTree

A tree node for a function call expression.

For example:

```java
identifier
(
arguments
)

this .
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

identifier

(

arguments

)

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

ExpressionTree

>

getArguments

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of arguments being passed to this function call.

ExpressionTree

getFunctionSelect

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the function being called.

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

ExpressionTree

>

getArguments

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of arguments being passed to this function call.

ExpressionTree

getFunctionSelect

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the function being called.

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

Returns the list of arguments being passed to this function call.

Returns the function being called.

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

- getFunctionSelect

```java
ExpressionTree
getFunctionSelect()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the function being called.

**Returns:** the function being called

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of arguments being passed to this function call.

**Returns:** the list of argument expressions

Method Detail

- getFunctionSelect

```java
ExpressionTree
getFunctionSelect()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the function being called.

**Returns:** the function being called

- getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of arguments being passed to this function call.

**Returns:** the list of argument expressions

---

#### Method Detail

getFunctionSelect

```java
ExpressionTree
getFunctionSelect()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the function being called.

**Returns:** the function being called

---

#### getFunctionSelect

ExpressionTree

getFunctionSelect()

Returns the function being called.

getArguments

```java
List
<? extends
ExpressionTree
> getArguments()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the list of arguments being passed to this function call.

**Returns:** the list of argument expressions

---

#### getArguments

List

<? extends

ExpressionTree

> getArguments()

Returns the list of arguments being passed to this function call.

---

