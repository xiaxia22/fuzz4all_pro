# Interface Taglet

**Source:** `jdk.javadoc\jdk\javadoc\doclet\Taglet.html`

### Class Description

```java
public interface
Taglet
```

The interface for a custom taglet supported by doclets such as
the

standard doclet

.
Custom taglets are used to handle custom tags in documentation
comments.

A custom taglet must implement this interface, and must have
a public default constructor (i.e. a public constructor with no
parameters), by which, the doclet will instantiate and
register the custom taglet.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Set
<
Taglet.Location
> getAllowedLocations()

Returns the set of locations in which a tag may be used.

**Returns:**
- the set of locations in which a tag may be used

---

#### boolean isInlineTag()

Indicates whether this taglet is for inline tags or not.

**Returns:**
- true if this taglet is for an inline tag, and false otherwise

---

#### String
getName()

Returns the name of the tag.

**Returns:**
- the name of this custom tag.

---

#### default void init​(
DocletEnvironment
env,

Doclet
doclet)

Initializes this taglet with the given doclet environment and doclet.

**Parameters:**
- env

- the environment in which the doclet and taglet are running
- doclet

- the doclet that instantiated this taglet

**API Note:**
- The environment may be used to access utility classes for

elements

and

types

if needed.

**Implementation Requirements:**
- This implementation does nothing.

---

#### String
toString​(
List
<? extends
DocTree
> tags,

Element
element)

Returns the string representation of a series of instances of
this tag to be included in the generated output.
If this taglet is for an

inline

tag it will
be called once per instance of the tag, each time with a singleton list.
Otherwise, if this tag is a block tag, it will be called once per
comment, with a list of all the instances of the tag in a comment.

**Parameters:**
- tags

- the list of instances of this tag
- element

- the element to which the enclosing comment belongs

**Returns:**
- the string representation of the tags to be included in
the generated output

---

### Additional Sections

#### Interface Taglet

```java
public interface
Taglet
```

The interface for a custom taglet supported by doclets such as
the

standard doclet

.
Custom taglets are used to handle custom tags in documentation
comments.

A custom taglet must implement this interface, and must have
a public default constructor (i.e. a public constructor with no
parameters), by which, the doclet will instantiate and
register the custom taglet.

**Since:** 9

public interface

Taglet

The interface for a custom taglet supported by doclets such as
the

standard doclet

.
Custom taglets are used to handle custom tags in documentation
comments.

A custom taglet must implement this interface, and must have
a public default constructor (i.e. a public constructor with no
parameters), by which, the doclet will instantiate and
register the custom taglet.

A custom taglet must implement this interface, and must have
a public default constructor (i.e. a public constructor with no
parameters), by which, the doclet will instantiate and
register the custom taglet.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Taglet.Location

The kind of location in which a tag may be used.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

Set

<

Taglet.Location

>

getAllowedLocations

()

Returns the set of locations in which a tag may be used.

String

getName

()

Returns the name of the tag.

default void

init

​(

DocletEnvironment

env,

Doclet

doclet)

Initializes this taglet with the given doclet environment and doclet.

boolean

isInlineTag

()

Indicates whether this taglet is for inline tags or not.

String

toString

​(

List

<? extends

DocTree

> tags,

Element

element)

Returns the string representation of a series of instances of
this tag to be included in the generated output.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Taglet.Location

The kind of location in which a tag may be used.

---

#### Nested Class Summary

The kind of location in which a tag may be used.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

Set

<

Taglet.Location

>

getAllowedLocations

()

Returns the set of locations in which a tag may be used.

String

getName

()

Returns the name of the tag.

default void

init

​(

DocletEnvironment

env,

Doclet

doclet)

Initializes this taglet with the given doclet environment and doclet.

boolean

isInlineTag

()

Indicates whether this taglet is for inline tags or not.

String

toString

​(

List

<? extends

DocTree

> tags,

Element

element)

Returns the string representation of a series of instances of
this tag to be included in the generated output.

---

#### Method Summary

Returns the set of locations in which a tag may be used.

Returns the name of the tag.

Initializes this taglet with the given doclet environment and doclet.

Indicates whether this taglet is for inline tags or not.

Returns the string representation of a series of instances of
this tag to be included in the generated output.

============ METHOD DETAIL ==========

- Method Detail

- getAllowedLocations

```java
Set
<
Taglet.Location
> getAllowedLocations()
```

Returns the set of locations in which a tag may be used.

**Returns:** the set of locations in which a tag may be used

- isInlineTag

```java
boolean isInlineTag()
```

Indicates whether this taglet is for inline tags or not.

**Returns:** true if this taglet is for an inline tag, and false otherwise

- getName

```java
String
getName()
```

Returns the name of the tag.

