# Interface Doc

**Source:** `jdk.javadoc\com\sun\javadoc\Doc.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Doc

extends
Comparable
<
Object
>
```

Represents Java language constructs (package, class, constructor,
method, field) which have comments and have been processed by this
run of javadoc. All Doc objects are unique, that is, they
are == comparable.

**All Superinterfaces:** Comparable

<

Object

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
commentText()

Return the text of the comment for this doc item.
Tags have been removed.

**Returns:**
- the text of the comment for this doc item.

---

#### Tag
[] tags()

Return all tags in this Doc item.

**Returns:**
- an array of

Tag

objects containing all tags on
this Doc item.

---

#### Tag
[] tags​(
String
tagname)

Return tags of the specified

kind

in
this Doc item.

For example, if 'tagname' has value "@serial", all tags in
this Doc item of kind "@serial" will be returned.

**Parameters:**
- tagname

- name of the tag kind to search for.

**Returns:**
- an array of Tag containing all tags whose 'kind()'
matches 'tagname'.

---

#### SeeTag
[] seeTags()

Return the see also tags in this Doc item.

**Returns:**
- an array of SeeTag containing all @see tags.

---

#### Tag
[] inlineTags()

Return comment as an array of tags. Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

**Returns:**
- an array of

Tag

s representing the comment

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

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by block
HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:**
- an array of

Tag

s representing the
first sentence of the comment

---

#### String
getRawCommentText()

Return the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Returns:**
- the full unprocessed text of the comment.

---

#### void setRawCommentText​(
String
rawDocumentation)

Set the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Parameters:**
- rawDocumentation

- A String containing the full unprocessed text of the comment.

---

#### String
name()

Returns the non-qualified name of this Doc item.

**Returns:**
- the name

---

#### int compareTo​(
Object
obj)

Compares this doc object with the specified object for order. Returns a
negative integer, zero, or a positive integer as this doc object is less
than, equal to, or greater than the given object.

This method satisfies the

Comparable

interface.

**Specified by:**
- compareTo

in interface

Comparable

<

Object

>

**Parameters:**
- obj

- the

Object

to be compared.

**Returns:**
- a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.

**Throws:**
- ClassCastException

- the specified Object's type prevents it
from being compared to this Object.

---

#### boolean isField()

Is this Doc item a field (but not an enum constant)?

**Returns:**
- true if it represents a field

---

#### boolean isEnumConstant()

Is this Doc item an enum constant?

**Returns:**
- true if it represents an enum constant

**Since:**
- 1.5

---

#### boolean isConstructor()

Is this Doc item a constructor?

**Returns:**
- true if it represents a constructor

---

#### boolean isMethod()

Is this Doc item a method (but not a constructor or annotation
type element)?

**Returns:**
- true if it represents a method

---

#### boolean isAnnotationTypeElement()

Is this Doc item an annotation type element?

**Returns:**
- true if it represents an annotation type element

**Since:**
- 1.5

---

#### boolean isInterface()

Is this Doc item an interface (but not an annotation type)?

**Returns:**
- true if it represents an interface

---

#### boolean isException()

Is this Doc item an exception class?

**Returns:**
- true if it represents an exception

---

#### boolean isError()

Is this Doc item an error class?

**Returns:**
- true if it represents a error

---

#### boolean isEnum()

Is this Doc item an enum type?

**Returns:**
- true if it represents an enum type

**Since:**
- 1.5

---

#### boolean isAnnotationType()

Is this Doc item an annotation type?

**Returns:**
- true if it represents an annotation type

**Since:**
- 1.5

---

#### boolean isOrdinaryClass()

Is this Doc item an

ordinary
class

?
(i.e. not an interface, annotation type, enum, exception, or error)?

**Returns:**
- true if it represents an ordinary class

---

#### boolean isClass()

Is this Doc item a

class

(and not an interface or annotation type)?
This includes ordinary classes, enums, errors and exceptions.

