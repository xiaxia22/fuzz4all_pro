# Interface AttributedCharacterIterator

**Source:** `java.base\java\text\AttributedCharacterIterator.html`

### Class Description

```java
public interface
AttributedCharacterIterator

extends
CharacterIterator
```

An

AttributedCharacterIterator

allows iteration through both text and
related attribute information.

An attribute is a key/value pair, identified by the key. No two
attributes on a given character can have the same key.

The values for an attribute are immutable, or must not be mutated
by clients or storage. They are always passed by reference, and not
cloned.

A

run with respect to an attribute

is a maximum text range for
which:

- the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

**All Superinterfaces:** CharacterIterator

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getRunStart()

Returns the index of the first character of the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:**
- the index of the first character of the run

---

#### int getRunStart​(
AttributedCharacterIterator.Attribute
attribute)

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

**Parameters:**
- attribute

- the desired attribute.

**Returns:**
- the index of the first character of the run

---

#### int getRunStart​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

**Parameters:**
- attributes

- a set of the desired attributes.

**Returns:**
- the index of the first character of the run

---

#### int getRunLimit()

Returns the index of the first character following the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:**
- the index of the first character following the run

---

#### int getRunLimit​(
AttributedCharacterIterator.Attribute
attribute)

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

**Parameters:**
- attribute

- the desired attribute

**Returns:**
- the index of the first character following the run

---

#### int getRunLimit​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

**Parameters:**
- attributes

- a set of the desired attributes

**Returns:**
- the index of the first character following the run

---

#### Map
<
AttributedCharacterIterator.Attribute
,​
Object
> getAttributes()

Returns a map with the attributes defined on the current
character.

**Returns:**
- a map with the attributes defined on the current character

---

#### Object
getAttribute​(
AttributedCharacterIterator.Attribute
attribute)

Returns the value of the named

attribute

for the current character.
Returns

null

if the

attribute

is not defined.

**Parameters:**
- attribute

- the desired attribute

**Returns:**
- the value of the named

attribute

or

null

---

#### Set
<
AttributedCharacterIterator.Attribute
> getAllAttributeKeys()

Returns the keys of all attributes defined on the
iterator's text range. The set is empty if no
attributes are defined.

**Returns:**
- the keys of all attributes

---

### Additional Sections

#### Interface AttributedCharacterIterator

**All Superinterfaces:** CharacterIterator

,

Cloneable

```java
public interface
AttributedCharacterIterator

extends
CharacterIterator
```

An

AttributedCharacterIterator

allows iteration through both text and
related attribute information.

An attribute is a key/value pair, identified by the key. No two
attributes on a given character can have the same key.

The values for an attribute are immutable, or must not be mutated
by clients or storage. They are always passed by reference, and not
cloned.

A

run with respect to an attribute

is a maximum text range for
which:

- the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

**Since:** 1.2
**See Also:** AttributedCharacterIterator.Attribute

,

TextAttribute

,

AttributedString

,

Annotation

public interface

AttributedCharacterIterator

extends

CharacterIterator

An

AttributedCharacterIterator

allows iteration through both text and
related attribute information.

An attribute is a key/value pair, identified by the key. No two
attributes on a given character can have the same key.

The values for an attribute are immutable, or must not be mutated
by clients or storage. They are always passed by reference, and not
cloned.

A

run with respect to an attribute

is a maximum text range for
which:

- the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

An attribute is a key/value pair, identified by the key. No two
attributes on a given character can have the same key.

The values for an attribute are immutable, or must not be mutated
by clients or storage. They are always passed by reference, and not
cloned.

A

run with respect to an attribute

is a maximum text range for
which:

- the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

The values for an attribute are immutable, or must not be mutated
by clients or storage. They are always passed by reference, and not
cloned.

A

run with respect to an attribute

is a maximum text range for
which:

- the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

A

run with respect to an attribute

is a maximum text range for
which:

- the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

the attribute is undefined or

null

for the entire range, or

the attribute value is defined and has the same non-

null

value for the
entire range.

A

run with respect to a set of attributes

is a maximum text range for
which this condition is met for each member attribute.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

When getting a run with no explicit attributes specified (i.e.,
calling

getRunStart()

and

getRunLimit()

), any
contiguous text segments having the same attributes (the same set
of attribute/value pairs) are treated as separate runs if the
attributes have been given to those text segments separately.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

The returned indexes are limited to the range of the iterator.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

The returned attribute information is limited to runs that contain
the current character.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

Attribute keys are instances of

AttributedCharacterIterator.Attribute

and its
subclasses, such as

TextAttribute

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

AttributedCharacterIterator.Attribute

Defines attribute keys that are used to identify text attributes.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.text.

CharacterIterator

DONE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Set

<

AttributedCharacterIterator.Attribute

>

getAllAttributeKeys

()

Returns the keys of all attributes defined on the
iterator's text range.

Object

getAttribute

