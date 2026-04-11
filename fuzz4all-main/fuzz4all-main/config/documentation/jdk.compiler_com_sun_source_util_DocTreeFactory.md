# Interface DocTreeFactory

**Source:** `jdk.compiler\com\sun\source\util\DocTreeFactory.html`

### Class Description

```java
public interface
DocTreeFactory
```

Factory for creating

DocTree

nodes.

**Implementation Note:** The methods in an implementation of this interface may only accept

DocTree

nodes that have been created by the same implementation.
**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AttributeTree
newAttributeTree​(
Name
name,

AttributeTree.ValueKind
vkind,

List
<? extends
DocTree
> value)

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

**Parameters:**
- name

- the name of the attribute
- vkind

- the kind of attribute value
- value

- the value, if any, of the attribute

**Returns:**
- an

AttributeTree

object

---

#### AuthorTree
newAuthorTree​(
List
<? extends
DocTree
> name)

Create a new

AuthorTree

object, to represent an

{@author }

tag.

**Parameters:**
- name

- the name of the author

**Returns:**
- an

AuthorTree

object

---

#### LiteralTree
newCodeTree​(
TextTree
text)

Create a new

CodeTree

object, to represent a

{@code }

tag.

**Parameters:**
- text

- the content of the tag

**Returns:**
- a

CodeTree

object

---

#### CommentTree
newCommentTree​(
String
text)

Create a new

CommentTree

, to represent an HTML comment.

**Parameters:**
- text

- the content of the comment

**Returns:**
- a

CommentTree

object

---

#### DeprecatedTree
newDeprecatedTree​(
List
<? extends
DocTree
> text)

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

**Parameters:**
- text

- the content of the tag

**Returns:**
- a

DeprecatedTree

object

---

#### DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags)

Create a new

DocCommentTree

object, to represent a complete doc comment.

**Parameters:**
- fullBody

- the entire body of the doc comment
- tags

- the block tags in the doc comment

**Returns:**
- a

DocCommentTree

object

---

#### DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags,

List
<? extends
DocTree
> preamble,

List
<? extends
DocTree
> postamble)

Create a new

DocCommentTree

object, to represent the enitire doc comment.

**Parameters:**
- fullBody

- the entire body of the doc comment
- tags

- the block tags in the doc comment
- preamble

- the meta content of an html file including the body tag
- postamble

- the meta content of an html including the closing body tag

**Returns:**
- a

DocCommentTree

object

**Since:**
- 10

---

#### DocRootTree
newDocRootTree()

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

**Returns:**
- a

DocRootTree

object

---

#### DocTypeTree
newDocTypeTree​(
String
text)

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

**Parameters:**
- text

- the content of the declaration

**Returns:**
- a

CommentTree

object

**Since:**
- 10

---

#### EndElementTree
newEndElementTree​(
Name
name)

Create a new

EndElement

object, to represent the end of an HTML element.

**Parameters:**
- name

- the name of the HTML element

**Returns:**
- an

EndElementTree

object

---

#### EntityTree
newEntityTree​(
Name
name)

Create a new

EntityTree

object, to represent an HTML entity.

**Parameters:**
- name

- the name of the entity, representing the characters between '<' and ';'
in the representation of the entity in an HTML document

**Returns:**
- an

EntityTree

object

---

#### ErroneousTree
newErroneousTree​(
String
text,

Diagnostic
<
JavaFileObject
> diag)

Create a new

ErroneousTree

object, to represent some unparseable input.

**Parameters:**
- text

- the unparseable text
- diag

- a diagnostic associated with the unparseable text, or null

**Returns:**
- an

ErroneousTree

object

---

#### ThrowsTree
newExceptionTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)

Create a new

ExceptionTree

object, to represent an

@exception

tag.

**Parameters:**
- name

- the name of the exception
- description

- a description of why the exception might be thrown

**Returns:**
- an

ExceptionTree

object

---

#### HiddenTree
newHiddenTree​(
List
<? extends
DocTree
> text)

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

**Parameters:**
- text

- the content of the tag

**Returns:**
- a

HiddenTree

object

---

#### IdentifierTree
newIdentifierTree​(
Name
name)

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

**Parameters:**
- name

- the name of the identifier

**Returns:**
- an

IdentifierTree

object

---

#### IndexTree
newIndexTree​(
DocTree
term,

List
<? extends
DocTree
> description)

Create a new

IndexTree

object, to represent an

{@index }

tag.

**Parameters:**
- term

- the search term
- description

- an optional description of the search term

**Returns:**
- an

IndexTree

object

---

#### InheritDocTree
newInheritDocTree()

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

**Returns:**
- an

InheritDocTree

object

---

#### LinkTree
newLinkTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)

Create a new

LinkTree

object, to represent a

{@link }

tag.

**Parameters:**
- ref

- the API element being referenced
- label

- an optional label for the link

**Returns:**
- a

LinkTree

object

---

#### LinkTree
newLinkPlainTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

**Parameters:**
- ref

- the API element being referenced
- label

- an optional label for the link

**Returns:**
- a

LinkPlainTree

object

---

#### LiteralTree
newLiteralTree​(
TextTree
text)

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

**Parameters:**
- text

- the content of the tag

**Returns:**
- a

LiteralTree

object

---

#### ParamTree
newParamTree​(boolean isTypeParameter,

IdentifierTree
name,

List
<? extends
DocTree
> description)

Create a new

ParamTree

object, to represent a

@param

tag.

**Parameters:**
- isTypeParameter

- true if this is a type parameter, and false otherwise
- name

- the parameter being described
- description

- the description of the parameter

**Returns:**
- a

ParamTree

object

---

#### ProvidesTree
newProvidesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)

Create a new

ProvidesTree

object, to represent a

@provides

tag.

**Parameters:**
- name

- the name of the service type
- description

- a description of the service being provided

**Returns:**
- a

ProvidesTree

object

---

#### ReferenceTree
newReferenceTree​(
String
signature)

Create a new

ReferenceTree

object, to represent a reference to an API element.

**Parameters:**
- signature

- the doc comment signature of the reference

**Returns:**
- a

ReferenceTree

object

---

#### ReturnTree
newReturnTree​(
List
<? extends
DocTree
> description)

Create a new

ReturnTree

object, to represent a

@return

tag.

**Parameters:**
- description

- the description of the return value of a method

**Returns:**
- a

ReturnTree

object

---

#### SeeTree
newSeeTree​(
List
<? extends
DocTree
> reference)

Create a new

SeeTree

object, to represent a

@see

tag.

**Parameters:**
- reference

- the reference

**Returns:**
- a

SeeTree

object

---

#### SerialTree
newSerialTree​(
List
<? extends
DocTree
> description)

Create a new

SerialTree

object, to represent a

@serial

tag.

**Parameters:**
- description

- the description for the tag

**Returns:**
- a

SerialTree

object

---

#### SerialDataTree
newSerialDataTree​(
List
<? extends
DocTree
> description)

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

**Parameters:**
- description

- the description for the tag

**Returns:**
- a

SerialDataTree

object

---

#### SerialFieldTree
newSerialFieldTree​(
IdentifierTree
name,

ReferenceTree
type,

List
<? extends
DocTree
> description)

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

**Parameters:**
- name

- the name of the field
- type

- the type of the field
- description

- the description of the field

**Returns:**
- a

SerialFieldTree

object

---

#### SinceTree
newSinceTree​(
List
<? extends
DocTree
> text)

Create a new

SinceTree

object, to represent a

@since

tag.

**Parameters:**
- text

- the content of the tag

**Returns:**
- a

SinceTree

object

---

#### StartElementTree
newStartElementTree​(
Name
name,

List
<? extends
DocTree
> attrs,
boolean selfClosing)

Create a new

StartElementTree

object, to represent the start of an HTML element.

**Parameters:**
- name