**Returns:**
- true if it represents a class

---

#### boolean isIncluded()

Return true if this Doc item is

included

in the result set.

**Returns:**
- true if this Doc item is

included

in the result set.

---

#### SourcePosition
position()

Return the source position of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.

**Returns:**
- the source positino of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.

**Since:**
- 1.4

---

### Additional Sections

#### Interface Doc

**All Superinterfaces:** Comparable

<

Object

>

**All Known Subinterfaces:** AnnotationTypeDoc

,

AnnotationTypeElementDoc

,

ClassDoc

,

ConstructorDoc

,

ExecutableMemberDoc

,

FieldDoc

,

MemberDoc

,

MethodDoc

,

PackageDoc

,

ProgramElementDoc

,

RootDoc

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Doc

extends
Comparable
<
Object
>
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents Java language constructs (package, class, constructor,
method, field) which have comments and have been processed by this
run of javadoc. All Doc objects are unique, that is, they
are == comparable.

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Doc

extends

Comparable

<

Object

>

Represents Java language constructs (package, class, constructor,
method, field) which have comments and have been processed by this
run of javadoc. All Doc objects are unique, that is, they
are == comparable.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

String

commentText

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of the comment for this doc item.

int

compareTo

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this doc object with the specified object for order.

Tag

[]

firstSentenceTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.

String

getRawCommentText

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the full unprocessed text of the comment.

Tag

[]

inlineTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return comment as an array of tags.

boolean

isAnnotationType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type?

boolean

isAnnotationTypeElement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type element?

boolean

isClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a

class

(and not an interface or annotation type)?

boolean

isConstructor

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a constructor?

boolean

isEnum

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum type?

boolean

isEnumConstant

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum constant?

boolean

isError

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an error class?

boolean

isException

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an exception class?

boolean

isField

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a field (but not an enum constant)?

boolean

isIncluded

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this Doc item is

included

in the result set.

boolean

isInterface

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an interface (but not an annotation type)?

boolean

isMethod

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a method (but not a constructor or annotation
type element)?

boolean

isOrdinaryClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an

ordinary
class

?

String

name

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the non-qualified name of this Doc item.

SourcePosition

position

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of the first line of the
corresponding declaration, or null if
no position is available.

SeeTag

[]

seeTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the see also tags in this Doc item.

void

setRawCommentText

​(

String

rawDocumentation)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the full unprocessed text of the comment.

Tag

[]

tags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return all tags in this Doc item.

Tag

[]

tags

​(

String

tagname)

Deprecated, for removal: This API element is subject to removal in a future version.

Return tags of the specified

kind

in
this Doc item.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

String

commentText

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of the comment for this doc item.

int

compareTo

​(

Object

obj)

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this doc object with the specified object for order.

Tag

[]

firstSentenceTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the first sentence of the comment as an array of tags.

String

getRawCommentText

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the full unprocessed text of the comment.

Tag

[]

inlineTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return comment as an array of tags.

boolean

isAnnotationType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type?

boolean

isAnnotationTypeElement

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type element?

boolean

isClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a

class

(and not an interface or annotation type)?

boolean

isConstructor

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a constructor?

boolean

isEnum

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum type?

boolean

isEnumConstant

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum constant?

boolean

isError

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an error class?

boolean

isException

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an exception class?

boolean

isField

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a field (but not an enum constant)?

boolean

isIncluded

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this Doc item is

included

in the result set.

boolean

isInterface

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an interface (but not an annotation type)?

boolean

isMethod

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a method (but not a constructor or annotation
type element)?

boolean

isOrdinaryClass

()

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an

ordinary
class

?

String

name

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the non-qualified name of this Doc item.

SourcePosition

position

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of the first line of the
corresponding declaration, or null if
no position is available.

SeeTag

[]

seeTags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the see also tags in this Doc item.

void

