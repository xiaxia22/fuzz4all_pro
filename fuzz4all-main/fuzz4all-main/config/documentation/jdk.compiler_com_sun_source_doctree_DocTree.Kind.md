# Enum DocTree.Kind

**Source:** `jdk.compiler\com\sun\source\doctree\DocTree.Kind.html`

### Class Description

```java
public static enum
DocTree.Kind

extends
Enum
<
DocTree.Kind
>
```

Enumerates all kinds of trees.

**All Implemented Interfaces:** Serializable

,

Comparable

<

DocTree.Kind

>

---

### Field Details

#### public final
String
tagName

The name of the tag, if any, associated with this kind of node.

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
DocTree.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocTree.Kind c : DocTree.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
DocTree.Kind
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum DocTree.Kind

java.lang.Object

- java.lang.Enum

<

DocTree.Kind

>
- - com.sun.source.doctree.DocTree.Kind

java.lang.Enum

<

DocTree.Kind

>

- com.sun.source.doctree.DocTree.Kind

com.sun.source.doctree.DocTree.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

DocTree.Kind

>

**Enclosing interface:** DocTree

```java
public static enum
DocTree.Kind

extends
Enum
<
DocTree.Kind
>
```

Enumerates all kinds of trees.

public static enum

DocTree.Kind

extends

Enum

<

DocTree.Kind

>

Enumerates all kinds of trees.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ATTRIBUTE

Used for instances of

AttributeTree

representing an HTML attribute.

AUTHOR

Used for instances of

AuthorTree

representing an @author tag.

CODE

Used for instances of

LiteralTree

representing an @code tag.

COMMENT

Used for instances of

CommentTree

representing an HTML comment.

DEPRECATED

Used for instances of

DeprecatedTree

representing an @deprecated tag.

DOC_COMMENT

Used for instances of

DocCommentTree

representing a complete doc comment.

DOC_ROOT

Used for instances of

DocRootTree

representing an @docRoot tag.

DOC_TYPE

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

END_ELEMENT

Used for instances of

EndElementTree

representing the end of an HTML element.

ENTITY

Used for instances of

EntityTree

representing an HTML entity.

ERRONEOUS

Used for instances of

ErroneousTree

representing some invalid text.

EXCEPTION

Used for instances of

ThrowsTree

representing an @exception tag.

HIDDEN

Used for instances of

HiddenTree

representing an @hidden tag.

IDENTIFIER

Used for instances of

IdentifierTree

representing an identifier.

INDEX

Used for instances of

IndexTree

representing a search term.

INHERIT_DOC

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

LINK

Used for instances of

LinkTree

representing an @link tag.

LINK_PLAIN

Used for instances of

LinkTree

representing an @linkplain tag.

LITERAL

Used for instances of

LiteralTree

representing an @literal tag.

OTHER

An implementation-reserved node.

PARAM

Used for instances of

ParamTree

representing an @param tag.

PROVIDES

Used for instances of

ProvidesTree

representing an @provides tag.

REFERENCE

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

RETURN

Used for instances of

ReturnTree

representing an @return tag.

SEE

Used for instances of

SeeTree

representing an @see tag.

SERIAL

Used for instances of

SerialTree

representing an @serial tag.

SERIAL_DATA

Used for instances of

SerialDataTree

representing an @serialData tag.

SERIAL_FIELD

Used for instances of

SerialFieldTree

representing an @serialField tag.

SINCE

Used for instances of

SinceTree

representing an @since tag.

START_ELEMENT

Used for instances of

EndElementTree

representing the start of an HTML element.

SUMMARY

Used for instances of

SummaryTree

representing the summary of a comment description.

TEXT

Used for instances of

TextTree

representing some documentation text.

THROWS

Used for instances of

ThrowsTree

representing an @throws tag.

UNKNOWN_BLOCK_TAG

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

UNKNOWN_INLINE_TAG

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

USES

Used for instances of

UsesTree