- the name of the HTML element
- attrs

- the attributes
- selfClosing

- true if the start element is marked as self-closing; otherwise false

**Returns:**
- a

StartElementTree

object

---

#### default
SummaryTree
newSummaryTree​(
List
<? extends
DocTree
> summary)

Create a new

SummaryTree

object, to represent a

@summary

tag.

**Parameters:**
- summary

- the content of the tag

**Returns:**
- a

SummaryTree

object

**Since:**
- 10

**Implementation Requirements:**
- This implementation throws

UnsupportedOperationException

.

---

#### TextTree
newTextTree​(
String
text)

Create a new

TextTree

object, to represent some plain text.

**Parameters:**
- text

- the text

**Returns:**
- a

TextTree

object

---

#### ThrowsTree
newThrowsTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)

Create a new

ThrowsTree

object, to represent a

@throws

tag.

**Parameters:**
- name

- the name of the exception
- description

- a description of why the exception might be thrown

**Returns:**
- a

ThrowsTree

object

---

#### UnknownBlockTagTree
newUnknownBlockTagTree​(
Name
name,

List
<? extends
DocTree
> content)

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

**Parameters:**
- name

- the name of the block tag
- content

- the content

**Returns:**
- an

UnknownBlockTagTree

object

---

#### UnknownInlineTagTree
newUnknownInlineTagTree​(
Name
name,

List
<? extends
DocTree
> content)

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

**Parameters:**
- name

- the name of the inline tag
- content

- the content

**Returns:**
- an

UnknownInlineTagTree

object

---

#### UsesTree
newUsesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)

Create a new

UsesTree

object, to represent a

@uses

tag.

**Parameters:**
- name

- the name of the service type
- description

- a description of how the service will be used

**Returns:**
- a

UsesTree

object

---

#### ValueTree
newValueTree​(
ReferenceTree
ref)

Create a new

ValueTree

object, to represent a

{@value }

tag.

**Parameters:**
- ref

- a reference to the value

**Returns:**
- a

ValueTree

object

---

#### VersionTree
newVersionTree​(
List
<? extends
DocTree
> text)

Create a new

VersionTree

object, to represent a

{@version }

tag.

**Parameters:**
- text

- the content of the tag

**Returns:**
- a

VersionTree

object

---

#### DocTreeFactory
at​(int pos)

Set the position to be recorded in subsequent tree nodes created by this factory.
The position should be a character offset relative to the beginning of the source file
or

NOPOS

.

**Parameters:**
- pos

- the position

**Returns:**
- this object, to facilitate method chaining

---

#### List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)

Get the first sentence contained in a list of content.
The determination of the first sentence is implementation specific, and may
involve the use of a locale-specific

BreakIterator

and other heuristics.
The resulting list may share a common set of initial items with the input list.

**Parameters:**
- list

- the list

**Returns:**
- a list containing the first sentence of the list.

---

### Additional Sections

#### Interface DocTreeFactory

```java
public interface
DocTreeFactory
```

Factory for creating

DocTree

nodes.

**Implementation Note:** The methods in an implementation of this interface may only accept

DocTree

nodes that have been created by the same implementation.
**Since:** 9

public interface

DocTreeFactory

Factory for creating

DocTree

nodes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

DocTreeFactory

at

​(int pos)

Set the position to be recorded in subsequent tree nodes created by this factory.

List

<

DocTree

>

getFirstSentence

​(

List

<? extends

DocTree

> list)

Get the first sentence contained in a list of content.

AttributeTree

newAttributeTree

​(

Name

name,

AttributeTree.ValueKind

vkind,

List

<? extends

DocTree

> value)

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

AuthorTree

newAuthorTree

​(

List

<? extends

DocTree

> name)

Create a new

AuthorTree

object, to represent an

{@author }

tag.

LiteralTree

newCodeTree

​(

TextTree

text)

Create a new

CodeTree

object, to represent a

{@code }

tag.

CommentTree

newCommentTree

​(

String

text)

Create a new

CommentTree

, to represent an HTML comment.

DeprecatedTree

newDeprecatedTree

​(

List

<? extends

DocTree

> text)

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

DocCommentTree

newDocCommentTree

​(

List

<? extends

DocTree

> fullBody,

List

<? extends

DocTree

> tags)

Create a new

DocCommentTree

object, to represent a complete doc comment.

DocCommentTree

newDocCommentTree

​(

List

<? extends

DocTree

> fullBody,

List

<? extends

DocTree

> tags,

List

<? extends

DocTree

> preamble,

List

<? extends

DocTree

> postamble)

Create a new

DocCommentTree

object, to represent the enitire doc comment.

DocRootTree

newDocRootTree

()

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

DocTypeTree

newDocTypeTree

​(

String

text)

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

EndElementTree

newEndElementTree

​(

Name

name)

Create a new

EndElement

object, to represent the end of an HTML element.

EntityTree

newEntityTree

​(

Name

name)

Create a new

EntityTree

object, to represent an HTML entity.

ErroneousTree

newErroneousTree

​(

String

text,

Diagnostic

<

JavaFileObject

> diag)

Create a new

ErroneousTree

object, to represent some unparseable input.

ThrowsTree

newExceptionTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ExceptionTree

object, to represent an

@exception

tag.

HiddenTree

newHiddenTree

​(

List

<? extends

DocTree

> text)

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

IdentifierTree

newIdentifierTree

​(

Name

name)

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

IndexTree

newIndexTree

​(

DocTree

term,

List

<? extends

DocTree

> description)

Create a new

IndexTree

object, to represent an

{@index }

tag.

InheritDocTree

newInheritDocTree

()

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

LinkTree

newLinkPlainTree

​(

ReferenceTree

ref,

List

<? extends

DocTree

> label)

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

LinkTree

newLinkTree

​(

ReferenceTree

ref,

List

<? extends

DocTree

> label)

Create a new

LinkTree

object, to represent a

{@link }

tag.

LiteralTree

newLiteralTree

​(

TextTree

text)

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

ParamTree

newParamTree

​(boolean isTypeParameter,

IdentifierTree

name,

List

<? extends

DocTree

> description)

Create a new

ParamTree

object, to represent a

@param

tag.

ProvidesTree

newProvidesTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ProvidesTree

object, to represent a

@provides

tag.

ReferenceTree

newReferenceTree

​(

String

signature)

Create a new

ReferenceTree

object, to represent a reference to an API element.

ReturnTree

newReturnTree

​(

List

<? extends

DocTree

> description)

Create a new

ReturnTree

object, to represent a

@return

tag.

SeeTree

newSeeTree

​(

List

<? extends

DocTree

> reference)

Create a new

SeeTree

object, to represent a

@see

tag.

SerialDataTree

newSerialDataTree

​(

List

<? extends

DocTree

> description)

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

SerialFieldTree

newSerialFieldTree

​(

IdentifierTree

name,

ReferenceTree

type,

List

<? extends

DocTree

> description)

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

SerialTree

newSerialTree

​(

List

<? extends

DocTree

> description)

Create a new

SerialTree

object, to represent a

@serial

tag.

SinceTree

newSinceTree

​(

List

<? extends

DocTree

> text)

Create a new

SinceTree

object, to represent a

@since

tag.

StartElementTree

newStartElementTree

​(

Name

name,

List

<? extends

DocTree

> attrs,
boolean selfClosing)

Create a new

StartElementTree

object, to represent the start of an HTML element.

default

SummaryTree

newSummaryTree

​(

List

<? extends

DocTree

> summary)

Create a new

SummaryTree

object, to represent a

@summary

tag.

TextTree

newTextTree

​(

String

text)

Create a new

TextTree

object, to represent some plain text.

ThrowsTree

newThrowsTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ThrowsTree

object, to represent a

@throws

tag.

UnknownBlockTagTree

newUnknownBlockTagTree

​(

Name

name,

List

<? extends

DocTree

> content)

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

