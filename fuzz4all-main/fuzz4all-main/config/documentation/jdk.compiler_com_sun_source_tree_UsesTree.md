# Interface UsesTree

**Source:** `jdk.compiler\com\sun\source\tree\UsesTree.html`

### Class Description

```java
public interface
UsesTree

extends
DirectiveTree
```

A tree node for a 'uses' directive in a module declaration.

For example:

```java
uses
service-name
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

#### ExpressionTree
getServiceName()

Returns the name of the service type.

**Returns:**
- the name of the service type

---

### Additional Sections

#### Interface UsesTree

**All Superinterfaces:** DirectiveTree

,

Tree

```java
public interface
UsesTree

extends
DirectiveTree
```

A tree node for a 'uses' directive in a module declaration.

For example:

```java
uses
service-name
;
```

**Since:** 9

public interface

UsesTree

extends

DirectiveTree

A tree node for a 'uses' directive in a module declaration.

For example:

```java
uses
service-name
;
```

uses

service-name

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

getServiceName

()

Returns the name of the service type.

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

getServiceName

()

Returns the name of the service type.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the name of the service type.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getServiceName

```java
ExpressionTree
getServiceName()
```

Returns the name of the service type.

**Returns:** the name of the service type

Method Detail

- getServiceName

```java
ExpressionTree
getServiceName()
```

Returns the name of the service type.

**Returns:** the name of the service type

---

#### Method Detail

getServiceName

```java
ExpressionTree
getServiceName()
```

Returns the name of the service type.

**Returns:** the name of the service type

---

#### getServiceName

ExpressionTree

getServiceName()

Returns the name of the service type.

---