representing an @uses tag.

VALUE

Used for instances of

ValueTree

representing an @value tag.

VERSION

Used for instances of

VersionTree

representing an @version tag.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

String

tagName

The name of the tag, if any, associated with this kind of node.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

DocTree.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DocTree.Kind

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

ATTRIBUTE

Used for instances of

AttributeTree

representing an HTML attribute.

AUTHOR

Used for instances of

AuthorTree

representing an @author tag.

CODE

Used for instances of

LiteralTree

representing an @code tag.

COMMENT

Used for instances of

CommentTree

representing an HTML comment.

DEPRECATED

Used for instances of

DeprecatedTree

representing an @deprecated tag.

DOC_COMMENT

Used for instances of

DocCommentTree

representing a complete doc comment.

DOC_ROOT

Used for instances of

DocRootTree

representing an @docRoot tag.

DOC_TYPE

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

END_ELEMENT

Used for instances of

EndElementTree

representing the end of an HTML element.

ENTITY

Used for instances of

EntityTree

representing an HTML entity.

ERRONEOUS

Used for instances of

ErroneousTree

representing some invalid text.

EXCEPTION

Used for instances of

ThrowsTree

representing an @exception tag.

HIDDEN

Used for instances of

HiddenTree

representing an @hidden tag.

IDENTIFIER

Used for instances of

IdentifierTree

representing an identifier.

INDEX

Used for instances of

IndexTree

representing a search term.

INHERIT_DOC

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

LINK

Used for instances of

LinkTree

representing an @link tag.

LINK_PLAIN

Used for instances of

LinkTree

representing an @linkplain tag.

LITERAL

Used for instances of

LiteralTree

representing an @literal tag.

OTHER

An implementation-reserved node.

PARAM

Used for instances of

ParamTree

representing an @param tag.

PROVIDES

Used for instances of

ProvidesTree

representing an @provides tag.

REFERENCE

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

RETURN

Used for instances of

ReturnTree

representing an @return tag.

SEE

Used for instances of

SeeTree

representing an @see tag.

SERIAL

Used for instances of

SerialTree

representing an @serial tag.

SERIAL_DATA

Used for instances of

SerialDataTree

representing an @serialData tag.

SERIAL_FIELD

Used for instances of

SerialFieldTree

representing an @serialField tag.

SINCE

Used for instances of

SinceTree

representing an @since tag.

START_ELEMENT

Used for instances of

EndElementTree

representing the start of an HTML element.

SUMMARY

Used for instances of

SummaryTree

representing the summary of a comment description.

TEXT

Used for instances of

TextTree

representing some documentation text.

THROWS

Used for instances of

ThrowsTree

representing an @throws tag.

UNKNOWN_BLOCK_TAG

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

UNKNOWN_INLINE_TAG

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

USES

Used for instances of

UsesTree

representing an @uses tag.

VALUE

Used for instances of

ValueTree

representing an @value tag.

VERSION

Used for instances of

VersionTree

representing an @version tag.

---

#### Enum Constant Summary

Used for instances of

AttributeTree

representing an HTML attribute.

Used for instances of

AuthorTree

representing an @author tag.

Used for instances of

LiteralTree

representing an @code tag.

Used for instances of

CommentTree

representing an HTML comment.

Used for instances of

DeprecatedTree

representing an @deprecated tag.

Used for instances of

DocCommentTree

representing a complete doc comment.

Used for instances of

DocRootTree

representing an @docRoot tag.

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

Used for instances of

EndElementTree

representing the end of an HTML element.

Used for instances of

EntityTree

representing an HTML entity.

Used for instances of

ErroneousTree

representing some invalid text.

Used for instances of

ThrowsTree

representing an @exception tag.

Used for instances of

HiddenTree

representing an @hidden tag.

Used for instances of

IdentifierTree

representing an identifier.

Used for instances of

IndexTree

representing a search term.

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

Used for instances of

LinkTree