UnknownInlineTagTree

newUnknownInlineTagTree

​(

Name

name,

List

<? extends

DocTree

> content)

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

UsesTree

newUsesTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

UsesTree

object, to represent a

@uses

tag.

ValueTree

newValueTree

​(

ReferenceTree

ref)

Create a new

ValueTree

object, to represent a

{@value }

tag.

VersionTree

newVersionTree

​(

List

<? extends

DocTree

> text)

Create a new

VersionTree

object, to represent a

{@version }

tag.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

DocTreeFactory

at

​(int pos)

Set the position to be recorded in subsequent tree nodes created by this factory.

List

<

DocTree

>

getFirstSentence

​(

List

<? extends

DocTree

> list)

Get the first sentence contained in a list of content.

AttributeTree

newAttributeTree

​(

Name

name,

AttributeTree.ValueKind

vkind,

List

<? extends

DocTree

> value)

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

AuthorTree

newAuthorTree

​(

List

<? extends

DocTree

> name)

Create a new

AuthorTree

object, to represent an

{@author }

tag.

LiteralTree

newCodeTree

​(

TextTree

text)

Create a new

CodeTree

object, to represent a

{@code }

tag.

CommentTree

newCommentTree

​(

String

text)

Create a new

CommentTree

, to represent an HTML comment.

DeprecatedTree

newDeprecatedTree

​(

List

<? extends

DocTree

> text)

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

DocCommentTree

newDocCommentTree

​(

List

<? extends

DocTree

> fullBody,

List

<? extends

DocTree

> tags)

Create a new

DocCommentTree

object, to represent a complete doc comment.

DocCommentTree

newDocCommentTree

​(

List

<? extends

DocTree

> fullBody,

List

<? extends

DocTree

> tags,

List

<? extends

DocTree

> preamble,

List

<? extends

DocTree

> postamble)

Create a new

DocCommentTree

object, to represent the enitire doc comment.

DocRootTree

newDocRootTree

()

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

DocTypeTree

newDocTypeTree

​(

String

text)

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

EndElementTree

newEndElementTree

​(

Name

name)

Create a new

EndElement

object, to represent the end of an HTML element.

EntityTree

newEntityTree

​(

Name

name)

Create a new

EntityTree

object, to represent an HTML entity.

ErroneousTree

newErroneousTree

​(

String

text,

Diagnostic

<

JavaFileObject

> diag)

Create a new

ErroneousTree

object, to represent some unparseable input.

ThrowsTree

newExceptionTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ExceptionTree

object, to represent an

@exception

tag.

HiddenTree

newHiddenTree

​(

List

<? extends

DocTree

> text)

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

IdentifierTree

newIdentifierTree

​(

Name

name)

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

IndexTree

newIndexTree

​(

DocTree

term,

List

<? extends

DocTree

> description)

Create a new

IndexTree

object, to represent an

{@index }

tag.

InheritDocTree

newInheritDocTree

()

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

LinkTree

newLinkPlainTree

​(

ReferenceTree

ref,

List

<? extends

DocTree

> label)

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

LinkTree

newLinkTree

​(

ReferenceTree

ref,

List

<? extends

DocTree

> label)

Create a new

LinkTree

object, to represent a

{@link }

tag.

LiteralTree

newLiteralTree

​(

TextTree

text)

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

ParamTree

newParamTree

​(boolean isTypeParameter,

IdentifierTree

name,

List

<? extends

DocTree

> description)

Create a new

ParamTree

object, to represent a

@param

tag.

ProvidesTree

newProvidesTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ProvidesTree

object, to represent a

@provides

tag.

ReferenceTree

newReferenceTree

​(

String

signature)

Create a new

ReferenceTree

object, to represent a reference to an API element.

ReturnTree

newReturnTree

​(

List

<? extends

DocTree

> description)

Create a new

ReturnTree

object, to represent a

@return

tag.

SeeTree

newSeeTree

​(

List

<? extends

DocTree

> reference)

Create a new

SeeTree

object, to represent a

@see

tag.

SerialDataTree

newSerialDataTree

​(

List

<? extends

DocTree

> description)

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

SerialFieldTree

newSerialFieldTree

​(

IdentifierTree

name,

ReferenceTree

type,

List

<? extends

DocTree

> description)

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

SerialTree

newSerialTree

​(

List

<? extends

DocTree

> description)

Create a new

SerialTree

object, to represent a

@serial

tag.

SinceTree

newSinceTree

​(

List

<? extends

DocTree

> text)

Create a new

SinceTree

object, to represent a

@since

tag.

StartElementTree

newStartElementTree

​(

Name

name,

List

<? extends

DocTree

> attrs,
boolean selfClosing)

Create a new

StartElementTree

object, to represent the start of an HTML element.

default

SummaryTree

newSummaryTree

​(

List

<? extends

DocTree

> summary)

Create a new

SummaryTree

object, to represent a

@summary

tag.

TextTree

newTextTree

​(

String

text)

Create a new

TextTree

object, to represent some plain text.

ThrowsTree

newThrowsTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ThrowsTree

object, to represent a

@throws

tag.

UnknownBlockTagTree

newUnknownBlockTagTree

​(

Name

name,

List

<? extends

DocTree

> content)

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

UnknownInlineTagTree

newUnknownInlineTagTree

​(

Name

name,

List

<? extends

DocTree

> content)

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

UsesTree

newUsesTree

​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

UsesTree

object, to represent a

@uses

tag.

ValueTree

newValueTree

​(

ReferenceTree

ref)

Create a new

ValueTree

object, to represent a

{@value }

tag.

VersionTree

newVersionTree

​(

List

<? extends

DocTree

> text)

Create a new

VersionTree

object, to represent a

{@version }

tag.

---

#### Method Summary

Set the position to be recorded in subsequent tree nodes created by this factory.

Get the first sentence contained in a list of content.

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

Create a new

AuthorTree

object, to represent an

{@author }

tag.

Create a new

CodeTree

object, to represent a

{@code }

tag.

Create a new

CommentTree

, to represent an HTML comment.

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

Create a new

DocCommentTree

object, to represent a complete doc comment.

Create a new

DocCommentTree

object, to represent the enitire doc comment.

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

Create a new

EndElement

object, to represent the end of an HTML element.

Create a new

EntityTree

object, to represent an HTML entity.

Create a new

ErroneousTree

object, to represent some unparseable input.

Create a new

ExceptionTree

object, to represent an

@exception

tag.

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

Create a new

IndexTree

object, to represent an

{@index }

tag.

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

Create a new

LinkTree

object, to represent a

{@link }

tag.

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

Create a new

ParamTree

object, to represent a

@param

tag.

Create a new

ProvidesTree

object, to represent a

@provides

tag.

Create a new

ReferenceTree

object, to represent a reference to an API element.

Create a new

ReturnTree

object, to represent a

@return

tag.

Create a new

SeeTree

object, to represent a

@see

tag.

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

Create a new

SerialTree

object, to represent a

@serial

tag.

Create a new

SinceTree

object, to represent a

@since

tag.

Create a new

StartElementTree

object, to represent the start of an HTML element.

Create a new

SummaryTree

object, to represent a

@summary

tag.

Create a new

TextTree

object, to represent some plain text.

Create a new

ThrowsTree

object, to represent a

@throws

tag.

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

Create a new

UsesTree

object, to represent a

@uses

tag.

Create a new

ValueTree

object, to represent a

{@value }

tag.

Create a new

VersionTree

object, to represent a

{@version }

tag.

============ METHOD DETAIL ==========

- Method Detail

- newAttributeTree

```java
AttributeTree
newAttributeTree​(
Name
name,

AttributeTree.ValueKind
vkind,

List
<? extends
DocTree
> value)
```

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

**Parameters:** name

- the name of the attribute
**Parameters:** vkind

