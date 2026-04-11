# Interface ClassDeclarationTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\ClassDeclarationTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
ClassDeclarationTree

extends
StatementTree
```

A tree node that represents a

class declaration

.

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

Class identifier.

**Returns:**
- the class identifier

---

#### ExpressionTree
getClassHeritage()

The expression of the

extends

clause. Optional.

**Returns:**
- the class heritage

---

#### PropertyTree
getConstructor()

Get the constructor method definition.

**Returns:**
- the constructor

---

#### List
<? extends
PropertyTree
> getClassElements()

Get other property definitions except for the constructor.

**Returns:**
- the class elements

---

### Additional Sections

#### Interface ClassDeclarationTree

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
ClassDeclarationTree

extends
StatementTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node that represents a

class declaration

.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

ClassDeclarationTree

extends

StatementTree

A tree node that represents a

class declaration

.

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

PropertyTree

>

getClassElements

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get other property definitions except for the constructor.

ExpressionTree

getClassHeritage

()

Deprecated, for removal: This API element is subject to removal in a future version.

The expression of the

extends

clause.

PropertyTree

getConstructor

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the constructor method definition.

IdentifierTree

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Class identifier.

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

PropertyTree

>

getClassElements

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get other property definitions except for the constructor.

ExpressionTree

getClassHeritage

()

Deprecated, for removal: This API element is subject to removal in a future version.

The expression of the

extends

clause.

PropertyTree

getConstructor

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the constructor method definition.

IdentifierTree

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Class identifier.

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

Get other property definitions except for the constructor.

The expression of the

extends

clause.

Get the constructor method definition.

Class identifier.

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

Class identifier.

**Returns:** the class identifier

- getClassHeritage

```java
ExpressionTree
getClassHeritage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The expression of the

extends

clause. Optional.

**Returns:** the class heritage

- getConstructor

```java
PropertyTree
getConstructor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the constructor method definition.

**Returns:** the constructor

- getClassElements

```java
List
<? extends
PropertyTree
> getClassElements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get other property definitions except for the constructor.

**Returns:** the class elements

Method Detail

- getName

```java
IdentifierTree
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Class identifier.

**Returns:** the class identifier

- getClassHeritage

```java
ExpressionTree
getClassHeritage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The expression of the

extends

clause. Optional.

**Returns:** the class heritage

- getConstructor

```java
PropertyTree
getConstructor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the constructor method definition.

**Returns:** the constructor

- getClassElements

```java
List
<? extends
PropertyTree
> getClassElements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get other property definitions except for the constructor.

**Returns:** the class elements

---

#### Method Detail

getName

```java
IdentifierTree
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Class identifier.

**Returns:** the class identifier

---

#### getName

IdentifierTree

getName()

Class identifier.

getClassHeritage

```java
ExpressionTree
getClassHeritage()
```

Deprecated, for removal: This API element is subject to removal in a future version.

The expression of the

extends

clause. Optional.

**Returns:** the class heritage

---

#### getClassHeritage

ExpressionTree

getClassHeritage()

The expression of the

extends

clause. Optional.

getConstructor

```java
PropertyTree
getConstructor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the constructor method definition.

**Returns:** the constructor

---

#### getConstructor

PropertyTree

getConstructor()

Get the constructor method definition.

getClassElements

```java
List
<? extends
PropertyTree
> getClassElements()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get other property definitions except for the constructor.

**Returns:** the class elements

---

#### getClassElements

List

<? extends

PropertyTree

> getClassElements()

Get other property definitions except for the constructor.

---

