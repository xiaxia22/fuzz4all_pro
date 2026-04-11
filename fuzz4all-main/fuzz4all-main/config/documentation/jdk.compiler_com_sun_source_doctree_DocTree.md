# Interface DocTree

**Source:** `jdk.compiler\com\sun\source\doctree\DocTree.html`

### Class Description

```java
public interface
DocTree
```

Common interface for all nodes in a documentation syntax tree.

**All Known Subinterfaces:** AttributeTree

,

AuthorTree

,

BlockTagTree

,

CommentTree

,

DeprecatedTree

,

DocCommentTree

,

DocRootTree

,

DocTypeTree

,

EndElementTree

,

EntityTree

,

ErroneousTree

,

HiddenTree

,

IdentifierTree

,

IndexTree

,

InheritDocTree

,

InlineTagTree

,

LinkTree

,

LiteralTree

,

ParamTree

,

ProvidesTree

,

ReferenceTree

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

StartElementTree

,

SummaryTree

,

TextTree

,

ThrowsTree

,

UnknownBlockTagTree

,

UnknownInlineTagTree

,

UsesTree

,

ValueTree

,

VersionTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DocTree.Kind
getKind()

Returns the kind of this tree.

**Returns:**
- the kind of this tree.

---

#### <R,​D> R accept​(
DocTreeVisitor
<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Parameters:**
- visitor

- the visitor to be called
- data

- a parameter value to be passed to the visitor method

**Returns:**
- the value returned from the visitor method

**Type Parameters:**
- R

- result type of this operation.
- D

- type of additional data.

---

### Additional Sections

#### Interface DocTree

**All Known Subinterfaces:** AttributeTree

,

AuthorTree

,

BlockTagTree

,

CommentTree

,

DeprecatedTree

,

DocCommentTree

,

DocRootTree

,

DocTypeTree

,

EndElementTree

,

EntityTree

,

ErroneousTree

,

HiddenTree

,

IdentifierTree

,

IndexTree

,

InheritDocTree

,

InlineTagTree

,

LinkTree

,

LiteralTree

,

ParamTree

,

ProvidesTree

,

ReferenceTree

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

StartElementTree

,

SummaryTree

,

TextTree

,

ThrowsTree

,

UnknownBlockTagTree

,

UnknownInlineTagTree

,

UsesTree

,

ValueTree

,

VersionTree

```java
public interface
DocTree
```

Common interface for all nodes in a documentation syntax tree.

**Since:** 1.8

public interface

DocTree

Common interface for all nodes in a documentation syntax tree.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

DocTree.Kind

Enumerates all kinds of trees.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​D>

R

accept

​(

DocTreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern.

DocTree.Kind

getKind

()

Returns the kind of this tree.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

DocTree.Kind

Enumerates all kinds of trees.

---

#### Nested Class Summary

Enumerates all kinds of trees.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​D>

R

accept

​(

DocTreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern.

DocTree.Kind

getKind

()

Returns the kind of this tree.

---

#### Method Summary

Accept method used to implement the visitor pattern.

Returns the kind of this tree.

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
DocTree.Kind
getKind()
```

Returns the kind of this tree.

**Returns:** the kind of this tree.

- accept

```java
<R,​D> R accept​(
DocTreeVisitor
<R,​D> visitor,
D data)
```

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- the visitor to be called
**Parameters:** data

- a parameter value to be passed to the visitor method
**Returns:** the value returned from the visitor method

Method Detail

- getKind

```java
DocTree.Kind
getKind()
```

Returns the kind of this tree.

**Returns:** the kind of this tree.

- accept

```java
<R,​D> R accept​(
DocTreeVisitor
<R,​D> visitor,
D data)
```

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- the visitor to be called
**Parameters:** data

- a parameter value to be passed to the visitor method
**Returns:** the value returned from the visitor method

---

#### Method Detail

getKind

```java
DocTree.Kind
getKind()
```

Returns the kind of this tree.

**Returns:** the kind of this tree.

---

#### getKind

DocTree.Kind

getKind()

Returns the kind of this tree.

accept

```java
<R,​D> R accept​(
DocTreeVisitor
<R,​D> visitor,
D data)
```

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

**Type Parameters:** R

- result type of this operation.
**Type Parameters:** D

- type of additional data.
**Parameters:** visitor

- the visitor to be called
**Parameters:** data

- a parameter value to be passed to the visitor method
**Returns:** the value returned from the visitor method

---

#### accept

<R,​D> R accept​(

DocTreeVisitor

<R,​D> visitor,
D data)

Accept method used to implement the visitor pattern. The
visitor pattern is used to implement operations on trees.

---