- the kind of attribute value
**Parameters:** value

- the value, if any, of the attribute
**Returns:** an

AttributeTree

object

- newAuthorTree

```java
AuthorTree
newAuthorTree​(
List
<? extends
DocTree
> name)
```

Create a new

AuthorTree

object, to represent an

{@author }

tag.

**Parameters:** name

- the name of the author
**Returns:** an

AuthorTree

object

- newCodeTree

```java
LiteralTree
newCodeTree​(
TextTree
text)
```

Create a new

CodeTree

object, to represent a

{@code }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

CodeTree

object

- newCommentTree

```java
CommentTree
newCommentTree​(
String
text)
```

Create a new

CommentTree

, to represent an HTML comment.

**Parameters:** text

- the content of the comment
**Returns:** a

CommentTree

object

- newDeprecatedTree

```java
DeprecatedTree
newDeprecatedTree​(
List
<? extends
DocTree
> text)
```

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

DeprecatedTree

object

- newDocCommentTree

```java
DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags)
```

Create a new

DocCommentTree

object, to represent a complete doc comment.

**Parameters:** fullBody

- the entire body of the doc comment
**Parameters:** tags

- the block tags in the doc comment
**Returns:** a

DocCommentTree

object

- newDocCommentTree

```java
DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags,

List
<? extends
DocTree
> preamble,

List
<? extends
DocTree
> postamble)
```

Create a new

DocCommentTree

object, to represent the enitire doc comment.

**Parameters:** fullBody

- the entire body of the doc comment
**Parameters:** tags

- the block tags in the doc comment
**Parameters:** preamble

- the meta content of an html file including the body tag
**Parameters:** postamble

- the meta content of an html including the closing body tag
**Returns:** a

DocCommentTree

object
**Since:** 10

- newDocRootTree

```java
DocRootTree
newDocRootTree()
```

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

**Returns:** a

DocRootTree

object

- newDocTypeTree

```java
DocTypeTree
newDocTypeTree​(
String
text)
```

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

**Parameters:** text

- the content of the declaration
**Returns:** a

CommentTree

object
**Since:** 10

- newEndElementTree

```java
EndElementTree
newEndElementTree​(
Name
name)
```

Create a new

EndElement

object, to represent the end of an HTML element.

**Parameters:** name

- the name of the HTML element
**Returns:** an

EndElementTree

object

- newEntityTree

```java
EntityTree
newEntityTree​(
Name
name)
```

Create a new

EntityTree

object, to represent an HTML entity.

**Parameters:** name

- the name of the entity, representing the characters between '<' and ';'
in the representation of the entity in an HTML document
**Returns:** an

EntityTree

object

- newErroneousTree

```java
ErroneousTree
newErroneousTree​(
String
text,

Diagnostic
<
JavaFileObject
> diag)
```

Create a new

ErroneousTree

object, to represent some unparseable input.

**Parameters:** text

- the unparseable text
**Parameters:** diag

- a diagnostic associated with the unparseable text, or null
**Returns:** an

ErroneousTree

object

- newExceptionTree

```java
ThrowsTree
newExceptionTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ExceptionTree

object, to represent an

@exception

tag.

**Parameters:** name

- the name of the exception
**Parameters:** description

- a description of why the exception might be thrown
**Returns:** an

ExceptionTree

object

- newHiddenTree

```java
HiddenTree
newHiddenTree​(
List
<? extends
DocTree
> text)
```

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

HiddenTree

object

- newIdentifierTree

```java
IdentifierTree
newIdentifierTree​(
Name
name)
```

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

**Parameters:** name

- the name of the identifier
**Returns:** an

IdentifierTree

object

- newIndexTree

```java
IndexTree
newIndexTree​(
DocTree
term,

List
<? extends
DocTree
> description)
```

Create a new

IndexTree

object, to represent an

{@index }

tag.

**Parameters:** term

- the search term
**Parameters:** description

- an optional description of the search term
**Returns:** an

IndexTree

object

- newInheritDocTree

```java
InheritDocTree
newInheritDocTree()
```

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

**Returns:** an

InheritDocTree

object

- newLinkTree

```java
LinkTree
newLinkTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)
```

Create a new

LinkTree

object, to represent a

{@link }

tag.

**Parameters:** ref

- the API element being referenced
**Parameters:** label

- an optional label for the link
**Returns:** a

LinkTree

object

- newLinkPlainTree

```java
LinkTree
newLinkPlainTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)
```

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

**Parameters:** ref

- the API element being referenced
**Parameters:** label

- an optional label for the link
**Returns:** a

LinkPlainTree

object

- newLiteralTree

```java
LiteralTree
newLiteralTree​(
TextTree
text)
```

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

LiteralTree

object

- newParamTree

```java
ParamTree
newParamTree​(boolean isTypeParameter,

IdentifierTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ParamTree

object, to represent a

@param

tag.

**Parameters:** isTypeParameter

- true if this is a type parameter, and false otherwise
**Parameters:** name

- the parameter being described
**Parameters:** description

- the description of the parameter
**Returns:** a

ParamTree

object

- newProvidesTree

```java
ProvidesTree
newProvidesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ProvidesTree

object, to represent a

@provides

tag.

**Parameters:** name

- the name of the service type
**Parameters:** description

- a description of the service being provided
**Returns:** a

ProvidesTree

object

- newReferenceTree

```java
ReferenceTree
newReferenceTree​(
String
signature)
```

Create a new

ReferenceTree

object, to represent a reference to an API element.

**Parameters:** signature

- the doc comment signature of the reference
**Returns:** a

ReferenceTree

object

- newReturnTree

```java
ReturnTree
newReturnTree​(
List
<? extends
DocTree
> description)
```

Create a new

ReturnTree

object, to represent a

@return

tag.

**Parameters:** description

- the description of the return value of a method
**Returns:** a

ReturnTree

object

- newSeeTree

```java
SeeTree
newSeeTree​(
List
<? extends
DocTree
> reference)
```

Create a new

SeeTree

object, to represent a

@see

tag.

**Parameters:** reference

- the reference
**Returns:** a

SeeTree

object

- newSerialTree

```java
SerialTree
newSerialTree​(
List
<? extends
DocTree
> description)
```

Create a new

SerialTree

object, to represent a

@serial

tag.

**Parameters:** description

- the description for the tag
**Returns:** a

SerialTree

object

- newSerialDataTree

```java
SerialDataTree
newSerialDataTree​(
List
<? extends
DocTree
> description)
```

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

**Parameters:** description

- the description for the tag
**Returns:** a

SerialDataTree

object

- newSerialFieldTree

```java
SerialFieldTree
newSerialFieldTree​(
IdentifierTree
name,

ReferenceTree
type,

List
<? extends
DocTree
> description)
```

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Parameters:** description

- the description of the field
**Returns:** a

SerialFieldTree

object

- newSinceTree

```java
SinceTree
newSinceTree​(
List
<? extends
DocTree
> text)
```

Create a new

SinceTree

object, to represent a

@since

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

SinceTree

object

- newStartElementTree

```java
StartElementTree
newStartElementTree​(
Name
name,

List
<? extends
DocTree
> attrs,
boolean selfClosing)
```

Create a new

StartElementTree

object, to represent the start of an HTML element.

**Parameters:** name

- the name of the HTML element
**Parameters:** attrs

- the attributes
**Parameters:** selfClosing

- true if the start element is marked as self-closing; otherwise false
**Returns:** a

StartElementTree

object

- newSummaryTree

```java
default
SummaryTree
newSummaryTree​(
List
<? extends
DocTree
> summary)
```

Create a new

SummaryTree

object, to represent a

@summary

tag.

**Implementation Requirements:** This implementation throws

UnsupportedOperationException

.
**Parameters:** summary

- the content of the tag
**Returns:** a

SummaryTree

object
**Since:** 10

- newTextTree

```java
TextTree
newTextTree​(
String
text)
```

Create a new

TextTree

object, to represent some plain text.

**Parameters:** text

- the text
**Returns:** a

TextTree

object

- newThrowsTree

```java
ThrowsTree
newThrowsTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ThrowsTree

object, to represent a

@throws

tag.

**Parameters:** name

- the name of the exception
**Parameters:** description

- a description of why the exception might be thrown
**Returns:** a

ThrowsTree

object

- newUnknownBlockTagTree

```java
UnknownBlockTagTree
newUnknownBlockTagTree​(
Name
name,

List
<? extends
DocTree
> content)
```

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

**Parameters:** name

- the name of the block tag
**Parameters:** content

- the content
**Returns:** an

UnknownBlockTagTree

object

- newUnknownInlineTagTree

```java
UnknownInlineTagTree
newUnknownInlineTagTree​(
Name
name,

List
<? extends
DocTree
> content)
```

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

**Parameters:** name

- the name of the inline tag
**Parameters:** content

- the content
**Returns:** an

UnknownInlineTagTree

object

- newUsesTree

```java
UsesTree
newUsesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

UsesTree

object, to represent a

@uses

tag.

**Parameters:** name

- the name of the service type
**Parameters:** description

- a description of how the service will be used
**Returns:** a

UsesTree

object

- newValueTree

```java
ValueTree
newValueTree​(
ReferenceTree
ref)
```

Create a new

ValueTree

object, to represent a

{@value }

tag.

**Parameters:** ref

- a reference to the value
**Returns:** a

ValueTree

object

- newVersionTree

```java
VersionTree
newVersionTree​(
List
<? extends
DocTree
> text)
```

Create a new

VersionTree

object, to represent a

{@version }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

VersionTree

object

- at

```java
DocTreeFactory
at​(int pos)
```

Set the position to be recorded in subsequent tree nodes created by this factory.
The position should be a character offset relative to the beginning of the source file
or

NOPOS

.

**Parameters:** pos

- the position
**Returns:** this object, to facilitate method chaining

- getFirstSentence

```java
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)
```

Get the first sentence contained in a list of content.
The determination of the first sentence is implementation specific, and may
involve the use of a locale-specific

BreakIterator

and other heuristics.
The resulting list may share a common set of initial items with the input list.

**Parameters:** list

- the list
**Returns:** a list containing the first sentence of the list.

Method Detail

- newAttributeTree

```java
AttributeTree
newAttributeTree​(
Name
name,

AttributeTree.ValueKind
vkind,

List
<? extends
DocTree
> value)
```

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

**Parameters:** name

- the name of the attribute
**Parameters:** vkind

- the kind of attribute value
**Parameters:** value

- the value, if any, of the attribute
**Returns:** an

AttributeTree

object

- newAuthorTree

```java
AuthorTree
newAuthorTree​(
List
<? extends
DocTree
> name)
```

Create a new

AuthorTree

object, to represent an

{@author }

tag.

**Parameters:** name

- the name of the author
**Returns:** an

AuthorTree

object

- newCodeTree

```java
LiteralTree
newCodeTree​(
TextTree
text)
```

Create a new

CodeTree

object, to represent a

{@code }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

CodeTree

object

- newCommentTree

```java
CommentTree
newCommentTree​(
String
text)
```

Create a new

CommentTree

, to represent an HTML comment.

**Parameters:** text

- the content of the comment
**Returns:** a

CommentTree

object

- newDeprecatedTree

```java
DeprecatedTree
newDeprecatedTree​(
List
<? extends
DocTree
> text)
```

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

DeprecatedTree

object

- newDocCommentTree

```java
DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags)
```

Create a new

DocCommentTree

object, to represent a complete doc comment.

**Parameters:** fullBody

- the entire body of the doc comment
**Parameters:** tags

- the block tags in the doc comment
**Returns:** a

DocCommentTree

object

- newDocCommentTree

```java
DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags,

