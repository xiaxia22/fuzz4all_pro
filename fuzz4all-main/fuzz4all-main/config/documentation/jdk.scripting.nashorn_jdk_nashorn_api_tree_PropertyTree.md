# Interface PropertyTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\PropertyTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
PropertyTree

extends
Tree
```

To represent property setting in an object literal tree.

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ExpressionTree
getKey()

Returns the name of this property.

**Returns:**
- the name of the property

---

#### ExpressionTree
getValue()

Returns the value of this property. This is null for accessor properties.

**Returns:**
- the value of the property

---

#### FunctionExpressionTree
getGetter()

Returns the setter function of this property if this
is an accessor property. This is null for data properties.

**Returns:**
- the setter function of the property

---

#### FunctionExpressionTree
getSetter()

Returns the getter function of this property if this
is an accessor property. This is null for data properties.

**Returns:**
- the getter function of the property

---

#### boolean isStatic()

Is this a class static property?

**Returns:**
- true if this is a static property

---

#### boolean isComputed()

Is this a computed property?

**Returns:**
- true if this is a computed property

---

### Additional Sections

#### Interface PropertyTree

**All Superinterfaces:** Tree

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
PropertyTree

extends
Tree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

To represent property setting in an object literal tree.

**Since:** 9

@Deprecated

(

since

="11",

forRemoval

=true)
public interface

PropertyTree

extends

Tree

To represent property setting in an object literal tree.

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

FunctionExpressionTree

getGetter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the setter function of this property if this
is an accessor property.

ExpressionTree

getKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this property.

FunctionExpressionTree

getSetter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the getter function of this property if this
is an accessor property.

ExpressionTree

getValue

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the value of this property.

boolean

isComputed

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a computed property?

boolean

isStatic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a class static property?

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

FunctionExpressionTree

getGetter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the setter function of this property if this
is an accessor property.

ExpressionTree

getKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this property.

FunctionExpressionTree

getSetter

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the getter function of this property if this
is an accessor property.

ExpressionTree

getValue

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the value of this property.

boolean

isComputed

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a computed property?

boolean

isStatic

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a class static property?

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

Returns the setter function of this property if this
is an accessor property.

Returns the name of this property.

Returns the getter function of this property if this
is an accessor property.

Returns the value of this property.

Is this a computed property?

Is this a class static property?

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

- getKey

```java
ExpressionTree
getKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this property.

**Returns:** the name of the property

- getValue

```java
ExpressionTree
getValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the value of this property. This is null for accessor properties.

**Returns:** the value of the property

- getGetter

```java
FunctionExpressionTree
getGetter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the setter function of this property if this
is an accessor property. This is null for data properties.

**Returns:** the setter function of the property

- getSetter

```java
FunctionExpressionTree
getSetter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the getter function of this property if this
is an accessor property. This is null for data properties.

**Returns:** the getter function of the property

- isStatic

```java
boolean isStatic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a class static property?

**Returns:** true if this is a static property

- isComputed

```java
boolean isComputed()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a computed property?

**Returns:** true if this is a computed property

Method Detail

- getKey

```java
ExpressionTree
getKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this property.

**Returns:** the name of the property

- getValue

```java
ExpressionTree
getValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the value of this property. This is null for accessor properties.

**Returns:** the value of the property

- getGetter

```java
FunctionExpressionTree
getGetter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the setter function of this property if this
is an accessor property. This is null for data properties.

**Returns:** the setter function of the property

- getSetter

```java
FunctionExpressionTree
getSetter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the getter function of this property if this
is an accessor property. This is null for data properties.

**Returns:** the getter function of the property

- isStatic

```java
boolean isStatic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a class static property?

**Returns:** true if this is a static property

- isComputed

```java
boolean isComputed()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a computed property?

**Returns:** true if this is a computed property

---

#### Method Detail

getKey

```java
ExpressionTree
getKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of this property.

**Returns:** the name of the property

---

#### getKey

ExpressionTree

getKey()

Returns the name of this property.

getValue

```java
ExpressionTree
getValue()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the value of this property. This is null for accessor properties.

**Returns:** the value of the property

---

#### getValue

ExpressionTree

getValue()

Returns the value of this property. This is null for accessor properties.

getGetter

```java
FunctionExpressionTree
getGetter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the setter function of this property if this
is an accessor property. This is null for data properties.

**Returns:** the setter function of the property

---

#### getGetter

FunctionExpressionTree

getGetter()

Returns the setter function of this property if this
is an accessor property. This is null for data properties.

getSetter

```java
FunctionExpressionTree
getSetter()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the getter function of this property if this
is an accessor property. This is null for data properties.

**Returns:** the getter function of the property

---

#### getSetter

FunctionExpressionTree

getSetter()

Returns the getter function of this property if this
is an accessor property. This is null for data properties.

isStatic

```java
boolean isStatic()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a class static property?

**Returns:** true if this is a static property

---

#### isStatic

boolean isStatic()

Is this a class static property?

isComputed

```java
boolean isComputed()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a computed property?

**Returns:** true if this is a computed property

---

#### isComputed

boolean isComputed()

Is this a computed property?

---

