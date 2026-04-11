# Interface BlockTree

**Source:** `jdk.compiler\com\sun\source\tree\BlockTree.html`

### Class Description

```java
public interface
BlockTree

extends
StatementTree
```

A tree node for a statement block.

For example:

```java
{ }

{
statements
}

static {
statements
}
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

#### boolean isStatic()

Returns true if and only if this is a static initializer block.

**Returns:**
- true if this is a static initializer block

---

#### List
<? extends
StatementTree
> getStatements()

Returns the statements comprising this block.

**Returns:**
- the statements

---

### Additional Sections

#### Interface BlockTree

**All Superinterfaces:** StatementTree

,

Tree

```java
public interface
BlockTree

extends
StatementTree
```

A tree node for a statement block.

For example:

```java
{ }

{
statements
}

static {
statements
}
```

**Since:** 1.6
**See The Java™ Language Specification :** section 14.2

public interface

BlockTree

extends

StatementTree

A tree node for a statement block.

For example:

```java
{ }

{
statements
}

static {
statements
}
```

{ }

{

statements

}

static {

statements

}

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

List

<? extends

StatementTree

>

getStatements

()

Returns the statements comprising this block.

boolean

isStatic

()

Returns true if and only if this is a static initializer block.

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

List

<? extends

StatementTree

>

getStatements

()

Returns the statements comprising this block.

boolean

isStatic

()

Returns true if and only if this is a static initializer block.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the statements comprising this block.

Returns true if and only if this is a static initializer block.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- isStatic

```java
boolean isStatic()
```

Returns true if and only if this is a static initializer block.

**Returns:** true if this is a static initializer block

- getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Returns the statements comprising this block.

**Returns:** the statements

Method Detail

- isStatic

```java
boolean isStatic()
```

Returns true if and only if this is a static initializer block.

**Returns:** true if this is a static initializer block

- getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Returns the statements comprising this block.

**Returns:** the statements

---

#### Method Detail

isStatic

```java
boolean isStatic()
```

Returns true if and only if this is a static initializer block.

**Returns:** true if this is a static initializer block

---

#### isStatic

boolean isStatic()

Returns true if and only if this is a static initializer block.

getStatements

```java
List
<? extends
StatementTree
> getStatements()
```

Returns the statements comprising this block.

**Returns:** the statements

---

#### getStatements

List

<? extends

StatementTree

> getStatements()

Returns the statements comprising this block.

---