List
<? extends
DocTree
> preamble,

List
<? extends
DocTree
> postamble)
```

Create a new

DocCommentTree

object, to represent the enitire doc comment.

**Parameters:** fullBody

- the entire body of the doc comment
**Parameters:** tags

- the block tags in the doc comment
**Parameters:** preamble

- the meta content of an html file including the body tag
**Parameters:** postamble

- the meta content of an html including the closing body tag
**Returns:** a

DocCommentTree

object
**Since:** 10

- newDocRootTree

```java
DocRootTree
newDocRootTree()
```

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

**Returns:** a

DocRootTree

object

- newDocTypeTree

```java
DocTypeTree
newDocTypeTree​(
String
text)
```

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

**Parameters:** text

- the content of the declaration
**Returns:** a

CommentTree

object
**Since:** 10

- newEndElementTree

```java
EndElementTree
newEndElementTree​(
Name
name)
```

Create a new

EndElement

object, to represent the end of an HTML element.

**Parameters:** name

- the name of the HTML element
**Returns:** an

EndElementTree

object

- newEntityTree

```java
EntityTree
newEntityTree​(
Name
name)
```

Create a new

EntityTree

object, to represent an HTML entity.

**Parameters:** name

- the name of the entity, representing the characters between '<' and ';'
in the representation of the entity in an HTML document
**Returns:** an

EntityTree

object

- newErroneousTree

```java
ErroneousTree
newErroneousTree​(
String
text,

Diagnostic
<
JavaFileObject
> diag)
```

Create a new

ErroneousTree

object, to represent some unparseable input.

**Parameters:** text

- the unparseable text
**Parameters:** diag

- a diagnostic associated with the unparseable text, or null
**Returns:** an

ErroneousTree

object

- newExceptionTree

```java
ThrowsTree
newExceptionTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ExceptionTree

object, to represent an

@exception

tag.

**Parameters:** name

- the name of the exception
**Parameters:** description

- a description of why the exception might be thrown
**Returns:** an

ExceptionTree

object

- newHiddenTree

```java
HiddenTree
newHiddenTree​(
List
<? extends
DocTree
> text)
```

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

HiddenTree

object

- newIdentifierTree

```java
IdentifierTree
newIdentifierTree​(
Name
name)
```

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

**Parameters:** name

- the name of the identifier
**Returns:** an

IdentifierTree

object

- newIndexTree

```java
IndexTree
newIndexTree​(
DocTree
term,

List
<? extends
DocTree
> description)
```

Create a new

IndexTree

object, to represent an

{@index }

tag.

**Parameters:** term

- the search term
**Parameters:** description

- an optional description of the search term
**Returns:** an

IndexTree

object

- newInheritDocTree

```java
InheritDocTree
newInheritDocTree()
```

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

**Returns:** an

InheritDocTree

object

- newLinkTree

```java
LinkTree
newLinkTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)
```

Create a new

LinkTree

object, to represent a

{@link }

tag.

**Parameters:** ref

- the API element being referenced
**Parameters:** label

- an optional label for the link
**Returns:** a

LinkTree

object

- newLinkPlainTree

```java
LinkTree
newLinkPlainTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)
```

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

**Parameters:** ref

- the API element being referenced
**Parameters:** label

- an optional label for the link
**Returns:** a

LinkPlainTree

object

- newLiteralTree

```java
LiteralTree
newLiteralTree​(
TextTree
text)
```

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

LiteralTree

object

- newParamTree

```java
ParamTree
newParamTree​(boolean isTypeParameter,

IdentifierTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ParamTree

object, to represent a

@param

tag.

**Parameters:** isTypeParameter

- true if this is a type parameter, and false otherwise
**Parameters:** name

- the parameter being described
**Parameters:** description

- the description of the parameter
**Returns:** a

ParamTree

object

- newProvidesTree

```java
ProvidesTree
newProvidesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ProvidesTree

object, to represent a

@provides

tag.

**Parameters:** name

- the name of the service type
**Parameters:** description

