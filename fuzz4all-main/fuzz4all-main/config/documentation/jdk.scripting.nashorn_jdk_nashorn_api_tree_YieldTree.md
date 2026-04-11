# Interface YieldTree

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\YieldTree.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public interface
YieldTree

extends
ExpressionTree
```

A tree node for

yield expressions

used in generator functions.

For example:

```java
function*
id(){
var index = 0;
while(index < 10)

yield index++;

}
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
getExpression()

Returns the expression that is yielded.

**Returns:**
- The expression that is yielded.

---

#### boolean isStar()

Is this a yield * expression in a generator function?

For example:

```java
function* id(){
yield 1;

yield * anotherGeneratorFunc();

yield 10;
}
```

**Returns:**
- true if this is a yield * expression

---

### Additional Sections

#### Interface YieldTree

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
YieldTree

extends
ExpressionTree
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A tree node for

yield expressions

used in generator functions.

For example:

```java
function*
id(){
var index = 0;
while(index < 10)

yield index++;

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

YieldTree

extends

ExpressionTree

A tree node for

yield expressions

used in generator functions.

For example:

```java
function*
id(){
var index = 0;
while(index < 10)

yield index++;

}
```

function*

id(){
var index = 0;
while(index < 10)

yield index++;

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

ExpressionTree

getExpression

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression that is yielded.

boolean

isStar

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a yield * expression in a generator function?

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

Returns the expression that is yielded.

boolean

isStar

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a yield * expression in a generator function?

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

Returns the expression that is yielded.

Is this a yield * expression in a generator function?

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

Returns the expression that is yielded.

**Returns:** The expression that is yielded.

- isStar

```java
boolean isStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a yield * expression in a generator function?

For example:

```java
function* id(){
yield 1;

yield * anotherGeneratorFunc();

yield 10;
}
```

**Returns:** true if this is a yield * expression

Method Detail

- getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression that is yielded.

**Returns:** The expression that is yielded.

- isStar

```java
boolean isStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a yield * expression in a generator function?

For example:

```java
function* id(){
yield 1;

yield * anotherGeneratorFunc();

yield 10;
}
```

**Returns:** true if this is a yield * expression

---

#### Method Detail

getExpression

```java
ExpressionTree
getExpression()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the expression that is yielded.

**Returns:** The expression that is yielded.

---

#### getExpression

ExpressionTree

getExpression()

Returns the expression that is yielded.

isStar

```java
boolean isStar()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this a yield * expression in a generator function?

For example:

```java
function* id(){
yield 1;

yield * anotherGeneratorFunc();

yield 10;
}
```

**Returns:** true if this is a yield * expression

---

#### isStar

boolean isStar()

Is this a yield * expression in a generator function?

For example:

```java
function* id(){
yield 1;

yield * anotherGeneratorFunc();

yield 10;
}
```

function* id(){
yield 1;

yield * anotherGeneratorFunc();

yield 10;
}

---

