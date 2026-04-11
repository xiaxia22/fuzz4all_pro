# Interface ProvidesTree

**Source:** `jdk.compiler\com\sun\source\tree\ProvidesTree.html`

### Class Description

```java
public interface
ProvidesTree

extends
DirectiveTree
```

A tree node for a 'provides' directive in a module declaration.

For example:

```java
provides
service-name
with
implementation-name
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

Returns the name of the service type being provided.

**Returns:**
- the name of the service type being provided

---

#### List
<? extends
ExpressionTree
> getImplementationNames()

Returns the names of the implementation types being provided.

**Returns:**
- the names of the implementation types being provided

---

### Additional Sections

#### Interface ProvidesTree

**All Superinterfaces:** DirectiveTree

,

Tree

```java
public interface
ProvidesTree

extends
DirectiveTree
```

A tree node for a 'provides' directive in a module declaration.

For example:

```java
provides
service-name
with
implementation-name
;
```

**Since:** 9

public interface

ProvidesTree

extends

DirectiveTree

A tree node for a 'provides' directive in a module declaration.

For example:

```java
provides
service-name
with
implementation-name
;
```

provides

service-name

with

implementation-name

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

List

<? extends

ExpressionTree

>

getImplementationNames

()

Returns the names of the implementation types being provided.

ExpressionTree

getServiceName

()

Returns the name of the service type being provided.

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

ExpressionTree

>

getImplementationNames

()

Returns the names of the implementation types being provided.

ExpressionTree

getServiceName

()

Returns the name of the service type being provided.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the names of the implementation types being provided.

Returns the name of the service type being provided.

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

Returns the name of the service type being provided.

**Returns:** the name of the service type being provided

- getImplementationNames

```java
List
<? extends
ExpressionTree
> getImplementationNames()
```

Returns the names of the implementation types being provided.

**Returns:** the names of the implementation types being provided

Method Detail

- getServiceName

```java
ExpressionTree
getServiceName()
```

Returns the name of the service type being provided.

**Returns:** the name of the service type being provided

- getImplementationNames

```java
List
<? extends
ExpressionTree
> getImplementationNames()
```

Returns the names of the implementation types being provided.

**Returns:** the names of the implementation types being provided

---

#### Method Detail

getServiceName

```java
ExpressionTree
getServiceName()
```

Returns the name of the service type being provided.

**Returns:** the name of the service type being provided

---

#### getServiceName

ExpressionTree

getServiceName()

Returns the name of the service type being provided.

getImplementationNames

```java
List
<? extends
ExpressionTree
> getImplementationNames()
```

Returns the names of the implementation types being provided.

**Returns:** the names of the implementation types being provided

---

#### getImplementationNames

List

<? extends

ExpressionTree

> getImplementationNames()

Returns the names of the implementation types being provided.

---