- a description of the service being provided
**Returns:** a

ProvidesTree

object

- newReferenceTree

```java
ReferenceTree
newReferenceTree​(
String
signature)
```

Create a new

ReferenceTree

object, to represent a reference to an API element.

**Parameters:** signature

- the doc comment signature of the reference
**Returns:** a

ReferenceTree

object

- newReturnTree

```java
ReturnTree
newReturnTree​(
List
<? extends
DocTree
> description)
```

Create a new

ReturnTree

object, to represent a

@return

tag.

**Parameters:** description

- the description of the return value of a method
**Returns:** a

ReturnTree

object

- newSeeTree

```java
SeeTree
newSeeTree​(
List
<? extends
DocTree
> reference)
```

Create a new

SeeTree

object, to represent a

@see

tag.

**Parameters:** reference

- the reference
**Returns:** a

SeeTree

object

- newSerialTree

```java
SerialTree
newSerialTree​(
List
<? extends
DocTree
> description)
```

Create a new

SerialTree

object, to represent a

@serial

tag.

**Parameters:** description

- the description for the tag
**Returns:** a

SerialTree

object

- newSerialDataTree

```java
SerialDataTree
newSerialDataTree​(
List
<? extends
DocTree
> description)
```

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

**Parameters:** description

- the description for the tag
**Returns:** a

SerialDataTree

object

- newSerialFieldTree

```java
SerialFieldTree
newSerialFieldTree​(
IdentifierTree
name,

ReferenceTree
type,

List
<? extends
DocTree
> description)
```

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Parameters:** description

- the description of the field
**Returns:** a

SerialFieldTree

object

- newSinceTree

```java
SinceTree
newSinceTree​(
List
<? extends
DocTree
> text)
```

Create a new

SinceTree

object, to represent a

@since

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

SinceTree

object

- newStartElementTree

```java
StartElementTree
newStartElementTree​(
Name
name,

List
<? extends
DocTree
> attrs,
boolean selfClosing)
```

Create a new

StartElementTree

object, to represent the start of an HTML element.

**Parameters:** name

- the name of the HTML element
**Parameters:** attrs

- the attributes
**Parameters:** selfClosing

- true if the start element is marked as self-closing; otherwise false
**Returns:** a

StartElementTree

object

- newSummaryTree

```java
default
SummaryTree
newSummaryTree​(
List
<? extends
DocTree
> summary)
```

Create a new

SummaryTree

object, to represent a

@summary

tag.

**Implementation Requirements:** This implementation throws

UnsupportedOperationException

.
**Parameters:** summary

- the content of the tag
**Returns:** a

SummaryTree

object
**Since:** 10

- newTextTree

```java
TextTree
newTextTree​(
String
text)
```

Create a new

TextTree

object, to represent some plain text.

**Parameters:** text

- the text
**Returns:** a

TextTree

object

- newThrowsTree

```java
ThrowsTree
newThrowsTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ThrowsTree

object, to represent a

@throws

tag.

**Parameters:** name

- the name of the exception
**Parameters:** description

- a description of why the exception might be thrown
**Returns:** a

ThrowsTree

object

- newUnknownBlockTagTree

```java
UnknownBlockTagTree
newUnknownBlockTagTree​(
Name
name,

List
<? extends
DocTree
> content)
```

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

**Parameters:** name

- the name of the block tag
**Parameters:** content

- the content
**Returns:** an

UnknownBlockTagTree

object

- newUnknownInlineTagTree

```java
UnknownInlineTagTree
newUnknownInlineTagTree​(
Name
name,

List
<? extends
DocTree
> content)
```

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

**Parameters:** name

- the name of the inline tag
**Parameters:** content

- the content
**Returns:** an

UnknownInlineTagTree

object

- newUsesTree

```java
UsesTree
newUsesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

UsesTree

object, to represent a

@uses

tag.

**Parameters:** name

- the name of the service type
**Parameters:** description

- a description of how the service will be used
**Returns:** a

UsesTree

object

- newValueTree

```java
ValueTree
newValueTree​(
ReferenceTree
ref)
```

Create a new

ValueTree

object, to represent a

{@value }

tag.

**Parameters:** ref

- a reference to the value
**Returns:** a

ValueTree

object

- newVersionTree

```java
VersionTree
newVersionTree​(
List
<? extends
DocTree
> text)
```

Create a new

VersionTree

object, to represent a

{@version }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

VersionTree

object

- at

```java
DocTreeFactory
at​(int pos)
```

Set the position to be recorded in subsequent tree nodes created by this factory.
The position should be a character offset relative to the beginning of the source file
or

NOPOS

.

**Parameters:** pos

- the position
**Returns:** this object, to facilitate method chaining

- getFirstSentence

```java
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)
```

Get the first sentence contained in a list of content.
The determination of the first sentence is implementation specific, and may
involve the use of a locale-specific

BreakIterator

and other heuristics.
The resulting list may share a common set of initial items with the input list.

**Parameters:** list

- the list
**Returns:** a list containing the first sentence of the list.

---

#### Method Detail

newAttributeTree

```java
AttributeTree
newAttributeTree​(
Name
name,

AttributeTree.ValueKind
vkind,

List
<? extends
DocTree
> value)
```

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

**Parameters:** name

- the name of the attribute
**Parameters:** vkind

- the kind of attribute value
**Parameters:** value

- the value, if any, of the attribute
**Returns:** an

AttributeTree

object

---

#### newAttributeTree

AttributeTree

newAttributeTree​(

Name

name,

AttributeTree.ValueKind

vkind,

List

<? extends

DocTree

> value)

Create a new

AttributeTree

object, to represent an HTML attribute in an HTML tag.

newAuthorTree

```java
AuthorTree
newAuthorTree​(
List
<? extends
DocTree
> name)
```

Create a new

AuthorTree

object, to represent an

{@author }

tag.

**Parameters:** name

- the name of the author
**Returns:** an

AuthorTree

object

---

#### newAuthorTree

AuthorTree

newAuthorTree​(

List

<? extends

DocTree

> name)

Create a new

AuthorTree

object, to represent an

{@author }

tag.

newCodeTree

```java
LiteralTree
newCodeTree​(
TextTree
text)
```

Create a new

CodeTree

object, to represent a

{@code }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

CodeTree

object

---

#### newCodeTree

LiteralTree

newCodeTree​(

TextTree

text)

Create a new

CodeTree

object, to represent a

{@code }

tag.

newCommentTree

```java
CommentTree
newCommentTree​(
String
text)
```

Create a new

CommentTree

, to represent an HTML comment.

**Parameters:** text

- the content of the comment
**Returns:** a

CommentTree

object

---

#### newCommentTree

CommentTree

newCommentTree​(

String

text)

Create a new

CommentTree

, to represent an HTML comment.

newDeprecatedTree

```java
DeprecatedTree
newDeprecatedTree​(
List
<? extends
DocTree
> text)
```

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

DeprecatedTree

object

---

#### newDeprecatedTree

DeprecatedTree

newDeprecatedTree​(

List

<? extends

DocTree

> text)

Create a new

DeprecatedTree

object, to represent an

{@deprecated }

tag.

newDocCommentTree

```java
DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags)
```

Create a new

DocCommentTree

object, to represent a complete doc comment.

**Parameters:** fullBody

- the entire body of the doc comment
**Parameters:** tags

- the block tags in the doc comment
**Returns:** a

DocCommentTree

object

---

#### newDocCommentTree

DocCommentTree

newDocCommentTree​(

List

<? extends

DocTree

> fullBody,

List

<? extends

DocTree

> tags)

Create a new

DocCommentTree

object, to represent a complete doc comment.

newDocCommentTree

```java
DocCommentTree
newDocCommentTree​(
List
<? extends
DocTree
> fullBody,

List
<? extends
DocTree
> tags,

List
<? extends
DocTree
> preamble,

List
<? extends
DocTree
> postamble)
```

