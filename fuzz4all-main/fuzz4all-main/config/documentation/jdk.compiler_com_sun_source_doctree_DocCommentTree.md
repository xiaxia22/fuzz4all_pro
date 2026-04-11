# Interface DocCommentTree

**Source:** `jdk.compiler\com\sun\source\doctree\DocCommentTree.html`

### Class Description

```java
public interface
DocCommentTree

extends
DocTree
```

The top level representation of a documentation comment.

first-sentence body block-tags

**All Superinterfaces:** DocTree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
DocTree
> getFirstSentence()

Returns the first sentence of a documentation comment.

**Returns:**
- the first sentence of a documentation comment

---

#### default
List
<? extends
DocTree
> getFullBody()

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

**Returns:**
- body of a documentation comment first sentence inclusive

**Since:**
- 9

---

#### List
<? extends
DocTree
> getBody()

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

**Returns:**
- the body of a documentation comment

---

#### List
<? extends
DocTree
> getBlockTags()

Returns the block tags for a documentation comment.

**Returns:**
- the block tags of a documentation comment

---

#### default
List
<? extends
DocTree
> getPreamble()

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When the

DocCommentTree

has been read from an HTML file, this
represents the content from the beginning of the file up to and
including the

<body>

tag.

**Returns:**
- the list of trees

**Since:**
- 10

**Implementation Requirements:**
- This implementation returns an empty list.

---

#### default
List
<? extends
DocTree
> getPostamble()

Returns a list of trees containing the content (if any) following the
content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When

DocCommentTree

has been read from an HTML file, this
represents the content from the

</body>

tag to the end of file.

**Returns:**
- the list of trees

**Since:**
- 10

**Implementation Requirements:**
- This implementation returns an empty list.

---

### Additional Sections

#### Interface DocCommentTree

**All Superinterfaces:** DocTree

```java
public interface
DocCommentTree

extends
DocTree
```

The top level representation of a documentation comment.

first-sentence body block-tags

**Since:** 1.8

public interface

DocCommentTree

extends

DocTree

The top level representation of a documentation comment.

first-sentence body block-tags

first-sentence body block-tags

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

Default Methods

Modifier and Type

Method

Description

List

<? extends

DocTree

>

getBlockTags

()

Returns the block tags for a documentation comment.

List

<? extends

DocTree

>

getBody

()

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

List

<? extends

DocTree

>

getFirstSentence

()

Returns the first sentence of a documentation comment.

default

List

<? extends

DocTree

>

getFullBody

()

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

default

List

<? extends

DocTree

>

getPostamble

()

Returns a list of trees containing the content (if any) following the
content of the documentation comment.

default

List

<? extends

DocTree

>

getPreamble

()

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.

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

Default Methods

Modifier and Type

Method

Description

List

<? extends

DocTree

>

getBlockTags

()

Returns the block tags for a documentation comment.

List

<? extends

DocTree

>

getBody

()

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

List

<? extends

DocTree

>

getFirstSentence

()

Returns the first sentence of a documentation comment.

default

List

<? extends

DocTree

>

getFullBody

()

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

default

List

<? extends

DocTree

>

getPostamble

()

Returns a list of trees containing the content (if any) following the
content of the documentation comment.

default

List

<? extends

DocTree

>

getPreamble

()

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.

- Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Method Summary

Returns the block tags for a documentation comment.

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

Returns the first sentence of a documentation comment.

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

Returns a list of trees containing the content (if any) following the
content of the documentation comment.

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.

Methods declared in interface com.sun.source.doctree.

DocTree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.doctree. DocTree

============ METHOD DETAIL ==========

- Method Detail

- getFirstSentence

```java
List
<? extends
DocTree
> getFirstSentence()
```

Returns the first sentence of a documentation comment.

**Returns:** the first sentence of a documentation comment

- getFullBody

```java
default
List
<? extends
DocTree
> getFullBody()
```

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

**Returns:** body of a documentation comment first sentence inclusive
**Since:** 9

- getBody

```java
List
<? extends
DocTree
> getBody()
```

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

**Returns:** the body of a documentation comment

- getBlockTags

```java
List
<? extends
DocTree
> getBlockTags()
```

Returns the block tags for a documentation comment.

**Returns:** the block tags of a documentation comment

- getPreamble

```java
default
List
<? extends
DocTree
> getPreamble()
```

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When the

DocCommentTree

