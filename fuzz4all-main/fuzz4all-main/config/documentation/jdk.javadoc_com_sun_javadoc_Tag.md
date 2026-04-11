# Interface Tag

**Source:** `jdk.javadoc\com\sun\javadoc\Tag.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Tag
```

Represents a simple documentation tag, such as @since, @author, @version.
Given a tag (e.g. "@since 1.2"), holds tag name (e.g. "@since")
and tag text (e.g. "1.2"). Tags with structure or which require
special processing are handled by subclasses such as ParamTag
(for @param), SeeTag (for @see and ), and ThrowsTag
(for @throws).

**All Known Subinterfaces:** ParamTag

,

SeeTag

,

SerialFieldTag

,

ThrowsTag

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Return the name of this tag. The name is the string
starting with "@" that is used in a doc comment, such as

@return

. For inline tags, such as

{@link}

, the curly brackets
are not part of the name, so in this example the name
would be simply

@link

.

**Returns:**
- the name of this tag

---

#### Doc
holder()

Return the containing

Doc

of this Tag element.

**Returns:**
- the containing

Doc

of this Tag element

---

#### String
kind()

Return the kind of this tag.
For most tags,

kind() == name()

;
the following table lists those cases where there is more
than one tag of a given kind:

Related Tags

name()

kind()

@exception

@throws

@link

@see

@linkplain

@see

@see

@see

@serial

@serial

@serialData

@serial

@throws

@throws

**Returns:**
- the kind of this tag.

---

#### String
text()

Return the text of this tag, that is, the portion beyond tag name.

**Returns:**
- the text of this tag

---

#### String
toString()

Convert this object to a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### Tag
[] inlineTags()

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects. The entire
doc comment is broken down into strings separated by

{@link}

tags, where each successive element
of the array represents either a string or

{@link}

tag, in order, from start to end.
Each string is represented by a

Tag

object of
name "Text", where

text()

returns the string. Each

{@link}

tag is represented by a

SeeTag

of name "@link" and kind "@see".
For example, given the following comment
tag:

This is a {@link Doc commentlabel} example.

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

**Returns:**
- Tag[] array of tags

**See Also:**
- ParamTag

,

ThrowsTag

---

#### Tag
[] firstSentenceTags()

Return the first sentence of the comment as an array of tags.
Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of kind "Text".
Inline tags are represented as a

SeeTag

of kind "@link".
If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by paragraph and
section terminating HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:**
- an array of

Tag

objects representing the
first sentence of the comment

---

#### SourcePosition
position()

Return the source position of this tag.

**Returns:**
- the source position of this tag.

---

### Additional Sections

#### Interface Tag

**All Known Subinterfaces:** ParamTag

,

SeeTag

,

SerialFieldTag

,

ThrowsTag

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Tag
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a simple documentation tag, such as @since, @author, @version.
Given a tag (e.g. "@since 1.2"), holds tag name (e.g. "@since")
and tag text (e.g. "1.2"). Tags with structure or which require
special processing are handled by subclasses such as ParamTag
(for @param), SeeTag (for @see and ), and ThrowsTag
(for @throws).

**See Also:** SeeTag

,

ParamTag

,

ThrowsTag

,

SerialFieldTag

,

Doc.tags()

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Tag

Represents a simple documentation tag, such as @since, @author, @version.
Given a tag (e.g. "@since 1.2"), holds tag name (e.g. "@since")
and tag text (e.g. "1.2"). Tags with structure or which require
special processing are handled by subclasses such as ParamTag
(for @param), SeeTag (for @see and ), and ThrowsTag
(for @throws).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Tag

[]

firstSentenceTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.

Doc

holder

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the containing

Doc

of this Tag element.

Tag

[]

inlineTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects.

String

kind

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the kind of this tag.

String

name

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of this tag.

SourcePosition

position

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of this tag.

String

text

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of this tag, that is, the portion beyond tag name.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Convert this object to a string.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Tag

