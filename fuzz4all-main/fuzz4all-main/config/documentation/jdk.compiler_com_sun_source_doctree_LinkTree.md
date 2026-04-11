# Interface LinkTree

**Source:** `jdk.compiler\com\sun\source\doctree\LinkTree.html`

### Class Description

```java
public interface
LinkTree

extends
InlineTagTree
```

A tree node for an @link or @linkplain inline tag.

{@link reference label}

{@linkplain reference label }

**All Superinterfaces:** DocTree

,

InlineTagTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ReferenceTree
getReference()

Returns the reference of a link.

**Returns:**
- the reference

---

#### List
<? extends
DocTree
> getLabel()

Returns the label, if any, of the link.

**Returns:**
- the label

---

### Additional Sections

#### Interface LinkTree

**All Superinterfaces:** DocTree

,

InlineTagTree

```java
public interface
LinkTree

extends
InlineTagTree
```

A tree node for an @link or @linkplain inline tag.

{@link reference label}

{@linkplain reference label }

**Since:** 1.8

public interface

LinkTree

extends

InlineTagTree

A tree node for an @link or @linkplain inline tag.

{@link reference label}

{@linkplain reference label }

{@link reference label}

{@linkplain reference label }

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

getLabel

()

Returns the label, if any, of the link.

ReferenceTree

getReference

()

Returns the reference of a link.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

- Methods declared in interface com.sun.source.doctree.

InlineTagTree

getTagName

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

getLabel

()

Returns the label, if any, of the link.

ReferenceTree

getReference

()

Returns the reference of a link.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

- Methods declared in interface com.sun.source.doctree.

InlineTagTree

getTagName

---

#### Method Summary

Returns the label, if any, of the link.

Returns the reference of a link.

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

Methods declared in interface com.sun.source.doctree.

InlineTagTree

getTagName

---

#### Methods declared in interface com.sun.source.doctree. InlineTagTree

============ METHOD DETAIL ==========

- Method Detail

- getReference

```java
ReferenceTree
getReference()
```

Returns the reference of a link.

**Returns:** the reference

- getLabel

```java
List
<? extends
DocTree
> getLabel()
```

Returns the label, if any, of the link.

**Returns:** the label

Method Detail

- getReference

```java
ReferenceTree
getReference()
```

Returns the reference of a link.

**Returns:** the reference

- getLabel

```java
List
<? extends
DocTree
> getLabel()
```

Returns the label, if any, of the link.

**Returns:** the label

---

#### Method Detail

getReference

```java
ReferenceTree
getReference()
```

Returns the reference of a link.

**Returns:** the reference

---

#### getReference

ReferenceTree

getReference()

Returns the reference of a link.

getLabel

```java
List
<? extends
DocTree
> getLabel()
```

Returns the label, if any, of the link.

**Returns:** the label

---

#### getLabel

List

<? extends

DocTree

> getLabel()

Returns the label, if any, of the link.

---

