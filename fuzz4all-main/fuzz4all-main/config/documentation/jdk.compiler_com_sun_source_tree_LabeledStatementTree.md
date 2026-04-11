# Interface LabeledStatementTree

**Source:** `jdk.compiler\com\sun\source\tree\LabeledStatementTree.html`

### Class Description

```java
public interface
LabeledStatementTree

extends
StatementTree
```

A tree node for a labeled statement.

For example:

```java
label
:
statement
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

Returns the label.

**Returns:**
- the label

---

#### StatementTree
getStatement()

Returns the statement that is labeled.

**Returns:**
- the statement

---

### Additional Sections

#### Interface LabeledStatementTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
LabeledStatementTree

extends
StatementTree
```

A tree node for a labeled statement.

For example:

```java
label
:
statement
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.7

public interface

LabeledStatementTree

extends

StatementTree

A tree node for a labeled statement.

For example:

```java
label
:
statement
```

label

:

statement

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

Returns the label.

StatementTree

getStatement

()

Returns the statement that is labeled.

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

Returns the label.

StatementTree

getStatement

()

Returns the statement that is labeled.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the label.

Returns the statement that is labeled.

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

Returns the label.

**Returns:** the label

- getStatement

```java
StatementTree
getStatement()
```

Returns the statement that is labeled.

**Returns:** the statement

Method Detail

- getLabel

```java
Name
getLabel()
```

Returns the label.

**Returns:** the label

- getStatement

```java
StatementTree
getStatement()
```

Returns the statement that is labeled.

**Returns:** the statement

---

#### Method Detail

getLabel

```java
Name
getLabel()
```

Returns the label.

**Returns:** the label

---

#### getLabel

Name

getLabel()

Returns the label.

getStatement

```java
StatementTree
getStatement()
```

Returns the statement that is labeled.

**Returns:** the statement

---

#### getStatement

StatementTree

getStatement()

Returns the statement that is labeled.

---

