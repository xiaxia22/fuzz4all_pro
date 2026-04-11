# Interface ContinueTree

**Source:** `jdk.compiler\com\sun\source\tree\ContinueTree.html`

### Class Description

```java
public interface
ContinueTree

extends
StatementTree
```

A tree node for a

continue

statement.

For example:

```java
continue;
continue
label
;
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

#### Name
getLabel()

Returns the label for this

continue

statement.

**Returns:**
- the label

---

### Additional Sections

#### Interface ContinueTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
ContinueTree

extends
StatementTree
```

A tree node for a

continue

statement.

For example:

```java
continue;
continue
label
;
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.16

public interface

ContinueTree

extends

StatementTree

A tree node for a

continue

statement.

For example:

```java
continue;
continue
label
;
```

continue;
continue

label

;

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

Name

getLabel

()

Returns the label for this

continue

statement.

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

Name

getLabel

()

Returns the label for this

continue

statement.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the label for this

continue

statement.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getLabel

```java
Name
getLabel()
```

Returns the label for this

continue

statement.

**Returns:** the label

Method Detail

- getLabel

```java
Name
getLabel()
```

Returns the label for this

continue

statement.

**Returns:** the label

---

#### Method Detail

getLabel

```java
Name
getLabel()
```

Returns the label for this

continue

statement.

**Returns:** the label

---

#### getLabel

Name

getLabel()

Returns the label for this

continue

statement.

---

