# Interface UsesTree

**Source:** `jdk.compiler\com\sun\source\doctree\UsesTree.html`

### Class Description

```java
public interface
UsesTree

extends
BlockTagTree
```

A tree node for an @uses block tag.

@uses service-type description

**All Superinterfaces:** BlockTagTree

,

DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ReferenceTree
getServiceType()

Returns the name of the service type being documented.

**Returns:**
- the name of the service type

---

#### List
<? extends
DocTree
> getDescription()

Returns a description of the use of service type within the module.

**Returns:**
- the description

---

### Additional Sections

#### Interface UsesTree

**All Superinterfaces:** BlockTagTree

,

DocTree

```java
public interface
UsesTree

extends
BlockTagTree
```

A tree node for an @uses block tag.

@uses service-type description

**Since:** 9

public interface

UsesTree

extends

BlockTagTree

A tree node for an @uses block tag.

@uses service-type description

@uses service-type description

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

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

DocTree

>

getDescription

()

Returns a description of the use of service type within the module.

ReferenceTree

getServiceType

()

Returns the name of the service type being documented.

- Methods declared in interface com.sun.source.doctree.

BlockTagTree

getTagName

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.doctree. DocTree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

DocTree

>

getDescription

()

Returns a description of the use of service type within the module.

ReferenceTree

getServiceType

()

Returns the name of the service type being documented.

- Methods declared in interface com.sun.source.doctree.

BlockTagTree

getTagName

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns a description of the use of service type within the module.

Returns the name of the service type being documented.

Methods declared in interface com.sun.source.doctree.

BlockTagTree

getTagName

---

#### Methods declared in interface com.sun.source.doctree. BlockTagTree

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getServiceType

```java
ReferenceTree
getServiceType()
```

Returns the name of the service type being documented.

**Returns:** the name of the service type

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns a description of the use of service type within the module.

**Returns:** the description

Method Detail

- getServiceType

```java
ReferenceTree
getServiceType()
```

Returns the name of the service type being documented.

**Returns:** the name of the service type

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns a description of the use of service type within the module.

**Returns:** the description

---

#### Method Detail

getServiceType

```java
ReferenceTree
getServiceType()
```

Returns the name of the service type being documented.

**Returns:** the name of the service type

---

#### getServiceType

ReferenceTree

getServiceType()

Returns the name of the service type being documented.

getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns a description of the use of service type within the module.

**Returns:** the description

---

#### getDescription

List

<? extends

DocTree

> getDescription()

Returns a description of the use of service type within the module.

---

