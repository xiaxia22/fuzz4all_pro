# Interface RequiresTree

**Source:** `jdk.compiler\com\sun\source\tree\RequiresTree.html`

### Class Description

```java
public interface
RequiresTree

extends
DirectiveTree
```

A tree node for a 'requires' directive in a module declaration.

For example:

```java
requires
module-name
;
requires static
module-name
;
requires transitive
module-name
;
```

**All Superinterfaces:** DirectiveTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isStatic()

Returns true if this is a "requires static" directive.

**Returns:**
- true if this is a "requires static" directive

---

#### boolean isTransitive()

Returns true if this is a "requires transitive" directive.

**Returns:**
- true if this is a "requires transitive" directive

---

#### ExpressionTree
getModuleName()

Returns the name of the module that is required.

**Returns:**
- the name of the module that is required

---

### Additional Sections

#### Interface RequiresTree

**All Superinterfaces:** DirectiveTree

,

Tree

```java
public interface
RequiresTree

extends
DirectiveTree
```

A tree node for a 'requires' directive in a module declaration.

For example:

```java
requires
module-name
;
requires static
module-name
;
requires transitive
module-name
;
```

**Since:** 9

public interface

RequiresTree

extends

DirectiveTree

A tree node for a 'requires' directive in a module declaration.

For example:

```java
requires
module-name
;
requires static
module-name
;
requires transitive
module-name
;
```

requires

module-name

;
requires static

module-name

;
requires transitive

module-name

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

ExpressionTree

getModuleName

()

Returns the name of the module that is required.

boolean

isStatic

()

Returns true if this is a "requires static" directive.

boolean

isTransitive

()

Returns true if this is a "requires transitive" directive.

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

ExpressionTree

getModuleName

()

Returns the name of the module that is required.

boolean

isStatic

()

Returns true if this is a "requires static" directive.

boolean

isTransitive

()

Returns true if this is a "requires transitive" directive.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the name of the module that is required.

Returns true if this is a "requires static" directive.

Returns true if this is a "requires transitive" directive.

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

Returns true if this is a "requires static" directive.

**Returns:** true if this is a "requires static" directive

- isTransitive

```java
boolean isTransitive()
```

Returns true if this is a "requires transitive" directive.

**Returns:** true if this is a "requires transitive" directive

- getModuleName

```java
ExpressionTree
getModuleName()
```

Returns the name of the module that is required.

**Returns:** the name of the module that is required

Method Detail

- isStatic

```java
boolean isStatic()
```

Returns true if this is a "requires static" directive.

**Returns:** true if this is a "requires static" directive

- isTransitive

```java
boolean isTransitive()
```

Returns true if this is a "requires transitive" directive.

**Returns:** true if this is a "requires transitive" directive

- getModuleName

```java
ExpressionTree
getModuleName()
```

Returns the name of the module that is required.

**Returns:** the name of the module that is required

---

#### Method Detail

isStatic

```java
boolean isStatic()
```

Returns true if this is a "requires static" directive.

**Returns:** true if this is a "requires static" directive

---

#### isStatic

boolean isStatic()

Returns true if this is a "requires static" directive.

isTransitive

```java
boolean isTransitive()
```

Returns true if this is a "requires transitive" directive.

**Returns:** true if this is a "requires transitive" directive

---

#### isTransitive

boolean isTransitive()

Returns true if this is a "requires transitive" directive.

getModuleName

```java
ExpressionTree
getModuleName()
```

Returns the name of the module that is required.

**Returns:** the name of the module that is required

---

#### getModuleName

ExpressionTree

getModuleName()

Returns the name of the module that is required.

---