[]

firstSentenceTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.

Doc

holder

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the containing

Doc

of this Tag element.

Tag

[]

inlineTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects.

String

kind

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the kind of this tag.

String

name

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of this tag.

SourcePosition

position

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of this tag.

String

text

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of this tag, that is, the portion beyond tag name.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Convert this object to a string.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.

Return the containing

Doc

of this Tag element.

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects.

Return the kind of this tag.

Return the name of this tag.

Return the source position of this tag.

Return the text of this tag, that is, the portion beyond tag name.

Convert this object to a string.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of this tag. The name is the string
starting with "@" that is used in a doc comment, such as

@return

. For inline tags, such as

{@link}

, the curly brackets
are not part of the name, so in this example the name
would be simply

@link

.

**Returns:** the name of this tag

- holder

```java
Doc
holder()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the containing

Doc

of this Tag element.

**Returns:** the containing

Doc

of this Tag element

- kind

```java
String
kind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the kind of this tag.
For most tags,

kind() == name()

;
the following table lists those cases where there is more
than one tag of a given kind:

Related Tags

name()

kind()

@exception

@throws

@link

@see

@linkplain

@see

@see

@see

@serial

@serial

@serialData

@serial

@throws

@throws

**Returns:** the kind of this tag.

- text

```java
String
text()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of this tag, that is, the portion beyond tag name.

**Returns:** the text of this tag

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert this object to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- inlineTags

```java
Tag
[] inlineTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects. The entire
doc comment is broken down into strings separated by

{@link}

tags, where each successive element
of the array represents either a string or

{@link}

tag, in order, from start to end.
Each string is represented by a

Tag

object of
name "Text", where

text()

returns the string. Each

{@link}

tag is represented by a

SeeTag

of name "@link" and kind "@see".
For example, given the following comment
tag:

This is a {@link Doc commentlabel} example.

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

**Returns:** Tag[] array of tags
**See Also:** ParamTag

,

ThrowsTag

- firstSentenceTags

```java
Tag
[] firstSentenceTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.
Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of kind "Text".
Inline tags are represented as a

SeeTag

of kind "@link".
If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by paragraph and
section terminating HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:** an array of

Tag

objects representing the
first sentence of the comment

- position

```java
SourcePosition
position()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of this tag.

**Returns:** the source position of this tag.

Method Detail

- name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of this tag. The name is the string
starting with "@" that is used in a doc comment, such as

@return

. For inline tags, such as

{@link}

, the curly brackets
are not part of the name, so in this example the name
would be simply

@link

.

**Returns:** the name of this tag

- holder

```java
Doc
holder()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the containing

Doc

of this Tag element.

**Returns:** the containing

Doc

of this Tag element

- kind

```java
String
kind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the kind of this tag.
For most tags,

kind() == name()

;
the following table lists those cases where there is more
than one tag of a given kind:

Related Tags

name()

kind()

@exception

@throws

@link

@see

@linkplain

@see

@see

@see

@serial

@serial

@serialData

@serial

@throws

@throws

**Returns:** the kind of this tag.

- text

```java
String
text()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of this tag, that is, the portion beyond tag name.

**Returns:** the text of this tag

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert this object to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- inlineTags

```java
Tag
[] inlineTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects. The entire
doc comment is broken down into strings separated by

{@link}

tags, where each successive element
of the array represents either a string or

{@link}

tag, in order, from start to end.
Each string is represented by a

Tag

object of
name "Text", where

text()

returns the string. Each

{@link}

tag is represented by a

SeeTag

of name "@link" and kind "@see".
For example, given the following comment
tag:

This is a {@link Doc commentlabel} example.

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

**Returns:** Tag[] array of tags
**See Also:** ParamTag

,

ThrowsTag

- firstSentenceTags

```java
Tag
[] firstSentenceTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.
Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of kind "Text".
Inline tags are represented as a

SeeTag

of kind "@link".
If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by paragraph and
section terminating HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:** an array of

Tag

objects representing the
first sentence of the comment

- position

```java
SourcePosition
position()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of this tag.

