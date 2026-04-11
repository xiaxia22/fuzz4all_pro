# Interface IdentifierTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\IdentifierTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
IdentifierTree

extends
ExpressionTree
```

A tree node for an identifier expression.

For example:

```java
name
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

#### String
getName()

Returns the name of this identifier.

**Returns:**
- the name of this identifier

---

#### boolean isRestParameter()

Is this a rest parameter for a function or rest elements of an array?

**Returns:**
- true if this is a rest parameter

---

#### boolean isSuper()

Is this super identifier?

**Returns:**
- true if this is super identifier

---

#### boolean isThis()

Is this 'this' identifier?

**Returns:**
- true if this is 'this' identifier

---

#### boolean isStar()

Is this "*" used in module export entry?

**Returns:**
- true if this "*" used in module export entry?

---

#### boolean isDefault()

Is this "default" used in module export entry?

**Returns:**
- true if this 'default' used in module export entry?

---

#### boolean isStarDefaultStar()

Is this "*default*" used in module export entry?

**Returns:**
- true if this '*default*' used in module export entry?

---

### Additional Sections

#### Interface IdentifierTree

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
IdentifierTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for an identifier expression.

For example:

```java
name
```

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

IdentifierTree

extends

ExpressionTree

A tree node for an identifier expression.

For example:

```java
name
```

name

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

String

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this identifier.

boolean

isDefault

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "default" used in module export entry?

boolean

isRestParameter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a rest parameter for a function or rest elements of an array?

boolean

isStar

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*" used in module export entry?

boolean

isStarDefaultStar

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*default*" used in module export entry?

boolean

isSuper

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this super identifier?

boolean

isThis

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this 'this' identifier?

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

String

getName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this identifier.

boolean

isDefault

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "default" used in module export entry?

boolean

isRestParameter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a rest parameter for a function or rest elements of an array?

boolean

isStar

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*" used in module export entry?

boolean

isStarDefaultStar

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*default*" used in module export entry?

boolean

isSuper

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this super identifier?

boolean

isThis

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this 'this' identifier?

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

Returns the name of this identifier.

Is this "default" used in module export entry?

Is this a rest parameter for a function or rest elements of an array?

Is this "*" used in module export entry?

Is this "*default*" used in module export entry?

Is this super identifier?

Is this 'this' identifier?

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
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this identifier.

**Returns:** the name of this identifier

- isRestParameter

```java
boolean isRestParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a rest parameter for a function or rest elements of an array?

**Returns:** true if this is a rest parameter

- isSuper

```java
boolean isSuper()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this super identifier?

**Returns:** true if this is super identifier

- isThis

```java
boolean isThis()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this 'this' identifier?

**Returns:** true if this is 'this' identifier

- isStar

```java
boolean isStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*" used in module export entry?

**Returns:** true if this "*" used in module export entry?

- isDefault

```java
boolean isDefault()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "default" used in module export entry?

**Returns:** true if this 'default' used in module export entry?

- isStarDefaultStar

```java
boolean isStarDefaultStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*default*" used in module export entry?

**Returns:** true if this '*default*' used in module export entry?

Method Detail

- getName

```java
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this identifier.

**Returns:** the name of this identifier

- isRestParameter

```java
boolean isRestParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a rest parameter for a function or rest elements of an array?

**Returns:** true if this is a rest parameter

- isSuper

```java
boolean isSuper()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this super identifier?

**Returns:** true if this is super identifier

- isThis

```java
boolean isThis()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this 'this' identifier?

**Returns:** true if this is 'this' identifier

- isStar

```java
boolean isStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*" used in module export entry?

**Returns:** true if this "*" used in module export entry?

- isDefault

```java
boolean isDefault()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "default" used in module export entry?

**Returns:** true if this 'default' used in module export entry?

- isStarDefaultStar

```java
boolean isStarDefaultStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*default*" used in module export entry?

**Returns:** true if this '*default*' used in module export entry?

---

#### Method Detail

getName

```java
String
getName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this identifier.

**Returns:** the name of this identifier

---

#### getName

String

getName()

Returns the name of this identifier.

isRestParameter

```java
boolean isRestParameter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a rest parameter for a function or rest elements of an array?

**Returns:** true if this is a rest parameter

---

#### isRestParameter

boolean isRestParameter()

Is this a rest parameter for a function or rest elements of an array?

isSuper

```java
boolean isSuper()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this super identifier?

**Returns:** true if this is super identifier

---

#### isSuper

boolean isSuper()

Is this super identifier?

isThis

```java
boolean isThis()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this 'this' identifier?

**Returns:** true if this is 'this' identifier

---

#### isThis

boolean isThis()

Is this 'this' identifier?

isStar

```java
boolean isStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*" used in module export entry?

**Returns:** true if this "*" used in module export entry?

---

#### isStar

boolean isStar()

Is this "*" used in module export entry?

isDefault

```java
boolean isDefault()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "default" used in module export entry?

**Returns:** true if this 'default' used in module export entry?

---

#### isDefault

boolean isDefault()

Is this "default" used in module export entry?

isStarDefaultStar

```java
boolean isStarDefaultStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this "*default*" used in module export entry?

**Returns:** true if this '*default*' used in module export entry?

---

#### isStarDefaultStar

boolean isStarDefaultStar()

Is this "*default*" used in module export entry?

---