representing an @link tag.

Used for instances of

LinkTree

representing an @linkplain tag.

Used for instances of

LiteralTree

representing an @literal tag.

An implementation-reserved node.

Used for instances of

ParamTree

representing an @param tag.

Used for instances of

ProvidesTree

representing an @provides tag.

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

Used for instances of

ReturnTree

representing an @return tag.

Used for instances of

SeeTree

representing an @see tag.

Used for instances of

SerialTree

representing an @serial tag.

Used for instances of

SerialDataTree

representing an @serialData tag.

Used for instances of

SerialFieldTree

representing an @serialField tag.

Used for instances of

SinceTree

representing an @since tag.

Used for instances of

EndElementTree

representing the start of an HTML element.

Used for instances of

SummaryTree

representing the summary of a comment description.

Used for instances of

TextTree

representing some documentation text.

Used for instances of

ThrowsTree

representing an @throws tag.

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

Used for instances of

UsesTree

representing an @uses tag.

Used for instances of

ValueTree

representing an @value tag.

Used for instances of

VersionTree

representing an @version tag.

Field Summary

Fields

Modifier and Type

Field

Description

String

tagName

The name of the tag, if any, associated with this kind of node.

---

#### Field Summary

The name of the tag, if any, associated with this kind of node.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

DocTree.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DocTree.Kind

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- ATTRIBUTE

```java
public static final
DocTree.Kind
ATTRIBUTE
```

Used for instances of

AttributeTree

representing an HTML attribute.

- AUTHOR

```java
public static final
DocTree.Kind
AUTHOR
```

Used for instances of

AuthorTree

representing an @author tag.

- CODE

```java
public static final
DocTree.Kind
CODE
```

Used for instances of

LiteralTree

representing an @code tag.

- COMMENT

```java
public static final
DocTree.Kind
COMMENT
```

Used for instances of

CommentTree

representing an HTML comment.

- DEPRECATED

```java
public static final
DocTree.Kind
DEPRECATED
```

Used for instances of

DeprecatedTree

representing an @deprecated tag.

- DOC_COMMENT

```java
public static final
DocTree.Kind
DOC_COMMENT
```

Used for instances of

DocCommentTree

representing a complete doc comment.

- DOC_ROOT

```java
public static final
DocTree.Kind
DOC_ROOT
```

Used for instances of

DocRootTree

representing an @docRoot tag.

- DOC_TYPE

```java
public static final
DocTree.Kind
DOC_TYPE
```

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

- END_ELEMENT

```java
public static final
DocTree.Kind
END_ELEMENT
```

Used for instances of

EndElementTree

representing the end of an HTML element.

- ENTITY

```java
public static final
DocTree.Kind
ENTITY
```

Used for instances of

EntityTree

representing an HTML entity.

- ERRONEOUS

```java
public static final
DocTree.Kind
ERRONEOUS
```

Used for instances of

ErroneousTree

representing some invalid text.

- EXCEPTION

```java
public static final
DocTree.Kind
EXCEPTION
```

Used for instances of

ThrowsTree

representing an @exception tag.

- HIDDEN

```java
public static final
DocTree.Kind
HIDDEN
```

Used for instances of

HiddenTree

representing an @hidden tag.

- IDENTIFIER

```java
public static final
DocTree.Kind
IDENTIFIER
```

Used for instances of

IdentifierTree

representing an identifier.

- INDEX

```java
public static final
DocTree.Kind
INDEX
```

Used for instances of

IndexTree

representing a search term.

- INHERIT_DOC

```java
public static final
DocTree.Kind
INHERIT_DOC
```

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

- LINK

```java
public static final
DocTree.Kind
LINK
```

Used for instances of

LinkTree

representing an @link tag.

- LINK_PLAIN

```java
public static final
DocTree.Kind
LINK_PLAIN
```

Used for instances of

LinkTree

representing an @linkplain tag.

- LITERAL

```java
public static final
DocTree.Kind
LITERAL
```

