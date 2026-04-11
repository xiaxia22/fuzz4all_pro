# Interface WildcardTree

**Source:** `jdk.compiler\com\sun\source\tree\WildcardTree.html`

### Class Description

```java
public interface
WildcardTree

extends
Tree
```

A tree node for a wildcard type argument.
Use

getKind

to determine the kind of bound.

For example:

```java
?

? extends
bound

? super
bound
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Tree
getBound()

Returns the bound of the wildcard.

**Returns:**
- the bound

---

### Additional Sections

#### Interface WildcardTree

**All Superinterfaces:** Tree

```java
public interface
WildcardTree

extends
Tree
```

A tree node for a wildcard type argument.
Use

getKind

to determine the kind of bound.

For example:

```java
?

? extends
bound

? super
bound
```

**Since:** 1.6
**See The Java™ Language Specification :** section 4.5.1

public interface

WildcardTree

extends

Tree

A tree node for a wildcard type argument.
Use

getKind

to determine the kind of bound.

For example:

```java
?

? extends
bound

? super
bound
```

?

? extends

bound

? super

bound

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

Tree

getBound

()

Returns the bound of the wildcard.

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

Tree

getBound

()

Returns the bound of the wildcard.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the bound of the wildcard.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getBound

```java
Tree
getBound()
```

Returns the bound of the wildcard.

**Returns:** the bound

Method Detail

- getBound

```java
Tree
getBound()
```

Returns the bound of the wildcard.

**Returns:** the bound

---

#### Method Detail

getBound

```java
Tree
getBound()
```

Returns the bound of the wildcard.

**Returns:** the bound

---

#### getBound

Tree

getBound()

Returns the bound of the wildcard.

---