has been read from an HTML file, this
represents the content from the beginning of the file up to and
including the

<body>

tag.

**Implementation Requirements:** This implementation returns an empty list.
**Returns:** the list of trees
**Since:** 10

- getPostamble

```java
default
List
<? extends
DocTree
> getPostamble()
```

Returns a list of trees containing the content (if any) following the
content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When

DocCommentTree

has been read from an HTML file, this
represents the content from the

</body>

tag to the end of file.

**Implementation Requirements:** This implementation returns an empty list.
**Returns:** the list of trees
**Since:** 10

Method Detail

- getFirstSentence

```java
List
<? extends
DocTree
> getFirstSentence()
```

Returns the first sentence of a documentation comment.

**Returns:** the first sentence of a documentation comment

- getFullBody

```java
default
List
<? extends
DocTree
> getFullBody()
```

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

**Returns:** body of a documentation comment first sentence inclusive
**Since:** 9

- getBody

```java
List
<? extends
DocTree
> getBody()
```

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

**Returns:** the body of a documentation comment

- getBlockTags

```java
List
<? extends
DocTree
> getBlockTags()
```

Returns the block tags for a documentation comment.

**Returns:** the block tags of a documentation comment

- getPreamble

```java
default
List
<? extends
DocTree
> getPreamble()
```

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When the

DocCommentTree

has been read from an HTML file, this
represents the content from the beginning of the file up to and
including the

<body>

tag.

**Implementation Requirements:** This implementation returns an empty list.
**Returns:** the list of trees
**Since:** 10

- getPostamble

```java
default
List
<? extends
DocTree
> getPostamble()
```

Returns a list of trees containing the content (if any) following the
content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When

DocCommentTree

has been read from an HTML file, this
represents the content from the

</body>

tag to the end of file.

**Implementation Requirements:** This implementation returns an empty list.
**Returns:** the list of trees
**Since:** 10

---

#### Method Detail

getFirstSentence

```java
List
<? extends
DocTree
> getFirstSentence()
```

Returns the first sentence of a documentation comment.

**Returns:** the first sentence of a documentation comment

---

#### getFirstSentence

List

<? extends

DocTree

> getFirstSentence()

Returns the first sentence of a documentation comment.

getFullBody

```java
default
List
<? extends
DocTree
> getFullBody()
```

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

**Returns:** body of a documentation comment first sentence inclusive
**Since:** 9

---

#### getFullBody

default

List

<? extends

DocTree

> getFullBody()

Returns the entire body of a documentation comment, appearing
before any block tags, including the first sentence.

getBody

```java
List
<? extends
DocTree
> getBody()
```

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

**Returns:** the body of a documentation comment

---

#### getBody

List

<? extends

DocTree

> getBody()

Returns the body of a documentation comment,
appearing after the first sentence, and before any block tags.

getBlockTags

```java
List
<? extends
DocTree
> getBlockTags()
```

Returns the block tags for a documentation comment.

**Returns:** the block tags of a documentation comment

---

#### getBlockTags

List

<? extends

DocTree

> getBlockTags()

Returns the block tags for a documentation comment.

getPreamble

```java
default
List
<? extends
DocTree
> getPreamble()
```

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When the

DocCommentTree

has been read from an HTML file, this
represents the content from the beginning of the file up to and
including the

<body>

tag.

**Implementation Requirements:** This implementation returns an empty list.
**Returns:** the list of trees
**Since:** 10

---

#### getPreamble

default

List

<? extends

DocTree

> getPreamble()

Returns a list of trees containing the content (if any) preceding
the content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When the

DocCommentTree

has been read from an HTML file, this
represents the content from the beginning of the file up to and
including the

<body>

tag.

getPostamble

```java
default
List
<? extends
DocTree
> getPostamble()
```

Returns a list of trees containing the content (if any) following the
content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When

DocCommentTree

has been read from an HTML file, this
represents the content from the

</body>

tag to the end of file.

**Implementation Requirements:** This implementation returns an empty list.
**Returns:** the list of trees
**Since:** 10

---

#### getPostamble

default

List

<? extends

DocTree

> getPostamble()

Returns a list of trees containing the content (if any) following the
content of the documentation comment.
When the

DocCommentTree

has been read from a documentation
comment in a Java source file, the list will be empty.
When

DocCommentTree

has been read from an HTML file, this
represents the content from the

</body>

tag to the end of file.

---