​(

AttributedCharacterIterator.Attribute

attribute)

Returns the value of the named

attribute

for the current character.

Map

<

AttributedCharacterIterator.Attribute

,​

Object

>

getAttributes

()

Returns a map with the attributes defined on the current
character.

int

getRunLimit

()

Returns the index of the first character following the run
with respect to all attributes containing the current character.

int

getRunLimit

​(

AttributedCharacterIterator.Attribute

attribute)

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

int

getRunLimit

​(

Set

<? extends

AttributedCharacterIterator.Attribute

> attributes)

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

int

getRunStart

()

Returns the index of the first character of the run
with respect to all attributes containing the current character.

int

getRunStart

​(

AttributedCharacterIterator.Attribute

attribute)

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

int

getRunStart

​(

Set

<? extends

AttributedCharacterIterator.Attribute

> attributes)

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

- Methods declared in interface java.text.

CharacterIterator

clone

,

current

,

first

,

getBeginIndex

,

getEndIndex

,

getIndex

,

last

,

next

,

previous

,

setIndex

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

AttributedCharacterIterator.Attribute

Defines attribute keys that are used to identify text attributes.

---

#### Nested Class Summary

Defines attribute keys that are used to identify text attributes.

Field Summary

- Fields declared in interface java.text.

CharacterIterator

DONE

---

#### Field Summary

Fields declared in interface java.text.

CharacterIterator

DONE

---

#### Fields declared in interface java.text. CharacterIterator

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Set

<

AttributedCharacterIterator.Attribute

>

getAllAttributeKeys

()

Returns the keys of all attributes defined on the
iterator's text range.

Object

getAttribute

​(

AttributedCharacterIterator.Attribute

attribute)

Returns the value of the named

attribute

for the current character.

Map

<

AttributedCharacterIterator.Attribute

,​

Object

>

getAttributes

()

Returns a map with the attributes defined on the current
character.

int

getRunLimit

()

Returns the index of the first character following the run
with respect to all attributes containing the current character.

int

getRunLimit

​(

AttributedCharacterIterator.Attribute

attribute)

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

int

getRunLimit

​(

Set

<? extends

AttributedCharacterIterator.Attribute

> attributes)

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

int

getRunStart

()

Returns the index of the first character of the run
with respect to all attributes containing the current character.

int

getRunStart

​(

AttributedCharacterIterator.Attribute

attribute)

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

int

getRunStart

​(

Set

<? extends

AttributedCharacterIterator.Attribute

> attributes)

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

- Methods declared in interface java.text.

CharacterIterator

clone

,

current

,

first

,

getBeginIndex

,

getEndIndex

,

getIndex

,

last

,

next

,

previous

,

setIndex

---

#### Method Summary

Returns the keys of all attributes defined on the
iterator's text range.

Returns the value of the named

attribute

for the current character.

Returns a map with the attributes defined on the current
character.

Returns the index of the first character following the run
with respect to all attributes containing the current character.

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

Returns the index of the first character of the run
with respect to all attributes containing the current character.

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

Methods declared in interface java.text.

CharacterIterator

clone

,

current

,

first

,

getBeginIndex

,

getEndIndex

,

getIndex

,

last

,

next

,

previous

,

setIndex

---

#### Methods declared in interface java.text. CharacterIterator

============ METHOD DETAIL ==========

- Method Detail

- getRunStart

```java
int getRunStart()
```

Returns the index of the first character of the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:** the index of the first character of the run

- getRunStart

```java
int getRunStart​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

**Parameters:** attribute

- the desired attribute.
**Returns:** the index of the first character of the run

- getRunStart

```java
int getRunStart​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)
```

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

**Parameters:** attributes

- a set of the desired attributes.
**Returns:** the index of the first character of the run

- getRunLimit

```java
int getRunLimit()
```

Returns the index of the first character following the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:** the index of the first character following the run

- getRunLimit

```java
int getRunLimit​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

**Parameters:** attribute

- the desired attribute
**Returns:** the index of the first character following the run

- getRunLimit

```java
int getRunLimit​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)
```

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

**Parameters:** attributes

- a set of the desired attributes
**Returns:** the index of the first character following the run

- getAttributes

```java
Map
<
AttributedCharacterIterator.Attribute
,​
Object
> getAttributes()
```

Returns a map with the attributes defined on the current
character.

**Returns:** a map with the attributes defined on the current character

- getAttribute

```java
Object
getAttribute​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the value of the named

attribute

for the current character.
Returns

null

if the

attribute

is not defined.

**Parameters:** attribute

- the desired attribute
**Returns:** the value of the named

attribute

or

null

- getAllAttributeKeys

```java
Set
<
AttributedCharacterIterator.Attribute
> getAllAttributeKeys()
```

Returns the keys of all attributes defined on the
iterator's text range. The set is empty if no
attributes are defined.

**Returns:** the keys of all attributes

Method Detail

- getRunStart

```java
int getRunStart()
```

Returns the index of the first character of the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:** the index of the first character of the run

- getRunStart

```java
int getRunStart​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