setRawCommentText

​(

String

rawDocumentation)

Deprecated, for removal: This API element is subject to removal in a future version.

Set the full unprocessed text of the comment.

Tag

[]

tags

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return all tags in this Doc item.

Tag

[]

tags

​(

String

tagname)

Deprecated, for removal: This API element is subject to removal in a future version.

Return tags of the specified

kind

in
this Doc item.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of the comment for this doc item.

Compares this doc object with the specified object for order.

Return the first sentence of the comment as an array of tags.

Return the full unprocessed text of the comment.

Return comment as an array of tags.

Is this Doc item an annotation type?

Is this Doc item an annotation type element?

Is this Doc item a

class

(and not an interface or annotation type)?

Is this Doc item a constructor?

Is this Doc item an enum type?

Is this Doc item an enum constant?

Is this Doc item an error class?

Is this Doc item an exception class?

Is this Doc item a field (but not an enum constant)?

Return true if this Doc item is

included

in the result set.

Is this Doc item an interface (but not an annotation type)?

Is this Doc item a method (but not a constructor or annotation
type element)?

Is this Doc item an

ordinary
class

?

Returns the non-qualified name of this Doc item.

Return the source position of the first line of the
corresponding declaration, or null if
no position is available.

Return the see also tags in this Doc item.

Set the full unprocessed text of the comment.

Return all tags in this Doc item.

Return tags of the specified

kind

in
this Doc item.

============ METHOD DETAIL ==========

- Method Detail

- commentText

```java
String
commentText()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of the comment for this doc item.
Tags have been removed.

**Returns:** the text of the comment for this doc item.

- tags

```java
Tag
[] tags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return all tags in this Doc item.

**Returns:** an array of

Tag

objects containing all tags on
this Doc item.

- tags

```java
Tag
[] tags​(
String
tagname)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return tags of the specified

kind

in
this Doc item.

For example, if 'tagname' has value "@serial", all tags in
this Doc item of kind "@serial" will be returned.

**Parameters:** tagname

- name of the tag kind to search for.
**Returns:** an array of Tag containing all tags whose 'kind()'
matches 'tagname'.

- seeTags

```java
SeeTag
[] seeTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the see also tags in this Doc item.

**Returns:** an array of SeeTag containing all @see tags.

- inlineTags

```java
Tag
[] inlineTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return comment as an array of tags. Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

**Returns:** an array of

Tag

s representing the comment

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

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by block
HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:** an array of

Tag

s representing the
first sentence of the comment

- getRawCommentText

```java
String
getRawCommentText()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Returns:** the full unprocessed text of the comment.

- setRawCommentText

```java
void setRawCommentText​(
String
rawDocumentation)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Parameters:** rawDocumentation

- A String containing the full unprocessed text of the comment.

- name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the non-qualified name of this Doc item.

**Returns:** the name

- compareTo

```java
int compareTo​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this doc object with the specified object for order. Returns a
negative integer, zero, or a positive integer as this doc object is less
than, equal to, or greater than the given object.

This method satisfies the

Comparable

interface.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the

Object

to be compared.
**Returns:** a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- the specified Object's type prevents it
from being compared to this Object.

- isField

```java
boolean isField()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a field (but not an enum constant)?

**Returns:** true if it represents a field

- isEnumConstant

```java
boolean isEnumConstant()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum constant?

**Returns:** true if it represents an enum constant
**Since:** 1.5

- isConstructor

```java
boolean isConstructor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a constructor?

**Returns:** true if it represents a constructor

- isMethod

```java
boolean isMethod()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a method (but not a constructor or annotation
type element)?

**Returns:** true if it represents a method

- isAnnotationTypeElement

```java
boolean isAnnotationTypeElement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type element?

**Returns:** true if it represents an annotation type element
**Since:** 1.5

- isInterface

```java
boolean isInterface()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an interface (but not an annotation type)?

