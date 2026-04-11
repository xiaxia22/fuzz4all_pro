# Interface BlockTagTree

**Source:** `jdk.compiler\com\sun\source\doctree\BlockTagTree.html`

### Class Description

```java
public interface
BlockTagTree

extends
DocTree
```

A tree node used as the base class for the different types of
block tags.

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

#### Interface BlockTagTree

**All Superinterfaces:** DocTree

**All Known Subinterfaces:** AuthorTree

,

DeprecatedTree

,

HiddenTree

,

ParamTree

,

ProvidesTree

,

ReturnTree

,

SeeTree

,

SerialDataTree

,

SerialFieldTree

,

SerialTree

,

SinceTree

,

ThrowsTree

,

UnknownBlockTagTree

,

UsesTree

,

VersionTree

```java
public interface
BlockTagTree

extends
DocTree
```

A tree node used as the base class for the different types of
block tags.

**Since:** 1.8

public interface

BlockTagTree

extends

DocTree

A tree node used as the base class for the different types of
block tags.

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