**Parameters:** attribute

- the desired attribute.
**Returns:** the index of the first character of the run

- getRunStart

```java
int getRunStart​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)
```

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

**Parameters:** attributes

- a set of the desired attributes.
**Returns:** the index of the first character of the run

- getRunLimit

```java
int getRunLimit()
```

Returns the index of the first character following the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:** the index of the first character following the run

- getRunLimit

```java
int getRunLimit​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

**Parameters:** attribute

- the desired attribute
**Returns:** the index of the first character following the run

- getRunLimit

```java
int getRunLimit​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)
```

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

**Parameters:** attributes

- a set of the desired attributes
**Returns:** the index of the first character following the run

- getAttributes

```java
Map
<
AttributedCharacterIterator.Attribute
,​
Object
> getAttributes()
```

Returns a map with the attributes defined on the current
character.

**Returns:** a map with the attributes defined on the current character

- getAttribute

```java
Object
getAttribute​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the value of the named

attribute

for the current character.
Returns

null

if the

attribute

is not defined.

**Parameters:** attribute

- the desired attribute
**Returns:** the value of the named

attribute

or

null

- getAllAttributeKeys

```java
Set
<
AttributedCharacterIterator.Attribute
> getAllAttributeKeys()
```

Returns the keys of all attributes defined on the
iterator's text range. The set is empty if no
attributes are defined.

**Returns:** the keys of all attributes

---

#### Method Detail

getRunStart

```java
int getRunStart()
```

Returns the index of the first character of the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:** the index of the first character of the run

---

#### getRunStart

int getRunStart()

Returns the index of the first character of the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

getRunStart

```java
int getRunStart​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

**Parameters:** attribute

- the desired attribute.
**Returns:** the index of the first character of the run

---

#### getRunStart

int getRunStart​(

AttributedCharacterIterator.Attribute

attribute)

Returns the index of the first character of the run
with respect to the given

attribute

containing the current character.

getRunStart

```java
int getRunStart​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)
```

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

**Parameters:** attributes

- a set of the desired attributes.
**Returns:** the index of the first character of the run

---

#### getRunStart

int getRunStart​(

Set

<? extends

AttributedCharacterIterator.Attribute

> attributes)

Returns the index of the first character of the run
with respect to the given

attributes

containing the current character.

getRunLimit

```java
int getRunLimit()
```

Returns the index of the first character following the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

**Returns:** the index of the first character following the run

---

#### getRunLimit

int getRunLimit()

Returns the index of the first character following the run
with respect to all attributes containing the current character.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

Any contiguous text segments having the same attributes (the
same set of attribute/value pairs) are treated as separate runs
if the attributes have been given to those text segments separately.

getRunLimit

```java
int getRunLimit​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

**Parameters:** attribute

- the desired attribute
**Returns:** the index of the first character following the run

---

#### getRunLimit

int getRunLimit​(

AttributedCharacterIterator.Attribute

attribute)

Returns the index of the first character following the run
with respect to the given

attribute

containing the current character.

getRunLimit

```java
int getRunLimit​(
Set
<? extends
AttributedCharacterIterator.Attribute
> attributes)
```

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

**Parameters:** attributes

- a set of the desired attributes
**Returns:** the index of the first character following the run

---

#### getRunLimit

int getRunLimit​(

Set

<? extends

AttributedCharacterIterator.Attribute

> attributes)

Returns the index of the first character following the run
with respect to the given

attributes

containing the current character.

getAttributes

```java
Map
<
AttributedCharacterIterator.Attribute
,​
Object
> getAttributes()
```

Returns a map with the attributes defined on the current
character.

**Returns:** a map with the attributes defined on the current character

---

#### getAttributes

Map

<

AttributedCharacterIterator.Attribute

,​

Object

> getAttributes()

Returns a map with the attributes defined on the current
character.

getAttribute

```java
Object
getAttribute​(
AttributedCharacterIterator.Attribute
attribute)
```

Returns the value of the named

attribute

for the current character.
Returns

null

if the

attribute

is not defined.

**Parameters:** attribute

- the desired attribute
**Returns:** the value of the named

attribute

or

null

---

#### getAttribute

Object

getAttribute​(

AttributedCharacterIterator.Attribute

attribute)

Returns the value of the named

attribute

for the current character.
Returns

null

if the

attribute

is not defined.

getAllAttributeKeys

```java
Set
<
AttributedCharacterIterator.Attribute
> getAllAttributeKeys()
```

Returns the keys of all attributes defined on the
iterator's text range. The set is empty if no
attributes are defined.

**Returns:** the keys of all attributes

---

#### getAllAttributeKeys

Set

<

AttributedCharacterIterator.Attribute

> getAllAttributeKeys()

Returns the keys of all attributes defined on the
iterator's text range. The set is empty if no
attributes are defined.

---

