# Interface SerialFieldTree

**Source:** `jdk.compiler\com\sun\source\doctree\SerialFieldTree.html`

### Class Description

```java
public interface
SerialFieldTree

extends
BlockTagTree
```

A tree node for an @serialData block tag.

@serialField field-name field-type field-description

**All Superinterfaces:** BlockTagTree

,

DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### IdentifierTree
getName()

Returns the name of the serial field.

**Returns:**
- the name of the serial field

---

#### ReferenceTree
getType()

Returns the type of the serial field.

**Returns:**
- the type of the serial field

---

#### List
<? extends
DocTree
> getDescription()

Returns the description of the serial field.

**Returns:**
- the description of the serial field

---

### Additional Sections

#### Interface SerialFieldTree

**All Superinterfaces:** BlockTagTree

,

DocTree

```java
public interface
SerialFieldTree

extends
BlockTagTree
```

A tree node for an @serialData block tag.

@serialField field-name field-type field-description

**Since:** 1.8

public interface

SerialFieldTree

extends

BlockTagTree

A tree node for an @serialData block tag.

@serialField field-name field-type field-description

@serialField field-name field-type field-description

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

Returns the description of the serial field.

IdentifierTree

getName

()

Returns the name of the serial field.

ReferenceTree

getType

()

Returns the type of the serial field.

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

Returns the description of the serial field.

IdentifierTree

getName

()

Returns the name of the serial field.

ReferenceTree

getType

()

Returns the type of the serial field.

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

Returns the description of the serial field.

Returns the name of the serial field.

Returns the type of the serial field.

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

- getName

```java
IdentifierTree
getName()
```

Returns the name of the serial field.

**Returns:** the name of the serial field

- getType

```java
ReferenceTree
getType()
```

Returns the type of the serial field.

**Returns:** the type of the serial field

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description of the serial field.

**Returns:** the description of the serial field

Method Detail

- getName

```java
IdentifierTree
getName()
```

Returns the name of the serial field.

**Returns:** the name of the serial field

- getType

```java
ReferenceTree
getType()
```

Returns the type of the serial field.

**Returns:** the type of the serial field

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description of the serial field.

**Returns:** the description of the serial field

---

#### Method Detail

getName

```java
IdentifierTree
getName()
```

Returns the name of the serial field.

**Returns:** the name of the serial field

---

#### getName

IdentifierTree

getName()

Returns the name of the serial field.

getType

```java
ReferenceTree
getType()
```

Returns the type of the serial field.

**Returns:** the type of the serial field

---

#### getType

ReferenceTree

getType()

Returns the type of the serial field.

getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description of the serial field.

**Returns:** the description of the serial field

---

#### getDescription

List

<? extends

DocTree

> getDescription()

Returns the description of the serial field.

---

