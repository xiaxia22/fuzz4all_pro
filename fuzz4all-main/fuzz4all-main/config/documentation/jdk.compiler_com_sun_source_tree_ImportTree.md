# Interface ImportTree

**Source:** `jdk.compiler\com\sun\source\tree\ImportTree.html`

### Class Description

```java
public interface
ImportTree

extends
Tree
```

A tree node for an import declaration.

For example:

```java
import
qualifiedIdentifier
;

static import
qualifiedIdentifier
;
```

**All Superinterfaces:** Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isStatic()

Returns true if this is a static import declaration.

**Returns:**
- true if this is a static import

---

#### Tree
getQualifiedIdentifier()

Returns the qualified identifier for the declaration(s)
being imported.
If this is an import-on-demand declaration, the
qualified identifier will end in "*".

**Returns:**
- a qualified identifier, ending in "*" if and only if
this is an import-on-demand

---

### Additional Sections

#### Interface ImportTree

**All Superinterfaces:** Tree

```java
public interface
ImportTree

extends
Tree
```

A tree node for an import declaration.

For example:

```java
import
qualifiedIdentifier
;

static import
qualifiedIdentifier
;
```

**Since:** 1.6
**See The Java™ Language Specification :** section 7.5

public interface

ImportTree

extends

Tree

A tree node for an import declaration.

For example:

```java
import
qualifiedIdentifier
;

static import
qualifiedIdentifier
;
```

import

qualifiedIdentifier

;

static import

qualifiedIdentifier

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

Tree

getQualifiedIdentifier

()

Returns the qualified identifier for the declaration(s)
being imported.

boolean

isStatic

()

Returns true if this is a static import declaration.

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

getQualifiedIdentifier

()

Returns the qualified identifier for the declaration(s)
being imported.

boolean

isStatic

()

Returns true if this is a static import declaration.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the qualified identifier for the declaration(s)
being imported.

Returns true if this is a static import declaration.

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

Returns true if this is a static import declaration.

**Returns:** true if this is a static import

- getQualifiedIdentifier

```java
Tree
getQualifiedIdentifier()
```

Returns the qualified identifier for the declaration(s)
being imported.
If this is an import-on-demand declaration, the
qualified identifier will end in "*".

**Returns:** a qualified identifier, ending in "*" if and only if
this is an import-on-demand

Method Detail

- isStatic

```java
boolean isStatic()
```

Returns true if this is a static import declaration.

**Returns:** true if this is a static import

- getQualifiedIdentifier

```java
Tree
getQualifiedIdentifier()
```

Returns the qualified identifier for the declaration(s)
being imported.
If this is an import-on-demand declaration, the
qualified identifier will end in "*".

**Returns:** a qualified identifier, ending in "*" if and only if
this is an import-on-demand

---

#### Method Detail

isStatic

```java
boolean isStatic()
```

Returns true if this is a static import declaration.

**Returns:** true if this is a static import

---

#### isStatic

boolean isStatic()

Returns true if this is a static import declaration.

getQualifiedIdentifier

```java
Tree
getQualifiedIdentifier()
```

Returns the qualified identifier for the declaration(s)
being imported.
If this is an import-on-demand declaration, the
qualified identifier will end in "*".

**Returns:** a qualified identifier, ending in "*" if and only if
this is an import-on-demand

---

#### getQualifiedIdentifier

Tree

getQualifiedIdentifier()

Returns the qualified identifier for the declaration(s)
being imported.
If this is an import-on-demand declaration, the
qualified identifier will end in "*".

---