**Returns:** true if it represents an interface

- isException

```java
boolean isException()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an exception class?

**Returns:** true if it represents an exception

- isError

```java
boolean isError()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an error class?

**Returns:** true if it represents a error

- isEnum

```java
boolean isEnum()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum type?

**Returns:** true if it represents an enum type
**Since:** 1.5

- isAnnotationType

```java
boolean isAnnotationType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type?

**Returns:** true if it represents an annotation type
**Since:** 1.5

- isOrdinaryClass

```java
boolean isOrdinaryClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an

ordinary
class

?
(i.e. not an interface, annotation type, enum, exception, or error)?

**Returns:** true if it represents an ordinary class

- isClass

```java
boolean isClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a

class

(and not an interface or annotation type)?
This includes ordinary classes, enums, errors and exceptions.

**Returns:** true if it represents a class

- isIncluded

```java
boolean isIncluded()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this Doc item is

included

in the result set.

**Returns:** true if this Doc item is

included

in the result set.

- position

```java
SourcePosition
position()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.

**Returns:** the source positino of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.
**Since:** 1.4

Method Detail

- commentText

```java
String
commentText()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of the comment for this doc item.
Tags have been removed.

**Returns:** the text of the comment for this doc item.

- tags

```java
Tag
[] tags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return all tags in this Doc item.

**Returns:** an array of

Tag

objects containing all tags on
this Doc item.

- tags

```java
Tag
[] tags​(
String
tagname)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return tags of the specified

kind

in
this Doc item.

For example, if 'tagname' has value "@serial", all tags in
this Doc item of kind "@serial" will be returned.

**Parameters:** tagname

- name of the tag kind to search for.
**Returns:** an array of Tag containing all tags whose 'kind()'
matches 'tagname'.

- seeTags

```java
SeeTag
[] seeTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the see also tags in this Doc item.

**Returns:** an array of SeeTag containing all @see tags.

- inlineTags

```java
Tag
[] inlineTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return comment as an array of tags. Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

**Returns:** an array of

Tag

s representing the comment

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

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by block
HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:** an array of

Tag

s representing the
first sentence of the comment

- getRawCommentText

```java
String
getRawCommentText()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Returns:** the full unprocessed text of the comment.

- setRawCommentText

```java
void setRawCommentText​(
String
rawDocumentation)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Parameters:** rawDocumentation

- A String containing the full unprocessed text of the comment.

- name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the non-qualified name of this Doc item.

**Returns:** the name

- compareTo

```java
int compareTo​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this doc object with the specified object for order. Returns a
negative integer, zero, or a positive integer as this doc object is less
than, equal to, or greater than the given object.

This method satisfies the

Comparable

interface.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the

Object

to be compared.
**Returns:** a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- the specified Object's type prevents it
from being compared to this Object.

- isField

```java
boolean isField()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a field (but not an enum constant)?

**Returns:** true if it represents a field

- isEnumConstant

```java
boolean isEnumConstant()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum constant?

**Returns:** true if it represents an enum constant
**Since:** 1.5

- isConstructor

```java
boolean isConstructor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a constructor?

**Returns:** true if it represents a constructor

- isMethod

```java
boolean isMethod()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a method (but not a constructor or annotation
type element)?

**Returns:** true if it represents a method

- isAnnotationTypeElement

```java
boolean isAnnotationTypeElement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type element?

**Returns:** true if it represents an annotation type element
**Since:** 1.5

- isInterface

```java
boolean isInterface()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an interface (but not an annotation type)?

**Returns:** true if it represents an interface

- isException

```java
boolean isException()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an exception class?

**Returns:** true if it represents an exception

- isError

```java
boolean isError()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an error class?

**Returns:** true if it represents a error

- isEnum

```java
boolean isEnum()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum type?

**Returns:** true if it represents an enum type
**Since:** 1.5

- isAnnotationType

```java
boolean isAnnotationType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type?

