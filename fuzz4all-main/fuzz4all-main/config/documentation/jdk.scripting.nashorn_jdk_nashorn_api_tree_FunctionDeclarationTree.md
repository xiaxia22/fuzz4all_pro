# Interface FunctionDeclarationTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\FunctionDeclarationTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
FunctionDeclarationTree

extends
StatementTree
```

A tree node for a

function declaration

.

For example:

```java
function

name

(
parameters
)

body
```

```java
function*

name

(
parameters
)

body
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

#### BlockTree
getBody()

Returns the body of code of this function.

**Returns:**
- the body of code

---

#### boolean isStrict()

Is this a strict function?

**Returns:**
- true if this function is strict

---

#### boolean isGenerator()

Is this a generator function?

**Returns:**
- true if this is a generator function

---

### Additional Sections

#### Interface FunctionDeclarationTree

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
FunctionDeclarationTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for a

function declaration

.

For example:

```java
function

name

(
parameters
)

body
```

```java
function*

name

(
parameters
)

body
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

FunctionDeclarationTree

extends

StatementTree

A tree node for a

function declaration

.

For example:

```java
function

name

(
parameters
)

body
```

```java
function*

name

(
parameters
)

body
```

function

name

(

parameters

)

body

function*

name

(

parameters

)

body

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

BlockTree

getBody

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of code of this function.

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

BlockTree

getBody

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of code of this function.

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

Returns the body of code of this function.

Returns the name of the function being declared.

Returns the parameters of this function.

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
BlockTree
getBody()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of code of this function.

**Returns:** the body of code

- isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

**Returns:** true if this function is strict

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
BlockTree
getBody()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of code of this function.

**Returns:** the body of code

- isStrict

```java
boolean isStrict()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a strict function?

**Returns:** true if this function is strict

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
BlockTree
getBody()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the body of code of this function.

**Returns:** the body of code

---

#### getBody

BlockTree

getBody()

Returns the body of code of this function.

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

