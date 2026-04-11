# Interface IndexTree

**Source:** `jdk.compiler\com\sun\source\doctree\IndexTree.html`

### Class Description

```java
public interface
IndexTree

extends
InlineTagTree
```

A tree node for an @index or @index inline tag.

{@index keyword optional description}

**All Superinterfaces:** DocTree

,

InlineTagTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DocTree
getSearchTerm()

Returns the specified search term.

**Returns:**
- the search term

---

#### List
<? extends
DocTree
> getDescription()

Returns the description, if any.

**Returns:**
- the description

---

### Additional Sections

#### Interface IndexTree

**All Superinterfaces:** DocTree

,

InlineTagTree

```java
public interface
IndexTree

extends
InlineTagTree
```

A tree node for an @index or @index inline tag.

{@index keyword optional description}

**Since:** 9

public interface

IndexTree

extends

InlineTagTree

A tree node for an @index or @index inline tag.

{@index keyword optional description}

{@index keyword optional description}

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

Returns the description, if any.

DocTree

getSearchTerm

()

Returns the specified search term.

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

getDescription

()

Returns the description, if any.

DocTree

getSearchTerm

()

Returns the specified search term.

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

Returns the description, if any.

Returns the specified search term.

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

- getSearchTerm

```java
DocTree
getSearchTerm()
```

Returns the specified search term.

**Returns:** the search term

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description, if any.

**Returns:** the description

Method Detail

- getSearchTerm

```java
DocTree
getSearchTerm()
```

Returns the specified search term.

**Returns:** the search term

- getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description, if any.

**Returns:** the description

---

#### Method Detail

getSearchTerm

```java
DocTree
getSearchTerm()
```

Returns the specified search term.

**Returns:** the search term

---

#### getSearchTerm

DocTree

getSearchTerm()

Returns the specified search term.

getDescription

```java
List
<? extends
DocTree
> getDescription()
```

Returns the description, if any.

**Returns:** the description

---

#### getDescription

List

<? extends

DocTree

> getDescription()

Returns the description, if any.

---

