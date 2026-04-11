# Interface AttributeTree

**Source:** `jdk.compiler\com\sun\source\doctree\AttributeTree.html`

### Class Description

```java
public interface
AttributeTree

extends
DocTree
```

A tree node for an attribute in an HTML element.

**All Superinterfaces:** DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Name
getName()

Returns the name of the attribute.

**Returns:**
- the name of the attribute

---

#### AttributeTree.ValueKind
getValueKind()

Returns the kind of the attribute.

**Returns:**
- the kind of the attribute.

---

#### List
<? extends
DocTree
> getValue()

Returns the value of the attribute, or

null

if the kind is EMPTY.

**Returns:**
- the value of the attribute.

---

### Additional Sections

#### Interface AttributeTree

**All Superinterfaces:** DocTree

```java
public interface
AttributeTree

extends
DocTree
```

A tree node for an attribute in an HTML element.

**Since:** 1.8

public interface

AttributeTree

extends

DocTree

A tree node for an attribute in an HTML element.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

AttributeTree.ValueKind

The kind of an attribute value.

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

Name

getName

()

Returns the name of the attribute.

List

<? extends

DocTree

>

getValue

()

Returns the value of the attribute, or

null

if the kind is EMPTY.

AttributeTree.ValueKind

getValueKind

()

Returns the kind of the attribute.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

AttributeTree.ValueKind

The kind of an attribute value.

- Nested classes/interfaces declared in interface com.sun.source.doctree.

DocTree

DocTree.Kind

---

#### Nested Class Summary

The kind of an attribute value.

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

Name

getName

()

Returns the name of the attribute.

List

<? extends

DocTree

>

getValue

()

Returns the value of the attribute, or

null

if the kind is EMPTY.

AttributeTree.ValueKind

getValueKind

()

Returns the kind of the attribute.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns the name of the attribute.

Returns the value of the attribute, or

null

if the kind is EMPTY.

Returns the kind of the attribute.

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
Name
getName()
```

Returns the name of the attribute.

**Returns:** the name of the attribute

- getValueKind

```java
AttributeTree.ValueKind
getValueKind()
```

Returns the kind of the attribute.

**Returns:** the kind of the attribute.

- getValue

```java
List
<? extends
DocTree
> getValue()
```

Returns the value of the attribute, or

null

if the kind is EMPTY.

**Returns:** the value of the attribute.

Method Detail

- getName

```java
Name
getName()
```

Returns the name of the attribute.

**Returns:** the name of the attribute

- getValueKind

```java
AttributeTree.ValueKind
getValueKind()
```

Returns the kind of the attribute.

**Returns:** the kind of the attribute.

- getValue

```java
List
<? extends
DocTree
> getValue()
```

Returns the value of the attribute, or

null

if the kind is EMPTY.

**Returns:** the value of the attribute.

---

#### Method Detail

getName

```java
Name
getName()
```

Returns the name of the attribute.

**Returns:** the name of the attribute

---

#### getName

Name

getName()

Returns the name of the attribute.

getValueKind

```java
AttributeTree.ValueKind
getValueKind()
```

Returns the kind of the attribute.

**Returns:** the kind of the attribute.

---

#### getValueKind

AttributeTree.ValueKind

getValueKind()

Returns the kind of the attribute.

getValue

```java
List
<? extends
DocTree
> getValue()
```

Returns the value of the attribute, or

null

if the kind is EMPTY.

**Returns:** the value of the attribute.

---

#### getValue

List

<? extends

DocTree

> getValue()

Returns the value of the attribute, or

null

if the kind is EMPTY.

---