**Returns:** the source position of this tag.

---

#### Method Detail

name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the name of this tag. The name is the string
starting with "@" that is used in a doc comment, such as

@return

. For inline tags, such as

{@link}

, the curly brackets
are not part of the name, so in this example the name
would be simply

@link

.

**Returns:** the name of this tag

---

#### name

String

name()

Return the name of this tag. The name is the string
starting with "@" that is used in a doc comment, such as

@return

. For inline tags, such as

{@link}

, the curly brackets
are not part of the name, so in this example the name
would be simply

@link

.

holder

```java
Doc
holder()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the containing

Doc

of this Tag element.

**Returns:** the containing

Doc

of this Tag element

---

#### holder

Doc

holder()

Return the containing

Doc

of this Tag element.

kind

```java
String
kind()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the kind of this tag.
For most tags,

kind() == name()

;
the following table lists those cases where there is more
than one tag of a given kind:

Related Tags

name()

kind()

@exception

@throws

@link

@see

@linkplain

@see

@see

@see

@serial

@serial

@serialData

@serial

@throws

@throws

**Returns:** the kind of this tag.

---

#### kind

String

kind()

Return the kind of this tag.
For most tags,

kind() == name()

;
the following table lists those cases where there is more
than one tag of a given kind:

Related Tags

name()

kind()

@exception

@throws

@link

@see

@linkplain

@see

@see

@see

@serial

@serial

@serialData

@serial

@throws

@throws

text

```java
String
text()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of this tag, that is, the portion beyond tag name.

**Returns:** the text of this tag

---

#### text

String

text()

Return the text of this tag, that is, the portion beyond tag name.

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Convert this object to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

String

toString()

Convert this object to a string.

inlineTags

```java
Tag
[] inlineTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects. The entire
doc comment is broken down into strings separated by

{@link}

tags, where each successive element
of the array represents either a string or

{@link}

tag, in order, from start to end.
Each string is represented by a

Tag

object of
name "Text", where

text()

returns the string. Each

{@link}

tag is represented by a

SeeTag

of name "@link" and kind "@see".
For example, given the following comment
tag:

This is a {@link Doc commentlabel} example.

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

**Returns:** Tag[] array of tags
**See Also:** ParamTag

,

ThrowsTag

---

#### inlineTags

Tag

[] inlineTags()

For a documentation comment with embedded

{@link}

tags, return an array of

Tag

objects. The entire
doc comment is broken down into strings separated by

{@link}

tags, where each successive element
of the array represents either a string or

{@link}

tag, in order, from start to end.
Each string is represented by a

Tag

object of
name "Text", where

text()

returns the string. Each

{@link}

tag is represented by a

SeeTag

of name "@link" and kind "@see".
For example, given the following comment
tag:

This is a {@link Doc commentlabel} example.

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

This is a {@link Doc commentlabel} example.

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

return an array of Tag objects:

- tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

tags[0] is a

Tag

with name "Text" and text consisting
of "This is a "

tags[1] is a

SeeTag

with name "@link", referenced
class

Doc

and label "commentlabel"

tags[2] is a

Tag

with name "Text" and text consisting
of " example."

firstSentenceTags

```java
Tag
[] firstSentenceTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.
Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of kind "Text".
Inline tags are represented as a

SeeTag

of kind "@link".
If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by paragraph and
section terminating HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:** an array of

Tag

objects representing the
first sentence of the comment

---

#### firstSentenceTags

Tag

[] firstSentenceTags()

Return the first sentence of the comment as an array of tags.
Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of kind "Text".
Inline tags are represented as a

SeeTag

of kind "@link".
If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by paragraph and
section terminating HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

position

```java
SourcePosition
position()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of this tag.

**Returns:** the source position of this tag.

---

#### position

SourcePosition

position()

Return the source position of this tag.

---