Used for instances of

LiteralTree

representing an @literal tag.

- PARAM

```java
public static final
DocTree.Kind
PARAM
```

Used for instances of

ParamTree

representing an @param tag.

- PROVIDES

```java
public static final
DocTree.Kind
PROVIDES
```

Used for instances of

ProvidesTree

representing an @provides tag.

- REFERENCE

```java
public static final
DocTree.Kind
REFERENCE
```

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

- RETURN

```java
public static final
DocTree.Kind
RETURN
```

Used for instances of

ReturnTree

representing an @return tag.

- SEE

```java
public static final
DocTree.Kind
SEE
```

Used for instances of

SeeTree

representing an @see tag.

- SERIAL

```java
public static final
DocTree.Kind
SERIAL
```

Used for instances of

SerialTree

representing an @serial tag.

- SERIAL_DATA

```java
public static final
DocTree.Kind
SERIAL_DATA
```

Used for instances of

SerialDataTree

representing an @serialData tag.

- SERIAL_FIELD

```java
public static final
DocTree.Kind
SERIAL_FIELD
```

Used for instances of

SerialFieldTree

representing an @serialField tag.

- SINCE

```java
public static final
DocTree.Kind
SINCE
```

Used for instances of

SinceTree

representing an @since tag.

- START_ELEMENT

```java
public static final
DocTree.Kind
START_ELEMENT
```

Used for instances of

EndElementTree

representing the start of an HTML element.

- SUMMARY

```java
public static final
DocTree.Kind
SUMMARY
```

Used for instances of

SummaryTree

representing the summary of a comment description.

- TEXT

```java
public static final
DocTree.Kind
TEXT
```

Used for instances of

TextTree

representing some documentation text.

- THROWS

```java
public static final
DocTree.Kind
THROWS
```

Used for instances of

ThrowsTree

representing an @throws tag.

- UNKNOWN_BLOCK_TAG

```java
public static final
DocTree.Kind
UNKNOWN_BLOCK_TAG
```

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

- UNKNOWN_INLINE_TAG

```java
public static final
DocTree.Kind
UNKNOWN_INLINE_TAG
```

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

- USES

```java
public static final
DocTree.Kind
USES
```

Used for instances of

UsesTree

representing an @uses tag.

- VALUE

```java
public static final
DocTree.Kind
VALUE
```

Used for instances of

ValueTree

representing an @value tag.

- VERSION

```java
public static final
DocTree.Kind
VERSION
```

Used for instances of

VersionTree

representing an @version tag.

- OTHER

```java
public static final
DocTree.Kind
OTHER
```

An implementation-reserved node. This is the not the node
you are looking for.

============ FIELD DETAIL ===========

- Field Detail

- tagName

```java
public final
String
tagName
```

The name of the tag, if any, associated with this kind of node.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
DocTree.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocTree.Kind c : DocTree.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DocTree.Kind
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- ATTRIBUTE

```java
public static final
DocTree.Kind
ATTRIBUTE
```

Used for instances of

AttributeTree

representing an HTML attribute.

- AUTHOR

```java
public static final
DocTree.Kind
AUTHOR
```

Used for instances of

AuthorTree

representing an @author tag.

- CODE

```java
public static final
DocTree.Kind
CODE
```

Used for instances of

LiteralTree

representing an @code tag.

- COMMENT

```java
public static final
DocTree.Kind
COMMENT
```

Used for instances of

CommentTree

representing an HTML comment.

- DEPRECATED

```java
public static final
DocTree.Kind
DEPRECATED
```

Used for instances of

DeprecatedTree

representing an @deprecated tag.

- DOC_COMMENT

```java
public static final
DocTree.Kind
DOC_COMMENT
```

Used for instances of

DocCommentTree

representing a complete doc comment.

- DOC_ROOT

```java
public static final
DocTree.Kind
DOC_ROOT
```

Used for instances of

DocRootTree

