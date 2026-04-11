# Interface FunctionExpressionTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\FunctionExpressionTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
FunctionExpressionTree

extends
ExpressionTree
```

A tree node for

function expressions

including

arrow functions

.

For example:

```java
var
func =
function

(
parameters
)

body
```

```java
var
func =
(x) => x+1
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

#### IdentifierTree
getName()

Returns the name of the function being declared.

**Returns:**
- name the function declared

---

#### List
<? extends
ExpressionTree
> getParameters()

Returns the parameters of this function.

**Returns:**
- the list of parameters

---

#### Tree
getBody()

Returns the body of this function. This may be a

BlockTree

when this
function has a block body. This is an

ExpressionTree

when the function body
is a concise expression as in an expression arrow, or in an expression closure.

**Returns:**
- the body of this function

---

#### boolean isStrict()

Is this a strict function?

**Returns:**
- true if this function is strict

---

#### boolean isArrow()

Is this a arrow function?

**Returns:**
- true if this is a arrow function

---

#### boolean isGenerator()

Is this a generator function?

**Returns:**
- true if this is a generator function

---

### Additional Sections

#### Interface FunctionExpressionTree

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
FunctionExpressionTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for

function expressions

including

arrow functions

.

For example:

```java
var
func =
function

(
parameters
)

body
```

```java
var
func =
(x) => x+1
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

FunctionExpressionTree

extends

ExpressionTree

A tree node for

function expressions

including

arrow functions

.

For example:

```java
var
func =
function

(
parameters
)

body
```

```java
var
func =
(x) => x+1
```

var

func =

function

(

parameters

)

body

var

func =

(x) => x+1

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

Tree

getBody

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of this function.

IdentifierTree

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the function being declared.

List

<? extends

ExpressionTree

>

getParameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the parameters of this function.

boolean

isArrow

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a arrow function?

boolean

isGenerator

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a generator function?

boolean

isStrict

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

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

Tree

getBody

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of this function.

IdentifierTree

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the function being declared.

List

<? extends

ExpressionTree

>

getParameters

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the parameters of this function.

boolean

isArrow

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a arrow function?

boolean

isGenerator

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a generator function?

boolean

isStrict

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

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

Returns the body of this function.

Returns the name of the function being declared.

Returns the parameters of this function.

Is this a arrow function?

Is this a generator function?

Is this a strict function?

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

- getName

```java
IdentifierTree
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the function being declared.

**Returns:** name the function declared

- getParameters

```java
List
<? extends
ExpressionTree
> getParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the parameters of this function.

**Returns:** the list of parameters

- getBody

```java
Tree
getBody()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of this function. This may be a

BlockTree

when this
function has a block body. This is an

ExpressionTree

when the function body
is a concise expression as in an expression arrow, or in an expression closure.

**Returns:** the body of this function

- isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

**Returns:** true if this function is strict

- isArrow

```java
boolean isArrow()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a arrow function?

**Returns:** true if this is a arrow function

- isGenerator

```java
boolean isGenerator()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a generator function?

**Returns:** true if this is a generator function

Method Detail

- getName

```java
IdentifierTree
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the function being declared.

**Returns:** name the function declared

- getParameters

```java
List
<? extends
ExpressionTree
> getParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the parameters of this function.

**Returns:** the list of parameters

- getBody

```java
Tree
getBody()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of this function. This may be a

BlockTree

when this
function has a block body. This is an

ExpressionTree

when the function body
is a concise expression as in an expression arrow, or in an expression closure.

**Returns:** the body of this function

- isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

**Returns:** true if this function is strict

- isArrow

```java
boolean isArrow()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a arrow function?

**Returns:** true if this is a arrow function

- isGenerator

```java
boolean isGenerator()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a generator function?

**Returns:** true if this is a generator function

---

#### Method Detail

getName

```java
IdentifierTree
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the function being declared.

**Returns:** name the function declared

---

#### getName

IdentifierTree

getName()

Returns the name of the function being declared.

getParameters

```java
List
<? extends
ExpressionTree
> getParameters()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the parameters of this function.

**Returns:** the list of parameters

---

#### getParameters

List

<? extends

ExpressionTree

> getParameters()

Returns the parameters of this function.

getBody

```java
Tree
getBody()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of this function. This may be a

BlockTree

when this
function has a block body. This is an

ExpressionTree

when the function body
is a concise expression as in an expression arrow, or in an expression closure.

**Returns:** the body of this function

---

#### getBody

Tree

getBody()

Returns the body of this function. This may be a

BlockTree

when this
function has a block body. This is an

ExpressionTree

when the function body
is a concise expression as in an expression arrow, or in an expression closure.

isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

**Returns:** true if this function is strict

---

#### isStrict

boolean isStrict()

Is this a strict function?

isArrow

```java
boolean isArrow()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a arrow function?

**Returns:** true if this is a arrow function

---

#### isArrow

boolean isArrow()

Is this a arrow function?

isGenerator

```java
boolean isGenerator()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a generator function?

**Returns:** true if this is a generator function

---

#### isGenerator

boolean isGenerator()

Is this a generator function?

---