**Returns:** true if it represents an annotation type
**Since:** 1.5

- isOrdinaryClass

```java
boolean isOrdinaryClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an

ordinary
class

?
(i.e. not an interface, annotation type, enum, exception, or error)?

**Returns:** true if it represents an ordinary class

- isClass

```java
boolean isClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a

class

(and not an interface or annotation type)?
This includes ordinary classes, enums, errors and exceptions.

**Returns:** true if it represents a class

- isIncluded

```java
boolean isIncluded()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this Doc item is

included

in the result set.

**Returns:** true if this Doc item is

included

in the result set.

- position

```java
SourcePosition
position()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.

**Returns:** the source positino of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.
**Since:** 1.4

---

#### Method Detail

commentText

```java
String
commentText()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the text of the comment for this doc item.
Tags have been removed.

**Returns:** the text of the comment for this doc item.

---

#### commentText

String

commentText()

Return the text of the comment for this doc item.
Tags have been removed.

tags

```java
Tag
[] tags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return all tags in this Doc item.

**Returns:** an array of

Tag

objects containing all tags on
this Doc item.

---

#### tags

Tag

[] tags()

Return all tags in this Doc item.

tags

```java
Tag
[] tags​(
String
tagname)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return tags of the specified

kind

in
this Doc item.

For example, if 'tagname' has value "@serial", all tags in
this Doc item of kind "@serial" will be returned.

**Parameters:** tagname

- name of the tag kind to search for.
**Returns:** an array of Tag containing all tags whose 'kind()'
matches 'tagname'.

---

#### tags

Tag

[] tags​(

String

tagname)

Return tags of the specified

kind

in
this Doc item.

For example, if 'tagname' has value "@serial", all tags in
this Doc item of kind "@serial" will be returned.

seeTags

```java
SeeTag
[] seeTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the see also tags in this Doc item.

**Returns:** an array of SeeTag containing all @see tags.

---

#### seeTags

SeeTag

[] seeTags()

Return the see also tags in this Doc item.

inlineTags

```java
Tag
[] inlineTags()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return comment as an array of tags. Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

**Returns:** an array of

Tag

s representing the comment

---

#### inlineTags

Tag

[] inlineTags()

Return comment as an array of tags. Includes inline tags
(i.e. {@link

reference

} tags) but not
block tags.
Each section of plain text is represented as a

Tag

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

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

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by block
HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

**Returns:** an array of

Tag

s representing the
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

of

kind

"Text".
Inline tags are represented as a

SeeTag

of kind "@see"
and name "@link".

If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by block
HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

If the locale is English language, the first sentence is
determined by the rules described in the Java Language
Specification (first version): "This sentence ends
at the first period that is followed by a blank, tab, or
line terminator or at the first tagline.", in
addition a line will be terminated by block
HTML tags: <p> </p> <h1>
<h2> <h3> <h4> <h5> <h6>
<hr> <pre> or </pre>.
If the locale is not English, the sentence end will be
determined by

BreakIterator.getSentenceInstance(Locale)

.

getRawCommentText

```java
String
getRawCommentText()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Returns:** the full unprocessed text of the comment.

---

#### getRawCommentText

String

getRawCommentText()

Return the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

setRawCommentText

```java
void setRawCommentText​(
String
rawDocumentation)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Set the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

**Parameters:** rawDocumentation

- A String containing the full unprocessed text of the comment.

---

#### setRawCommentText

void setRawCommentText​(

String

rawDocumentation)

Set the full unprocessed text of the comment. Tags
are included as text. Used mainly for store and retrieve
operations like internalization.

name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the non-qualified name of this Doc item.

**Returns:** the name

---

#### name

String

name()

Returns the non-qualified name of this Doc item.

compareTo

```java
int compareTo​(
Object
obj)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compares this doc object with the specified object for order. Returns a
negative integer, zero, or a positive integer as this doc object is less
than, equal to, or greater than the given object.