representing an @docRoot tag.

- DOC_TYPE

```java
public static final
DocTree.Kind
DOC_TYPE
```

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

- END_ELEMENT

```java
public static final
DocTree.Kind
END_ELEMENT
```

Used for instances of

EndElementTree

representing the end of an HTML element.

- ENTITY

```java
public static final
DocTree.Kind
ENTITY
```

Used for instances of

EntityTree

representing an HTML entity.

- ERRONEOUS

```java
public static final
DocTree.Kind
ERRONEOUS
```

Used for instances of

ErroneousTree

representing some invalid text.

- EXCEPTION

```java
public static final
DocTree.Kind
EXCEPTION
```

Used for instances of

ThrowsTree

representing an @exception tag.

- HIDDEN

```java
public static final
DocTree.Kind
HIDDEN
```

Used for instances of

HiddenTree

representing an @hidden tag.

- IDENTIFIER

```java
public static final
DocTree.Kind
IDENTIFIER
```

Used for instances of

IdentifierTree

representing an identifier.

- INDEX

```java
public static final
DocTree.Kind
INDEX
```

Used for instances of

IndexTree

representing a search term.

- INHERIT_DOC

```java
public static final
DocTree.Kind
INHERIT_DOC
```

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

- LINK

```java
public static final
DocTree.Kind
LINK
```

Used for instances of

LinkTree

representing an @link tag.

- LINK_PLAIN

```java
public static final
DocTree.Kind
LINK_PLAIN
```

Used for instances of

LinkTree

representing an @linkplain tag.

- LITERAL

```java
public static final
DocTree.Kind
LITERAL
```

Used for instances of

LiteralTree

representing an @literal tag.

- PARAM

```java
public static final
DocTree.Kind
PARAM
```

Used for instances of

ParamTree

representing an @param tag.

- PROVIDES

```java
public static final
DocTree.Kind
PROVIDES
```

Used for instances of

ProvidesTree

representing an @provides tag.

- REFERENCE

```java
public static final
DocTree.Kind
REFERENCE
```

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

- RETURN

```java
public static final
DocTree.Kind
RETURN
```

Used for instances of

ReturnTree

representing an @return tag.

- SEE

```java
public static final
DocTree.Kind
SEE
```

Used for instances of

SeeTree

representing an @see tag.

- SERIAL

```java
public static final
DocTree.Kind
SERIAL
```

Used for instances of

SerialTree

representing an @serial tag.

- SERIAL_DATA

```java
public static final
DocTree.Kind
SERIAL_DATA
```

Used for instances of

SerialDataTree

representing an @serialData tag.

- SERIAL_FIELD

```java
public static final
DocTree.Kind
SERIAL_FIELD
```

Used for instances of

SerialFieldTree

representing an @serialField tag.

- SINCE

```java
public static final
DocTree.Kind
SINCE
```

Used for instances of

SinceTree

representing an @since tag.

- START_ELEMENT

```java
public static final
DocTree.Kind
START_ELEMENT
```

Used for instances of

EndElementTree

representing the start of an HTML element.

- SUMMARY

```java
public static final
DocTree.Kind
SUMMARY
```

Used for instances of

SummaryTree

representing the summary of a comment description.

- TEXT

```java
public static final
DocTree.Kind
TEXT
```

Used for instances of

TextTree

representing some documentation text.

- THROWS

```java
public static final
DocTree.Kind
THROWS
```

Used for instances of

ThrowsTree

representing an @throws tag.

- UNKNOWN_BLOCK_TAG

```java
public static final
DocTree.Kind
UNKNOWN_BLOCK_TAG
```

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

- UNKNOWN_INLINE_TAG

```java
public static final
DocTree.Kind
UNKNOWN_INLINE_TAG
```

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

- USES

```java
public static final
DocTree.Kind
USES
```

Used for instances of

UsesTree

representing an @uses tag.

- VALUE

```java
public static final
DocTree.Kind
VALUE
```