Create a new

DocCommentTree

object, to represent the enitire doc comment.

**Parameters:** fullBody

- the entire body of the doc comment
**Parameters:** tags

- the block tags in the doc comment
**Parameters:** preamble

- the meta content of an html file including the body tag
**Parameters:** postamble

- the meta content of an html including the closing body tag
**Returns:** a

DocCommentTree

object
**Since:** 10

---

#### newDocCommentTree

DocCommentTree

newDocCommentTree​(

List

<? extends

DocTree

> fullBody,

List

<? extends

DocTree

> tags,

List

<? extends

DocTree

> preamble,

List

<? extends

DocTree

> postamble)

Create a new

DocCommentTree

object, to represent the enitire doc comment.

newDocRootTree

```java
DocRootTree
newDocRootTree()
```

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

**Returns:** a

DocRootTree

object

---

#### newDocRootTree

DocRootTree

newDocRootTree()

Create a new

DocRootTree

object, to represent an

{@docroot}

tag.

newDocTypeTree

```java
DocTypeTree
newDocTypeTree​(
String
text)
```

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

**Parameters:** text

- the content of the declaration
**Returns:** a

CommentTree

object
**Since:** 10

---

#### newDocTypeTree

DocTypeTree

newDocTypeTree​(

String

text)

Create a new

DocTypeTree

, to represent a

DOCTYPE

HTML declaration.

newEndElementTree

```java
EndElementTree
newEndElementTree​(
Name
name)
```

Create a new

EndElement

object, to represent the end of an HTML element.

**Parameters:** name

- the name of the HTML element
**Returns:** an

EndElementTree

object

---

#### newEndElementTree

EndElementTree

newEndElementTree​(

Name

name)

Create a new

EndElement

object, to represent the end of an HTML element.

newEntityTree

```java
EntityTree
newEntityTree​(
Name
name)
```

Create a new

EntityTree

object, to represent an HTML entity.

**Parameters:** name

- the name of the entity, representing the characters between '<' and ';'
in the representation of the entity in an HTML document
**Returns:** an

EntityTree

object

---

#### newEntityTree

EntityTree

newEntityTree​(

Name

name)

Create a new

EntityTree

object, to represent an HTML entity.

newErroneousTree

```java
ErroneousTree
newErroneousTree​(
String
text,

Diagnostic
<
JavaFileObject
> diag)
```

Create a new

ErroneousTree

object, to represent some unparseable input.

**Parameters:** text

- the unparseable text
**Parameters:** diag

- a diagnostic associated with the unparseable text, or null
**Returns:** an

ErroneousTree

object

---

#### newErroneousTree

ErroneousTree

newErroneousTree​(

String

text,

Diagnostic

<

JavaFileObject

> diag)

Create a new

ErroneousTree

object, to represent some unparseable input.

newExceptionTree