**Returns:** the name of this custom tag.

- init

```java
default void init​(
DocletEnvironment
env,

Doclet
doclet)
```

Initializes this taglet with the given doclet environment and doclet.

**API Note:** The environment may be used to access utility classes for

elements

and

types

if needed.
**Implementation Requirements:** This implementation does nothing.
**Parameters:** env

- the environment in which the doclet and taglet are running
**Parameters:** doclet

- the doclet that instantiated this taglet

- toString

```java
String
toString​(
List
<? extends
DocTree
> tags,

Element
element)
```

Returns the string representation of a series of instances of
this tag to be included in the generated output.
If this taglet is for an

inline

tag it will
be called once per instance of the tag, each time with a singleton list.
Otherwise, if this tag is a block tag, it will be called once per
comment, with a list of all the instances of the tag in a comment.

**Parameters:** tags

- the list of instances of this tag
**Parameters:** element

- the element to which the enclosing comment belongs
**Returns:** the string representation of the tags to be included in
the generated output

Method Detail

- getAllowedLocations

```java
Set
<
Taglet.Location
> getAllowedLocations()
```

Returns the set of locations in which a tag may be used.

**Returns:** the set of locations in which a tag may be used

- isInlineTag

```java
boolean isInlineTag()
```

Indicates whether this taglet is for inline tags or not.

**Returns:** true if this taglet is for an inline tag, and false otherwise

- getName

```java
String
getName()
```

Returns the name of the tag.

**Returns:** the name of this custom tag.

- init

```java
default void init​(
DocletEnvironment
env,

Doclet
doclet)
```

Initializes this taglet with the given doclet environment and doclet.

**API Note:** The environment may be used to access utility classes for

elements

and

types

if needed.
**Implementation Requirements:** This implementation does nothing.
**Parameters:** env

- the environment in which the doclet and taglet are running
**Parameters:** doclet

- the doclet that instantiated this taglet

- toString

```java
String
toString​(
List
<? extends
DocTree
> tags,

Element
element)
```

Returns the string representation of a series of instances of
this tag to be included in the generated output.
If this taglet is for an

inline

tag it will
be called once per instance of the tag, each time with a singleton list.
Otherwise, if this tag is a block tag, it will be called once per
comment, with a list of all the instances of the tag in a comment.

**Parameters:** tags

- the list of instances of this tag
**Parameters:** element

- the element to which the enclosing comment belongs
**Returns:** the string representation of the tags to be included in
the generated output

---

#### Method Detail

getAllowedLocations

```java
Set
<
Taglet.Location
> getAllowedLocations()
```

Returns the set of locations in which a tag may be used.

**Returns:** the set of locations in which a tag may be used

---

#### getAllowedLocations

Set

<

Taglet.Location

> getAllowedLocations()

Returns the set of locations in which a tag may be used.

isInlineTag

```java
boolean isInlineTag()
```

Indicates whether this taglet is for inline tags or not.

**Returns:** true if this taglet is for an inline tag, and false otherwise

---

#### isInlineTag

boolean isInlineTag()

Indicates whether this taglet is for inline tags or not.

getName

```java
String
getName()
```

Returns the name of the tag.

**Returns:** the name of this custom tag.

---

#### getName

String

getName()

Returns the name of the tag.

init

```java
default void init​(
DocletEnvironment
env,

Doclet
doclet)
```

Initializes this taglet with the given doclet environment and doclet.

**API Note:** The environment may be used to access utility classes for

elements

and

types

if needed.
**Implementation Requirements:** This implementation does nothing.
**Parameters:** env

- the environment in which the doclet and taglet are running
**Parameters:** doclet

- the doclet that instantiated this taglet

---

#### init

default void init​(

DocletEnvironment

env,

Doclet

doclet)

Initializes this taglet with the given doclet environment and doclet.

toString

```java
String
toString​(
List
<? extends
DocTree
> tags,

Element
element)
```

Returns the string representation of a series of instances of
this tag to be included in the generated output.
If this taglet is for an

inline

tag it will
be called once per instance of the tag, each time with a singleton list.
Otherwise, if this tag is a block tag, it will be called once per
comment, with a list of all the instances of the tag in a comment.

**Parameters:** tags

- the list of instances of this tag
**Parameters:** element

- the element to which the enclosing comment belongs
**Returns:** the string representation of the tags to be included in
the generated output

---

#### toString

String

toString​(

List

<? extends

DocTree

> tags,

Element

element)

Returns the string representation of a series of instances of
this tag to be included in the generated output.
If this taglet is for an

inline

tag it will
be called once per instance of the tag, each time with a singleton list.
Otherwise, if this tag is a block tag, it will be called once per
comment, with a list of all the instances of the tag in a comment.

---