Used for instances of

ValueTree

representing an @value tag.

- VERSION

```java
public static final
DocTree.Kind
VERSION
```

Used for instances of

VersionTree

representing an @version tag.

- OTHER

```java
public static final
DocTree.Kind
OTHER
```

An implementation-reserved node. This is the not the node
you are looking for.

---

#### Enum Constant Detail

ATTRIBUTE

```java
public static final
DocTree.Kind
ATTRIBUTE
```

Used for instances of

AttributeTree

representing an HTML attribute.

---

#### ATTRIBUTE

public static final

DocTree.Kind

ATTRIBUTE

Used for instances of

AttributeTree

representing an HTML attribute.

AUTHOR

```java
public static final
DocTree.Kind
AUTHOR
```

Used for instances of

AuthorTree

representing an @author tag.

---

#### AUTHOR

public static final

DocTree.Kind

AUTHOR

Used for instances of

AuthorTree

representing an @author tag.

CODE

```java
public static final
DocTree.Kind
CODE
```

Used for instances of

LiteralTree

representing an @code tag.

---

#### CODE

public static final

DocTree.Kind

CODE

Used for instances of

LiteralTree

representing an @code tag.

COMMENT

```java
public static final
DocTree.Kind
COMMENT
```

Used for instances of

CommentTree

representing an HTML comment.

---

#### COMMENT

public static final

DocTree.Kind

COMMENT

Used for instances of

CommentTree

representing an HTML comment.

DEPRECATED

```java
public static final
DocTree.Kind
DEPRECATED
```

Used for instances of

DeprecatedTree

representing an @deprecated tag.

---

#### DEPRECATED

public static final

DocTree.Kind

DEPRECATED

Used for instances of

DeprecatedTree

representing an @deprecated tag.

DOC_COMMENT

```java
public static final
DocTree.Kind
DOC_COMMENT
```

Used for instances of

DocCommentTree

representing a complete doc comment.

---

#### DOC_COMMENT

public static final

DocTree.Kind

DOC_COMMENT

Used for instances of

DocCommentTree

representing a complete doc comment.

DOC_ROOT

```java
public static final
DocTree.Kind
DOC_ROOT
```

Used for instances of

DocRootTree

representing an @docRoot tag.

---

#### DOC_ROOT

public static final

DocTree.Kind

DOC_ROOT

Used for instances of

DocRootTree

representing an @docRoot tag.

DOC_TYPE

```java
public static final
DocTree.Kind
DOC_TYPE
```

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

---

#### DOC_TYPE

public static final

DocTree.Kind

DOC_TYPE

Used for instances of

DocTypeTree

representing an HTML DocType declaration.

END_ELEMENT

```java
public static final
DocTree.Kind
END_ELEMENT
```

Used for instances of

EndElementTree

representing the end of an HTML element.

---

#### END_ELEMENT

public static final

DocTree.Kind

END_ELEMENT

Used for instances of

EndElementTree

representing the end of an HTML element.

ENTITY

```java
public static final
DocTree.Kind
ENTITY
```

Used for instances of

EntityTree

representing an HTML entity.

---

#### ENTITY

public static final

DocTree.Kind

ENTITY

Used for instances of

EntityTree

representing an HTML entity.

ERRONEOUS

```java
public static final
DocTree.Kind
ERRONEOUS
```

Used for instances of

ErroneousTree

representing some invalid text.

---

#### ERRONEOUS

public static final

DocTree.Kind

ERRONEOUS

Used for instances of

ErroneousTree

representing some invalid text.

EXCEPTION

```java
public static final
DocTree.Kind
EXCEPTION
```

Used for instances of

ThrowsTree

representing an @exception tag.

---

#### EXCEPTION

public static final

DocTree.Kind

EXCEPTION

Used for instances of

ThrowsTree

representing an @exception tag.

HIDDEN

```java
public static final
DocTree.Kind
HIDDEN
```