```java
ThrowsTree
newExceptionTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ExceptionTree

object, to represent an

@exception

tag.

**Parameters:** name

- the name of the exception
**Parameters:** description

- a description of why the exception might be thrown
**Returns:** an

ExceptionTree

object

---

#### newExceptionTree

ThrowsTree

newExceptionTree​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ExceptionTree

object, to represent an

@exception

tag.

newHiddenTree

```java
HiddenTree
newHiddenTree​(
List
<? extends
DocTree
> text)
```

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

HiddenTree

object

---

#### newHiddenTree

HiddenTree

newHiddenTree​(

List

<? extends

DocTree

> text)

Create a new

HiddenTree

object, to represent an

{@hidden }

tag.

newIdentifierTree

```java
IdentifierTree
newIdentifierTree​(
Name
name)
```

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

**Parameters:** name

- the name of the identifier
**Returns:** an

IdentifierTree

object

---

#### newIdentifierTree

IdentifierTree

newIdentifierTree​(

Name

name)

Create a new

IdentifierTree

object, to represent an identifier, such as in a

@param

tag.

newIndexTree

```java
IndexTree
newIndexTree​(
DocTree
term,

List
<? extends
DocTree
> description)
```

Create a new

IndexTree

object, to represent an

{@index }

tag.

**Parameters:** term

- the search term
**Parameters:** description

- an optional description of the search term
**Returns:** an

IndexTree

object

---

#### newIndexTree

IndexTree

newIndexTree​(

DocTree

term,

List

<? extends

DocTree

> description)

Create a new

IndexTree

object, to represent an

{@index }

tag.

newInheritDocTree

```java
InheritDocTree
newInheritDocTree()
```

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

**Returns:** an

InheritDocTree

object

---

#### newInheritDocTree

InheritDocTree

newInheritDocTree()

Create a new

InheritDocTree

object, to represent an

{@inheritDoc}

tag.

newLinkTree

```java
LinkTree
newLinkTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)
```

Create a new

LinkTree

object, to represent a

{@link }

tag.

**Parameters:** ref

- the API element being referenced
**Parameters:** label

- an optional label for the link
**Returns:** a

LinkTree

object

---

#### newLinkTree

LinkTree

newLinkTree​(

ReferenceTree

ref,

List

<? extends

DocTree

> label)

Create a new

LinkTree

object, to represent a

{@link }

tag.

newLinkPlainTree

```java
LinkTree
newLinkPlainTree​(
ReferenceTree
ref,

List
<? extends
DocTree
> label)
```

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

**Parameters:** ref

- the API element being referenced
**Parameters:** label

- an optional label for the link
**Returns:** a

LinkPlainTree

object

---

#### newLinkPlainTree

LinkTree

newLinkPlainTree​(

ReferenceTree

ref,

List

<? extends

DocTree

> label)

Create a new

LinkPlainTree

object, to represent a

{@linkplain }

tag.

newLiteralTree

```java
LiteralTree
newLiteralTree​(
TextTree
text)
```

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

LiteralTree

object

---

#### newLiteralTree

LiteralTree

newLiteralTree​(

TextTree

text)

Create a new

LiteralTree

object, to represent a

{@literal }

tag.

newParamTree

```java
ParamTree
newParamTree​(boolean isTypeParameter,

IdentifierTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ParamTree

object, to represent a

@param

tag.

**Parameters:** isTypeParameter

- true if this is a type parameter, and false otherwise
**Parameters:** name

- the parameter being described
**Parameters:** description

- the description of the parameter
**Returns:** a

ParamTree

object

---

#### newParamTree

ParamTree

newParamTree​(boolean isTypeParameter,

IdentifierTree

name,

List

<? extends

DocTree

> description)

Create a new

ParamTree

object, to represent a

@param

tag.

newProvidesTree

```java
ProvidesTree
newProvidesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ProvidesTree

object, to represent a

@provides

tag.

**Parameters:** name

- the name of the service type
**Parameters:** description

- a description of the service being provided
**Returns:** a

ProvidesTree

object

---

#### newProvidesTree

ProvidesTree

newProvidesTree​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ProvidesTree

object, to represent a

@provides

tag.

newReferenceTree

```java
ReferenceTree
newReferenceTree​(
String
signature)
```

Create a new

ReferenceTree

object, to represent a reference to an API element.

**Parameters:** signature

- the doc comment signature of the reference
**Returns:** a

ReferenceTree

object

---

#### newReferenceTree

ReferenceTree

newReferenceTree​(

String

signature)

Create a new

ReferenceTree

object, to represent a reference to an API element.

newReturnTree

```java
ReturnTree
newReturnTree​(
List
<? extends
DocTree
> description)
```

Create a new

ReturnTree

object, to represent a

@return

tag.

**Parameters:** description

- the description of the return value of a method
**Returns:** a

ReturnTree

object

---

#### newReturnTree

ReturnTree

newReturnTree​(

List

<? extends

DocTree

> description)

Create a new

ReturnTree

object, to represent a

@return

tag.

newSeeTree

```java
SeeTree
newSeeTree​(
List
<? extends
DocTree
> reference)
```

Create a new

SeeTree

object, to represent a

@see

tag.

**Parameters:** reference

- the reference
**Returns:** a

SeeTree

object

---

#### newSeeTree

SeeTree

newSeeTree​(

List

<? extends

DocTree

> reference)

Create a new

SeeTree

object, to represent a

@see

tag.

newSerialTree

```java
SerialTree
newSerialTree​(
List
<? extends
DocTree
> description)
```

Create a new

SerialTree

object, to represent a

@serial

tag.

**Parameters:** description

- the description for the tag
**Returns:** a

SerialTree

object

---

#### newSerialTree

SerialTree

newSerialTree​(

List

<? extends

DocTree

> description)

Create a new

SerialTree

object, to represent a

@serial

tag.

newSerialDataTree

```java
SerialDataTree
newSerialDataTree​(
List
<? extends
DocTree
> description)
```

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

**Parameters:** description

- the description for the tag
**Returns:** a

SerialDataTree

object

---

#### newSerialDataTree

SerialDataTree

newSerialDataTree​(

List

<? extends

DocTree

> description)

Create a new

SerialDataTree

object, to represent a

@serialData

tag.

newSerialFieldTree

```java
SerialFieldTree
newSerialFieldTree​(
IdentifierTree
name,

ReferenceTree
type,

List
<? extends
DocTree
> description)
```

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

**Parameters:** name

- the name of the field
**Parameters:** type

- the type of the field
**Parameters:** description

- the description of the field
**Returns:** a

SerialFieldTree

object

---

#### newSerialFieldTree

SerialFieldTree

newSerialFieldTree​(

IdentifierTree

name,

ReferenceTree

type,

List

<? extends

DocTree

> description)

Create a new

SerialFieldTree

object, to represent a

@serialField

tag.

newSinceTree

```java
SinceTree
newSinceTree​(
List
<? extends
DocTree
> text)
```

Create a new

SinceTree

object, to represent a

@since

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

SinceTree

object

---

#### newSinceTree

SinceTree

newSinceTree​(

List

<? extends

DocTree

> text)

Create a new

SinceTree

object, to represent a

@since

tag.

newStartElementTree

```java
StartElementTree
newStartElementTree​(
Name
name,

List
<? extends
DocTree
> attrs,
boolean selfClosing)
```

Create a new

StartElementTree

object, to represent the start of an HTML element.

**Parameters:** name

- the name of the HTML element
**Parameters:** attrs

- the attributes
**Parameters:** selfClosing

- true if the start element is marked as self-closing; otherwise false
**Returns:** a

StartElementTree

object

---

#### newStartElementTree

StartElementTree

newStartElementTree​(

Name

name,

List

<? extends

DocTree

> attrs,
boolean selfClosing)

Create a new

StartElementTree

object, to represent the start of an HTML element.

newSummaryTree

```java
default
SummaryTree
newSummaryTree​(
List
<? extends
DocTree
> summary)
```

Create a new

SummaryTree

object, to represent a

@summary

tag.

**Implementation Requirements:** This implementation throws

UnsupportedOperationException

.
**Parameters:** summary

- the content of the tag
**Returns:** a

SummaryTree

object
**Since:** 10

---

#### newSummaryTree

default

SummaryTree

newSummaryTree​(

List

<? extends

DocTree

> summary)

Create a new

SummaryTree

object, to represent a

@summary

tag.

newTextTree

```java
TextTree
newTextTree​(
String
text)
```

Create a new

TextTree

object, to represent some plain text.

**Parameters:** text

- the text
**Returns:** a

TextTree

object

---

#### newTextTree

TextTree

newTextTree​(

String

text)

Create a new

TextTree

object, to represent some plain text.

newThrowsTree

```java
ThrowsTree
newThrowsTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

ThrowsTree

object, to represent a

@throws

tag.

**Parameters:** name

- the name of the exception
**Parameters:** description

- a description of why the exception might be thrown
**Returns:** a

ThrowsTree

object

---

#### newThrowsTree

ThrowsTree

newThrowsTree​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

ThrowsTree

object, to represent a

@throws

tag.

newUnknownBlockTagTree

```java
UnknownBlockTagTree
newUnknownBlockTagTree​(
Name
name,

List
<? extends
DocTree
> content)
```

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

**Parameters:** name

- the name of the block tag
**Parameters:** content

- the content
**Returns:** an

UnknownBlockTagTree

object

---

#### newUnknownBlockTagTree

UnknownBlockTagTree

newUnknownBlockTagTree​(

Name

name,

List

<? extends

DocTree

> content)

Create a new

UnknownBlockTagTree

object, to represent an unrecognized block tag.

newUnknownInlineTagTree

```java
UnknownInlineTagTree
newUnknownInlineTagTree​(
Name
name,

List
<? extends
DocTree
> content)
```

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

**Parameters:** name

- the name of the inline tag
**Parameters:** content

- the content
**Returns:** an

UnknownInlineTagTree

object

---

#### newUnknownInlineTagTree

UnknownInlineTagTree

newUnknownInlineTagTree​(

Name

name,

List

<? extends

DocTree

> content)

Create a new

UnknownInlineTagTree

object, to represent an unrecognized inline tag.

newUsesTree

```java
UsesTree
newUsesTree​(
ReferenceTree
name,

List
<? extends
DocTree
> description)
```

Create a new

UsesTree

object, to represent a

@uses

tag.

**Parameters:** name

- the name of the service type
**Parameters:** description

- a description of how the service will be used
**Returns:** a

UsesTree

object

---

#### newUsesTree

UsesTree

newUsesTree​(

ReferenceTree

name,

List

<? extends

DocTree

> description)

Create a new

UsesTree

object, to represent a

@uses

tag.

newValueTree

```java
ValueTree
newValueTree​(
ReferenceTree
ref)
```

Create a new

ValueTree

object, to represent a

{@value }

tag.

**Parameters:** ref

- a reference to the value
**Returns:** a

ValueTree

object

---

#### newValueTree

ValueTree

newValueTree​(

ReferenceTree

ref)

Create a new

ValueTree

object, to represent a

{@value }

tag.

newVersionTree

```java
VersionTree
newVersionTree​(
List
<? extends
DocTree
> text)
```

Create a new

VersionTree

object, to represent a

{@version }

tag.

**Parameters:** text

- the content of the tag
**Returns:** a

VersionTree

object

---

#### newVersionTree

VersionTree

newVersionTree​(

List

<? extends

DocTree

> text)

Create a new

VersionTree

object, to represent a

{@version }

tag.

at

```java
DocTreeFactory
at​(int pos)
```

Set the position to be recorded in subsequent tree nodes created by this factory.
The position should be a character offset relative to the beginning of the source file
or

NOPOS

.

**Parameters:** pos

- the position
**Returns:** this object, to facilitate method chaining

---

#### at

DocTreeFactory

at​(int pos)

Set the position to be recorded in subsequent tree nodes created by this factory.
The position should be a character offset relative to the beginning of the source file
or

NOPOS

.

getFirstSentence

```java
List
<
DocTree
> getFirstSentence​(
List
<? extends
DocTree
> list)
```

Get the first sentence contained in a list of content.
The determination of the first sentence is implementation specific, and may
involve the use of a locale-specific

BreakIterator

and other heuristics.
The resulting list may share a common set of initial items with the input list.

**Parameters:** list

- the list
**Returns:** a list containing the first sentence of the list.

---

#### getFirstSentence

List

<

DocTree

> getFirstSentence​(

List

<? extends

DocTree

> list)

Get the first sentence contained in a list of content.
The determination of the first sentence is implementation specific, and may
involve the use of a locale-specific

BreakIterator

and other heuristics.
The resulting list may share a common set of initial items with the input list.

---

