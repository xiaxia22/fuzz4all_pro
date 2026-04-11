# Interface InlineTagTree

**Source:** `jdk.compiler\com\sun\source\doctree\InlineTagTree.html`

### Class Description

```java
public interface
InlineTagTree

extends
DocTree
```

A tree node used as the base class for the different types of
inline tags.

**All Superinterfaces:** DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getTagName()

Returns the name of the tag.

**Returns:**
- the name of the tag

---

### Additional Sections

#### Interface InlineTagTree

**All Superinterfaces:** DocTree

**All Known Subinterfaces:** DocRootTree

,

IndexTree

,

InheritDocTree

,

LinkTree

,

LiteralTree

,

SummaryTree

,

UnknownInlineTagTree

,

ValueTree

```java
public interface
InlineTagTree

extends
DocTree
```

A tree node used as the base class for the different types of
inline tags.

**Since:** 1.8

public interface

InlineTagTree

extends

DocTree

A tree node used as the base class for the different types of
inline tags.

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

String

getTagName

()

Returns the name of the tag.

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

String

getTagName

()

Returns the name of the tag.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns the name of the tag.

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getTagName

```java
String
getTagName()
```

Returns the name of the tag.

**Returns:** the name of the tag

Method Detail

- getTagName

```java
String
getTagName()
```

Returns the name of the tag.

**Returns:** the name of the tag

---

#### Method Detail

getTagName

```java
String
getTagName()
```

Returns the name of the tag.

**Returns:** the name of the tag

---

#### getTagName

String

getTagName()

Returns the name of the tag.

---