Used for instances of

HiddenTree

representing an @hidden tag.

---

#### HIDDEN

public static final

DocTree.Kind

HIDDEN

Used for instances of

HiddenTree

representing an @hidden tag.

IDENTIFIER

```java
public static final
DocTree.Kind
IDENTIFIER
```

Used for instances of

IdentifierTree

representing an identifier.

---

#### IDENTIFIER

public static final

DocTree.Kind

IDENTIFIER

Used for instances of

IdentifierTree

representing an identifier.

INDEX

```java
public static final
DocTree.Kind
INDEX
```

Used for instances of

IndexTree

representing a search term.

---

#### INDEX

public static final

DocTree.Kind

INDEX

Used for instances of

IndexTree

representing a search term.

INHERIT_DOC

```java
public static final
DocTree.Kind
INHERIT_DOC
```

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

---

#### INHERIT_DOC

public static final

DocTree.Kind

INHERIT_DOC

Used for instances of

InheritDocTree

representing an @inheritDoc tag.

LINK

```java
public static final
DocTree.Kind
LINK
```

Used for instances of

LinkTree

representing an @link tag.

---

#### LINK

public static final

DocTree.Kind

LINK

Used for instances of

LinkTree

representing an @link tag.

LINK_PLAIN

```java
public static final
DocTree.Kind
LINK_PLAIN
```

Used for instances of

LinkTree

representing an @linkplain tag.

---

#### LINK_PLAIN

public static final

DocTree.Kind

LINK_PLAIN

Used for instances of

LinkTree

representing an @linkplain tag.

LITERAL

```java
public static final
DocTree.Kind
LITERAL
```

Used for instances of

LiteralTree

representing an @literal tag.

---

#### LITERAL

public static final

DocTree.Kind

LITERAL

Used for instances of

LiteralTree

representing an @literal tag.

PARAM

```java
public static final
DocTree.Kind
PARAM
```

Used for instances of

ParamTree

representing an @param tag.

---

#### PARAM

public static final

DocTree.Kind

PARAM

Used for instances of

ParamTree

representing an @param tag.

PROVIDES

```java
public static final
DocTree.Kind
PROVIDES
```

Used for instances of

ProvidesTree

representing an @provides tag.

---

#### PROVIDES

public static final

DocTree.Kind

PROVIDES

Used for instances of

ProvidesTree

representing an @provides tag.

REFERENCE

```java
public static final
DocTree.Kind
REFERENCE
```

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

---

#### REFERENCE

public static final

DocTree.Kind

REFERENCE

Used for instances of

ReferenceTree

representing a reference to a element in the
Java programming language.

RETURN

```java
public static final
DocTree.Kind
RETURN
```

Used for instances of

ReturnTree

representing an @return tag.

---

#### RETURN

public static final

DocTree.Kind

RETURN

Used for instances of

ReturnTree

representing an @return tag.

SEE

```java
public static final
DocTree.Kind
SEE
```

Used for instances of

SeeTree

representing an @see tag.

---

#### SEE

public static final

DocTree.Kind

SEE

Used for instances of

SeeTree

representing an @see tag.

SERIAL

```java
public static final
DocTree.Kind
SERIAL
```

Used for instances of

SerialTree

representing an @serial tag.

---

#### SERIAL

public static final

DocTree.Kind

SERIAL

Used for instances of

SerialTree

representing an @serial tag.

SERIAL_DATA

```java
public static final
DocTree.Kind
SERIAL_DATA
```

Used for instances of

SerialDataTree

representing an @serialData tag.

---

#### SERIAL_DATA

public static final

DocTree.Kind

SERIAL_DATA

Used for instances of

SerialDataTree

representing an @serialData tag.

SERIAL_FIELD

```java
public static final
DocTree.Kind
SERIAL_FIELD
```

Used for instances of

SerialFieldTree

representing an @serialField tag.

---

#### SERIAL_FIELD

public static final

DocTree.Kind