This method satisfies the

Comparable

interface.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the

Object

to be compared.
**Returns:** a negative integer, zero, or a positive integer as this Object
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- the specified Object's type prevents it
from being compared to this Object.

---

#### compareTo

int compareTo​(

Object

obj)

Compares this doc object with the specified object for order. Returns a
negative integer, zero, or a positive integer as this doc object is less
than, equal to, or greater than the given object.

This method satisfies the

Comparable

interface.

This method satisfies the

Comparable

interface.

isField

```java
boolean isField()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a field (but not an enum constant)?

**Returns:** true if it represents a field

---

#### isField

boolean isField()

Is this Doc item a field (but not an enum constant)?

isEnumConstant

```java
boolean isEnumConstant()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum constant?

**Returns:** true if it represents an enum constant
**Since:** 1.5

---

#### isEnumConstant

boolean isEnumConstant()

Is this Doc item an enum constant?

isConstructor

```java
boolean isConstructor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a constructor?

**Returns:** true if it represents a constructor

---

#### isConstructor

boolean isConstructor()

Is this Doc item a constructor?

isMethod

```java
boolean isMethod()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a method (but not a constructor or annotation
type element)?

**Returns:** true if it represents a method

---

#### isMethod

boolean isMethod()

Is this Doc item a method (but not a constructor or annotation
type element)?

isAnnotationTypeElement

```java
boolean isAnnotationTypeElement()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type element?

**Returns:** true if it represents an annotation type element
**Since:** 1.5

---

#### isAnnotationTypeElement

boolean isAnnotationTypeElement()

Is this Doc item an annotation type element?

isInterface

```java
boolean isInterface()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an interface (but not an annotation type)?

**Returns:** true if it represents an interface

---

#### isInterface

boolean isInterface()

Is this Doc item an interface (but not an annotation type)?

isException

```java
boolean isException()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an exception class?

**Returns:** true if it represents an exception

---

#### isException

boolean isException()

Is this Doc item an exception class?

isError

```java
boolean isError()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an error class?

**Returns:** true if it represents a error

---

#### isError

boolean isError()

Is this Doc item an error class?

isEnum

```java
boolean isEnum()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an enum type?

**Returns:** true if it represents an enum type
**Since:** 1.5

---

#### isEnum

boolean isEnum()

Is this Doc item an enum type?

isAnnotationType

```java
boolean isAnnotationType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an annotation type?

**Returns:** true if it represents an annotation type
**Since:** 1.5

---

#### isAnnotationType

boolean isAnnotationType()

Is this Doc item an annotation type?

isOrdinaryClass

```java
boolean isOrdinaryClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item an

ordinary
class

?
(i.e. not an interface, annotation type, enum, exception, or error)?

**Returns:** true if it represents an ordinary class

---

#### isOrdinaryClass

boolean isOrdinaryClass()

Is this Doc item an

ordinary
class

?
(i.e. not an interface, annotation type, enum, exception, or error)?

isClass

```java
boolean isClass()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Is this Doc item a

class

(and not an interface or annotation type)?
This includes ordinary classes, enums, errors and exceptions.

**Returns:** true if it represents a class

---

#### isClass

boolean isClass()

Is this Doc item a

class

(and not an interface or annotation type)?
This includes ordinary classes, enums, errors and exceptions.

isIncluded

```java
boolean isIncluded()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this Doc item is

included

in the result set.

**Returns:** true if this Doc item is

included

in the result set.

---

#### isIncluded

boolean isIncluded()

Return true if this Doc item is

included

in the result set.

position

```java
SourcePosition
position()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the source position of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.

**Returns:** the source positino of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.
**Since:** 1.4

---

#### position

SourcePosition

position()

Return the source position of the first line of the
corresponding declaration, or null if
no position is available. A default constructor returns
null because it has no location in the source file.

---