SERIAL_FIELD

Used for instances of

SerialFieldTree

representing an @serialField tag.

SINCE

```java
public static final
DocTree.Kind
SINCE
```

Used for instances of

SinceTree

representing an @since tag.

---

#### SINCE

public static final

DocTree.Kind

SINCE

Used for instances of

SinceTree

representing an @since tag.

START_ELEMENT

```java
public static final
DocTree.Kind
START_ELEMENT
```

Used for instances of

EndElementTree

representing the start of an HTML element.

---

#### START_ELEMENT

public static final

DocTree.Kind

START_ELEMENT

Used for instances of

EndElementTree

representing the start of an HTML element.

SUMMARY

```java
public static final
DocTree.Kind
SUMMARY
```

Used for instances of

SummaryTree

representing the summary of a comment description.

---

#### SUMMARY

public static final

DocTree.Kind

SUMMARY

Used for instances of

SummaryTree

representing the summary of a comment description.

TEXT

```java
public static final
DocTree.Kind
TEXT
```

Used for instances of

TextTree

representing some documentation text.

---

#### TEXT

public static final

DocTree.Kind

TEXT

Used for instances of

TextTree

representing some documentation text.

THROWS

```java
public static final
DocTree.Kind
THROWS
```

Used for instances of

ThrowsTree

representing an @throws tag.

---

#### THROWS

public static final

DocTree.Kind

THROWS

Used for instances of

ThrowsTree

representing an @throws tag.

UNKNOWN_BLOCK_TAG

```java
public static final
DocTree.Kind
UNKNOWN_BLOCK_TAG
```

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

---

#### UNKNOWN_BLOCK_TAG

public static final

DocTree.Kind

UNKNOWN_BLOCK_TAG

Used for instances of

UnknownBlockTagTree

representing an unknown block tag.

UNKNOWN_INLINE_TAG

```java
public static final
DocTree.Kind
UNKNOWN_INLINE_TAG
```

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

---

#### UNKNOWN_INLINE_TAG

public static final

DocTree.Kind

UNKNOWN_INLINE_TAG

Used for instances of

UnknownInlineTagTree

representing an unknown inline tag.

USES

```java
public static final
DocTree.Kind
USES
```

Used for instances of

UsesTree

representing an @uses tag.

---

#### USES

public static final

DocTree.Kind

USES

Used for instances of

UsesTree

representing an @uses tag.

VALUE

```java
public static final
DocTree.Kind
VALUE
```

Used for instances of

ValueTree

representing an @value tag.

---

#### VALUE

public static final

DocTree.Kind

VALUE

Used for instances of

ValueTree

representing an @value tag.

VERSION

```java
public static final
DocTree.Kind
VERSION
```

Used for instances of

VersionTree

representing an @version tag.

---

#### VERSION

public static final

DocTree.Kind

VERSION

Used for instances of

VersionTree

representing an @version tag.

OTHER

```java
public static final
DocTree.Kind
OTHER
```

An implementation-reserved node. This is the not the node
you are looking for.

---

#### OTHER

public static final

DocTree.Kind

OTHER

An implementation-reserved node. This is the not the node
you are looking for.

Field Detail

- tagName

```java
public final
String
tagName
```

The name of the tag, if any, associated with this kind of node.

---

#### Field Detail

tagName

```java
public final
String
tagName
```

The name of the tag, if any, associated with this kind of node.

---

#### tagName

public final

String

tagName

The name of the tag, if any, associated with this kind of node.

Method Detail

- values

```java
public static
DocTree.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocTree.Kind c : DocTree.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DocTree.Kind
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
DocTree.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocTree.Kind c : DocTree.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

DocTree.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DocTree.Kind c : DocTree.Kind.values())
System.out.println(c);
```

for (DocTree.Kind c : DocTree.Kind.values())
System.out.println(c);

valueOf

```java
public static
DocTree.Kind
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

DocTree.Kind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

