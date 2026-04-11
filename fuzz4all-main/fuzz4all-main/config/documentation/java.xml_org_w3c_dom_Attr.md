# Interface Attr

**Source:** `java.xml\org\w3c\dom\Attr.html`

### Class Description

```java
public interface
Attr

extends
Node
```

The

Attr

interface represents an attribute in an

Element

object. Typically the allowable values for the
attribute are defined in a schema associated with the document.

Attr

objects inherit the

Node

interface, but
since they are not actually child nodes of the element they describe, the
DOM does not consider them part of the document tree. Thus, the

Node

attributes

parentNode

,

previousSibling

, and

nextSibling

have a

null

value for

Attr

objects. The DOM takes the
view that attributes are properties of elements rather than having a
separate identity from the elements they are associated with; this should
make it more efficient to implement such features as default attributes
associated with all elements of a given type. Furthermore,

Attr

nodes may not be immediate children of a

DocumentFragment

. However, they can be associated with

Element

nodes contained within a

DocumentFragment

. In short, users and implementors of the
DOM need to be aware that

Attr

nodes have some things in
common with other objects inheriting the

Node

interface, but
they also are quite distinct.

The attribute's effective value is determined as follows: if this
attribute has been explicitly assigned any value, that value is the
attribute's effective value; otherwise, if there is a declaration for
this attribute, and that declaration includes a default value, then that
default value is the attribute's effective value; otherwise, the
attribute does not exist on this element in the structure model until it
has been explicitly added. Note that the

Node.nodeValue

attribute on the

Attr

instance can also be used to retrieve
the string version of the attribute's value(s).

If the attribute was not explicitly given a value in the instance
document but has a default value provided by the schema associated with
the document, an attribute node will be created with

specified

set to

false

. Removing attribute
nodes for which a default value is defined in the schema generates a new
attribute node with the default value and

specified

set to

false

. If validation occurred while invoking

Document.normalizeDocument()

, attribute nodes with

specified

equals to

false

are recomputed
according to the default attribute values provided by the schema. If no
default value is associate with this attribute in the schema, the
attribute node is discarded.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**All Superinterfaces:** Node

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the name of this attribute. If

Node.localName

is
different from

null

, this attribute is a qualified name.

---

#### boolean getSpecified()

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise. If the
application changed the value of this attribute node (even if it ends
up having the same value as the default value) then it is set to

true

. The implementation may handle attributes with
default values from other schemas similarly but applications should
use

Document.normalizeDocument()

to guarantee this
information is up-to-date.

---

#### String
getValue()

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

---

#### void setValue​(
String
value)
throws
DOMException

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

#### Element
getOwnerElement()

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

**Since:**
- 1.4, DOM Level 2

---

#### TypeInfo
getSchemaTypeInfo()

The type information associated with this attribute. While the type
information contained in this attribute is guarantee to be correct
after loading the document or invoking

Document.normalizeDocument()

,

schemaTypeInfo

may not be reliable if the node was moved.

**Since:**
- 1.5, DOM Level 3

---

#### boolean isId()

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not. When it is and
its value is unique, the

ownerElement

of this attribute
can be retrieved using the method

Document.getElementById

. The implementation could use several ways to determine if an
attribute node is known to contain an identifier:

- If validation
occurred using an XML Schema [

XML Schema Part 1

]
while loading the document or while invoking

Document.normalizeDocument()

, the post-schema-validation
infoset contributions (PSVI contributions) values are used to
determine if this attribute is a schema-determined ID attribute using
the

schema-determined ID

definition in [

XPointer

]
.
- If validation occurred using a DTD while loading the document or
while invoking

Document.normalizeDocument()

, the infoset

[type definition]

value is used to determine if this attribute is a DTD-determined ID
attribute using the

DTD-determined ID

definition in [

XPointer

]
.
- from the use of the methods

Element.setIdAttribute()

,

Element.setIdAttributeNS()

, or

Element.setIdAttributeNode()

, i.e. it is an
user-determined ID attribute;

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.
- using mechanisms that
are outside the scope of this specification, it is then an
externally-determined ID attribute. This includes using schema
languages different from XML schema and DTD.

If validation occurred while invoking

Document.normalizeDocument()

, all user-determined ID
attributes are reset and all attribute nodes ID information are then
reevaluated in accordance to the schema used. As a consequence, if
the

Attr.schemaTypeInfo

attribute contains an ID type,

isId

will always return true.

**Since:**
- 1.5, DOM Level 3

---

### Additional Sections

#### Interface Attr

**All Superinterfaces:** Node

```java
public interface
Attr

extends
Node
```

The

Attr

interface represents an attribute in an

Element

object. Typically the allowable values for the
attribute are defined in a schema associated with the document.

Attr

objects inherit the

Node

interface, but
since they are not actually child nodes of the element they describe, the
DOM does not consider them part of the document tree. Thus, the

Node

attributes

parentNode

,

previousSibling

, and

nextSibling

have a

null

value for

Attr

objects. The DOM takes the
view that attributes are properties of elements rather than having a
separate identity from the elements they are associated with; this should
make it more efficient to implement such features as default attributes
associated with all elements of a given type. Furthermore,

Attr

nodes may not be immediate children of a

DocumentFragment

. However, they can be associated with

Element

nodes contained within a

DocumentFragment

. In short, users and implementors of the
DOM need to be aware that

Attr

nodes have some things in
common with other objects inheriting the

Node

interface, but
they also are quite distinct.

The attribute's effective value is determined as follows: if this
attribute has been explicitly assigned any value, that value is the
attribute's effective value; otherwise, if there is a declaration for
this attribute, and that declaration includes a default value, then that
default value is the attribute's effective value; otherwise, the
attribute does not exist on this element in the structure model until it
has been explicitly added. Note that the

Node.nodeValue

attribute on the

Attr

instance can also be used to retrieve
the string version of the attribute's value(s).

If the attribute was not explicitly given a value in the instance
document but has a default value provided by the schema associated with
the document, an attribute node will be created with

specified

set to

false

. Removing attribute
nodes for which a default value is defined in the schema generates a new
attribute node with the default value and

specified

set to

false

. If validation occurred while invoking

Document.normalizeDocument()

, attribute nodes with

specified

equals to

false

are recomputed
according to the default attribute values provided by the schema. If no
default value is associate with this attribute in the schema, the
attribute node is discarded.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

Attr

extends

Node

The

Attr

interface represents an attribute in an

Element

object. Typically the allowable values for the
attribute are defined in a schema associated with the document.

Attr

objects inherit the

Node

interface, but
since they are not actually child nodes of the element they describe, the
DOM does not consider them part of the document tree. Thus, the

Node

attributes

parentNode

,

previousSibling

, and

nextSibling

have a

null

value for

Attr

objects. The DOM takes the
view that attributes are properties of elements rather than having a
separate identity from the elements they are associated with; this should
make it more efficient to implement such features as default attributes
associated with all elements of a given type. Furthermore,

Attr

nodes may not be immediate children of a

DocumentFragment

. However, they can be associated with

Element

nodes contained within a

DocumentFragment

. In short, users and implementors of the
DOM need to be aware that

Attr

nodes have some things in
common with other objects inheriting the

Node

interface, but
they also are quite distinct.

The attribute's effective value is determined as follows: if this
attribute has been explicitly assigned any value, that value is the
attribute's effective value; otherwise, if there is a declaration for
this attribute, and that declaration includes a default value, then that
default value is the attribute's effective value; otherwise, the
attribute does not exist on this element in the structure model until it
has been explicitly added. Note that the

Node.nodeValue

attribute on the

Attr

instance can also be used to retrieve
the string version of the attribute's value(s).

If the attribute was not explicitly given a value in the instance
document but has a default value provided by the schema associated with
the document, an attribute node will be created with

specified

set to

false

. Removing attribute
nodes for which a default value is defined in the schema generates a new
attribute node with the default value and

specified

set to

false

. If validation occurred while invoking

Document.normalizeDocument()

, attribute nodes with

specified

equals to

false

are recomputed
according to the default attribute values provided by the schema. If no
default value is associate with this attribute in the schema, the
attribute node is discarded.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

Attr

objects inherit the

Node

interface, but
since they are not actually child nodes of the element they describe, the
DOM does not consider them part of the document tree. Thus, the

Node

attributes

parentNode

,

previousSibling

, and

nextSibling

have a

null

value for

Attr

objects. The DOM takes the
view that attributes are properties of elements rather than having a
separate identity from the elements they are associated with; this should
make it more efficient to implement such features as default attributes
associated with all elements of a given type. Furthermore,

Attr

nodes may not be immediate children of a

DocumentFragment

. However, they can be associated with

Element

nodes contained within a

DocumentFragment

. In short, users and implementors of the
DOM need to be aware that

Attr

nodes have some things in
common with other objects inheriting the

Node

interface, but
they also are quite distinct.

The attribute's effective value is determined as follows: if this
attribute has been explicitly assigned any value, that value is the
attribute's effective value; otherwise, if there is a declaration for
this attribute, and that declaration includes a default value, then that
default value is the attribute's effective value; otherwise, the
attribute does not exist on this element in the structure model until it
has been explicitly added. Note that the

Node.nodeValue

attribute on the

Attr

instance can also be used to retrieve
the string version of the attribute's value(s).

If the attribute was not explicitly given a value in the instance
document but has a default value provided by the schema associated with
the document, an attribute node will be created with

specified

set to

false

. Removing attribute
nodes for which a default value is defined in the schema generates a new
attribute node with the default value and

specified

set to

false

. If validation occurred while invoking

Document.normalizeDocument()

, attribute nodes with

specified

equals to

false

are recomputed
according to the default attribute values provided by the schema. If no
default value is associate with this attribute in the schema, the
attribute node is discarded.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The attribute's effective value is determined as follows: if this
attribute has been explicitly assigned any value, that value is the
attribute's effective value; otherwise, if there is a declaration for
this attribute, and that declaration includes a default value, then that
default value is the attribute's effective value; otherwise, the
attribute does not exist on this element in the structure model until it
has been explicitly added. Note that the

Node.nodeValue

attribute on the

Attr

instance can also be used to retrieve
the string version of the attribute's value(s).

If the attribute was not explicitly given a value in the instance
document but has a default value provided by the schema associated with
the document, an attribute node will be created with

specified

set to

false

. Removing attribute
nodes for which a default value is defined in the schema generates a new
attribute node with the default value and

specified

set to

false

. If validation occurred while invoking

Document.normalizeDocument()

, attribute nodes with

specified

equals to

false

are recomputed
according to the default attribute values provided by the schema. If no
default value is associate with this attribute in the schema, the
attribute node is discarded.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

If the attribute was not explicitly given a value in the instance
document but has a default value provided by the schema associated with
the document, an attribute node will be created with

specified

set to

false

. Removing attribute
nodes for which a default value is defined in the schema generates a new
attribute node with the default value and

specified

set to

false

. If validation occurred while invoking

Document.normalizeDocument()

, attribute nodes with

specified

equals to

false

are recomputed
according to the default attribute values provided by the schema. If no
default value is associate with this attribute in the schema, the
attribute node is discarded.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

In XML, where the value of an attribute can contain entity references,
the child nodes of the

Attr

node may be either

Text

or

EntityReference

nodes (when these are
in use; see the description of

EntityReference

for
discussion).

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The DOM Core represents all attribute values as simple strings, even if
the DTD or schema associated with the document declares them of some
specific type such as tokenized.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The way attribute value normalization is performed by the DOM
implementation depends on how much the implementation knows about the
schema in use. Typically, the

value

and

nodeValue

attributes of an

Attr

node initially
returns the normalized value given by the parser. It is also the case
after

Document.normalizeDocument()

is called (assuming the
right options have been set). But this may not be the case after
mutation, independently of whether the mutation is performed by setting
the string value directly or by changing the

Attr

child
nodes. In particular, this is true when

character
references

are involved, given that they are not represented in the DOM and they
impact attribute value normalization. On the other hand, if the
implementation knows about the schema in use when the attribute value is
changed, and it is of a different type than CDATA, it may normalize it
again at that time. This is especially true of specialized DOM
implementations, such as SVG DOM implementations, which store attribute
values in an internal form different from a string.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The following table gives some examples of the relations between the
attribute value in the original document (parsed attribute), the value as
exposed in the DOM, and the serialization of the value:

Examples of the Original, Normalized and Serialized Values

Examples

Parsed
attribute value

Initial

Attr.value

Serialized attribute value

Character reference

```java
"x&#178;=5"
```

```java
"x²=5"
```

```java
"x&#178;=5"
```

Built-in
character entity

```java
"y&lt;6"
```

```java
"y<6"
```

```java
"y&lt;6"
```

Literal newline between

```java
"x=5&#10;y=6"
```

```java
"x=5 y=6"
```

```java
"x=5&#10;y=6"
```

Normalized newline between

```java
"x=5
y=6"
```

```java
"x=5 y=6"
```

```java
"x=5 y=6"
```

Entity

e

with literal newline

```java
<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"
```

Dependent on Implementation and Load Options

Dependent on Implementation and Load/Save Options

See also the

Document Object Model (DOM) Level 3 Core Specification

.

"x&#178;=5"

"x²=5"

"y&lt;6"

"y<6"

"x=5&#10;y=6"

"x=5 y=6"

"x=5
y=6"

<!ENTITY e '...&#10;...'> [...]> "x=5&e;y=6"

See also the

Document Object Model (DOM) Level 3 Core Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.

Node

ATTRIBUTE_NODE

,

CDATA_SECTION_NODE

,

COMMENT_NODE

,

DOCUMENT_FRAGMENT_NODE

,

DOCUMENT_NODE

,

DOCUMENT_POSITION_CONTAINED_BY

,

DOCUMENT_POSITION_CONTAINS

,

DOCUMENT_POSITION_DISCONNECTED

,

DOCUMENT_POSITION_FOLLOWING

,

DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

,

DOCUMENT_POSITION_PRECEDING

,

DOCUMENT_TYPE_NODE

,

ELEMENT_NODE

,

ENTITY_NODE

,

ENTITY_REFERENCE_NODE

,

NOTATION_NODE

,

PROCESSING_INSTRUCTION_NODE

,

TEXT_NODE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this attribute.

Element

getOwnerElement

()

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

TypeInfo

getSchemaTypeInfo

()

The type information associated with this attribute.

boolean

getSpecified

()

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise.

String

getValue

()

On retrieval, the value of the attribute is returned as a string.

boolean

isId

()

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not.

void

setValue

​(

String

value)

On retrieval, the value of the attribute is returned as a string.

- Methods declared in interface org.w3c.dom.

Node

appendChild

,

cloneNode

,

compareDocumentPosition

,

getAttributes

,

getBaseURI

,

getChildNodes

,

getFeature

,

getFirstChild

,

getLastChild

,

getLocalName

,

getNamespaceURI

,

getNextSibling

,

getNodeName

,

getNodeType

,

getNodeValue

,

getOwnerDocument

,

getParentNode

,

getPrefix

,

getPreviousSibling

,

getTextContent

,

getUserData

,

hasAttributes

,

hasChildNodes

,

insertBefore

,

isDefaultNamespace

,

isEqualNode

,

isSameNode

,

isSupported

,

lookupNamespaceURI

,

lookupPrefix

,

normalize

,

removeChild

,

replaceChild

,

setNodeValue

,

setPrefix

,

setTextContent

,

setUserData

Field Summary

- Fields declared in interface org.w3c.dom.

Node

ATTRIBUTE_NODE

,

CDATA_SECTION_NODE

,

COMMENT_NODE

,

DOCUMENT_FRAGMENT_NODE

,

DOCUMENT_NODE

,

DOCUMENT_POSITION_CONTAINED_BY

,

DOCUMENT_POSITION_CONTAINS

,

DOCUMENT_POSITION_DISCONNECTED

,

DOCUMENT_POSITION_FOLLOWING

,

DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

,

DOCUMENT_POSITION_PRECEDING

,

DOCUMENT_TYPE_NODE

,

ELEMENT_NODE

,

ENTITY_NODE

,

ENTITY_REFERENCE_NODE

,

NOTATION_NODE

,

PROCESSING_INSTRUCTION_NODE

,

TEXT_NODE

---

#### Field Summary

Fields declared in interface org.w3c.dom.

Node

ATTRIBUTE_NODE

,

CDATA_SECTION_NODE

,

COMMENT_NODE

,

DOCUMENT_FRAGMENT_NODE

,

DOCUMENT_NODE

,

DOCUMENT_POSITION_CONTAINED_BY

,

DOCUMENT_POSITION_CONTAINS

,

DOCUMENT_POSITION_DISCONNECTED

,

DOCUMENT_POSITION_FOLLOWING

,

DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC

,

DOCUMENT_POSITION_PRECEDING

,

DOCUMENT_TYPE_NODE

,

ELEMENT_NODE

,

ENTITY_NODE

,

ENTITY_REFERENCE_NODE

,

NOTATION_NODE

,

PROCESSING_INSTRUCTION_NODE

,

TEXT_NODE

---

#### Fields declared in interface org.w3c.dom. Node

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this attribute.

Element

getOwnerElement

()

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

TypeInfo

getSchemaTypeInfo

()

The type information associated with this attribute.

boolean

getSpecified

()

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise.

String

getValue

()

On retrieval, the value of the attribute is returned as a string.

boolean

isId

()

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not.

void

setValue

​(

String

value)

On retrieval, the value of the attribute is returned as a string.

- Methods declared in interface org.w3c.dom.

Node

appendChild

,

cloneNode

,

compareDocumentPosition

,

getAttributes

,

getBaseURI

,

getChildNodes

,

getFeature

,

getFirstChild

,

getLastChild

,

getLocalName

,

getNamespaceURI

,

getNextSibling

,

getNodeName

,

getNodeType

,

getNodeValue

,

getOwnerDocument

,

getParentNode

,

getPrefix

,

getPreviousSibling

,

getTextContent

,

getUserData

,

hasAttributes

,

hasChildNodes

,

insertBefore

,

isDefaultNamespace

,

isEqualNode

,

isSameNode

,

isSupported

,

lookupNamespaceURI

,

lookupPrefix

,

normalize

,

removeChild

,

replaceChild

,

setNodeValue

,

setPrefix

,

setTextContent

,

setUserData

---

#### Method Summary

Returns the name of this attribute.

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

The type information associated with this attribute.

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise.

On retrieval, the value of the attribute is returned as a string.

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not.

Methods declared in interface org.w3c.dom.

Node

appendChild

,

cloneNode

,

compareDocumentPosition

,

getAttributes

,

getBaseURI

,

getChildNodes

,

getFeature

,

getFirstChild

,

getLastChild

,

getLocalName

,

getNamespaceURI

,

getNextSibling

,

getNodeName

,

getNodeType

,

getNodeValue

,

getOwnerDocument

,

getParentNode

,

getPrefix

,

getPreviousSibling

,

getTextContent

,

getUserData

,

hasAttributes

,

hasChildNodes

,

insertBefore

,

isDefaultNamespace

,

isEqualNode

,

isSameNode

,

isSupported

,

lookupNamespaceURI

,

lookupPrefix

,

normalize

,

removeChild

,

replaceChild

,

setNodeValue

,

setPrefix

,

setTextContent

,

setUserData

---

#### Methods declared in interface org.w3c.dom. Node

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the name of this attribute. If

Node.localName

is
different from

null

, this attribute is a qualified name.

- getSpecified

```java
boolean getSpecified()
```

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise. If the
application changed the value of this attribute node (even if it ends
up having the same value as the default value) then it is set to

true

. The implementation may handle attributes with
default values from other schemas similarly but applications should
use

Document.normalizeDocument()

to guarantee this
information is up-to-date.

- getValue

```java
String
getValue()
```

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

- setValue

```java
void setValue​(
String
value)
throws
DOMException
```

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

- getOwnerElement

```java
Element
getOwnerElement()
```

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

**Since:** 1.4, DOM Level 2

- getSchemaTypeInfo

```java
TypeInfo
getSchemaTypeInfo()
```

The type information associated with this attribute. While the type
information contained in this attribute is guarantee to be correct
after loading the document or invoking

Document.normalizeDocument()

,

schemaTypeInfo

may not be reliable if the node was moved.

**Since:** 1.5, DOM Level 3

- isId

```java
boolean isId()
```

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not. When it is and
its value is unique, the

ownerElement

of this attribute
can be retrieved using the method

Document.getElementById

. The implementation could use several ways to determine if an
attribute node is known to contain an identifier:

- If validation
occurred using an XML Schema [

XML Schema Part 1

]
while loading the document or while invoking

Document.normalizeDocument()

, the post-schema-validation
infoset contributions (PSVI contributions) values are used to
determine if this attribute is a schema-determined ID attribute using
the

schema-determined ID

definition in [

XPointer

]
.
- If validation occurred using a DTD while loading the document or
while invoking

Document.normalizeDocument()

, the infoset

[type definition]

value is used to determine if this attribute is a DTD-determined ID
attribute using the

DTD-determined ID

definition in [

XPointer

]
.
- from the use of the methods

Element.setIdAttribute()

,

Element.setIdAttributeNS()

, or

Element.setIdAttributeNode()

, i.e. it is an
user-determined ID attribute;

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.
- using mechanisms that
are outside the scope of this specification, it is then an
externally-determined ID attribute. This includes using schema
languages different from XML schema and DTD.

If validation occurred while invoking

Document.normalizeDocument()

, all user-determined ID
attributes are reset and all attribute nodes ID information are then
reevaluated in accordance to the schema used. As a consequence, if
the

Attr.schemaTypeInfo

attribute contains an ID type,

isId

will always return true.

**Since:** 1.5, DOM Level 3

Method Detail

- getName

```java
String
getName()
```

Returns the name of this attribute. If

Node.localName

is
different from

null

, this attribute is a qualified name.

- getSpecified

```java
boolean getSpecified()
```

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise. If the
application changed the value of this attribute node (even if it ends
up having the same value as the default value) then it is set to

true

. The implementation may handle attributes with
default values from other schemas similarly but applications should
use

Document.normalizeDocument()

to guarantee this
information is up-to-date.

- getValue

```java
String
getValue()
```

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

- setValue

```java
void setValue​(
String
value)
throws
DOMException
```

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

- getOwnerElement

```java
Element
getOwnerElement()
```

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

**Since:** 1.4, DOM Level 2

- getSchemaTypeInfo

```java
TypeInfo
getSchemaTypeInfo()
```

The type information associated with this attribute. While the type
information contained in this attribute is guarantee to be correct
after loading the document or invoking

Document.normalizeDocument()

,

schemaTypeInfo

may not be reliable if the node was moved.

**Since:** 1.5, DOM Level 3

- isId

```java
boolean isId()
```

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not. When it is and
its value is unique, the

ownerElement

of this attribute
can be retrieved using the method

Document.getElementById

. The implementation could use several ways to determine if an
attribute node is known to contain an identifier:

- If validation
occurred using an XML Schema [

XML Schema Part 1

]
while loading the document or while invoking

Document.normalizeDocument()

, the post-schema-validation
infoset contributions (PSVI contributions) values are used to
determine if this attribute is a schema-determined ID attribute using
the

schema-determined ID

definition in [

XPointer

]
.
- If validation occurred using a DTD while loading the document or
while invoking

Document.normalizeDocument()

, the infoset

[type definition]

value is used to determine if this attribute is a DTD-determined ID
attribute using the

DTD-determined ID

definition in [

XPointer

]
.
- from the use of the methods

Element.setIdAttribute()

,

Element.setIdAttributeNS()

, or

Element.setIdAttributeNode()

, i.e. it is an
user-determined ID attribute;

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.
- using mechanisms that
are outside the scope of this specification, it is then an
externally-determined ID attribute. This includes using schema
languages different from XML schema and DTD.

If validation occurred while invoking

Document.normalizeDocument()

, all user-determined ID
attributes are reset and all attribute nodes ID information are then
reevaluated in accordance to the schema used. As a consequence, if
the

Attr.schemaTypeInfo

attribute contains an ID type,

isId

will always return true.

**Since:** 1.5, DOM Level 3

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name of this attribute. If

Node.localName

is
different from

null

, this attribute is a qualified name.

---

#### getName

String

getName()

Returns the name of this attribute. If

Node.localName

is
different from

null

, this attribute is a qualified name.

getSpecified

```java
boolean getSpecified()
```

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise. If the
application changed the value of this attribute node (even if it ends
up having the same value as the default value) then it is set to

true

. The implementation may handle attributes with
default values from other schemas similarly but applications should
use

Document.normalizeDocument()

to guarantee this
information is up-to-date.

---

#### getSpecified

boolean getSpecified()

True

if this attribute was explicitly given a value in
the instance document,

false

otherwise. If the
application changed the value of this attribute node (even if it ends
up having the same value as the default value) then it is set to

true

. The implementation may handle attributes with
default values from other schemas similarly but applications should
use

Document.normalizeDocument()

to guarantee this
information is up-to-date.

getValue

```java
String
getValue()
```

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

---

#### getValue

String

getValue()

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

setValue

```java
void setValue​(
String
value)
throws
DOMException
```

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

#### setValue

void setValue​(

String

value)
throws

DOMException

On retrieval, the value of the attribute is returned as a string.
Character and general entity references are replaced with their
values. See also the method

getAttribute

on the

Element

interface.

On setting, this creates a

Text

node with the unparsed
contents of the string, i.e. any characters that an XML processor
would recognize as markup are instead treated as literal text. See
also the method

Element.setAttribute()

.

Some specialized implementations, such as some [

SVG 1.1

]
implementations, may do normalization automatically, even after
mutation; in such case, the value on retrieval may differ from the
value on setting.

getOwnerElement

```java
Element
getOwnerElement()
```

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

**Since:** 1.4, DOM Level 2

---

#### getOwnerElement

Element

getOwnerElement()

The

Element

node this attribute is attached to or

null

if this attribute is not in use.

getSchemaTypeInfo

```java
TypeInfo
getSchemaTypeInfo()
```

The type information associated with this attribute. While the type
information contained in this attribute is guarantee to be correct
after loading the document or invoking

Document.normalizeDocument()

,

schemaTypeInfo

may not be reliable if the node was moved.

**Since:** 1.5, DOM Level 3

---

#### getSchemaTypeInfo

TypeInfo

getSchemaTypeInfo()

The type information associated with this attribute. While the type
information contained in this attribute is guarantee to be correct
after loading the document or invoking

Document.normalizeDocument()

,

schemaTypeInfo

may not be reliable if the node was moved.

isId

```java
boolean isId()
```

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not. When it is and
its value is unique, the

ownerElement

of this attribute
can be retrieved using the method

Document.getElementById

. The implementation could use several ways to determine if an
attribute node is known to contain an identifier:

- If validation
occurred using an XML Schema [

XML Schema Part 1

]
while loading the document or while invoking

Document.normalizeDocument()

, the post-schema-validation
infoset contributions (PSVI contributions) values are used to
determine if this attribute is a schema-determined ID attribute using
the

schema-determined ID

definition in [

XPointer

]
.
- If validation occurred using a DTD while loading the document or
while invoking

Document.normalizeDocument()

, the infoset

[type definition]

value is used to determine if this attribute is a DTD-determined ID
attribute using the

DTD-determined ID

definition in [

XPointer

]
.
- from the use of the methods

Element.setIdAttribute()

,

Element.setIdAttributeNS()

, or

Element.setIdAttributeNode()

, i.e. it is an
user-determined ID attribute;

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.
- using mechanisms that
are outside the scope of this specification, it is then an
externally-determined ID attribute. This includes using schema
languages different from XML schema and DTD.

If validation occurred while invoking

Document.normalizeDocument()

, all user-determined ID
attributes are reset and all attribute nodes ID information are then
reevaluated in accordance to the schema used. As a consequence, if
the

Attr.schemaTypeInfo

attribute contains an ID type,

isId

will always return true.

**Since:** 1.5, DOM Level 3

---

#### isId

boolean isId()

Returns whether this attribute is known to be of type ID (i.e. to
contain an identifier for its owner element) or not. When it is and
its value is unique, the

ownerElement

of this attribute
can be retrieved using the method

Document.getElementById

. The implementation could use several ways to determine if an
attribute node is known to contain an identifier:

- If validation
occurred using an XML Schema [

XML Schema Part 1

]
while loading the document or while invoking

Document.normalizeDocument()

, the post-schema-validation
infoset contributions (PSVI contributions) values are used to
determine if this attribute is a schema-determined ID attribute using
the

schema-determined ID

definition in [

XPointer

]
.
- If validation occurred using a DTD while loading the document or
while invoking

Document.normalizeDocument()

, the infoset

[type definition]

value is used to determine if this attribute is a DTD-determined ID
attribute using the

DTD-determined ID

definition in [

XPointer

]
.
- from the use of the methods

Element.setIdAttribute()

,

Element.setIdAttributeNS()

, or

Element.setIdAttributeNode()

, i.e. it is an
user-determined ID attribute;

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.
- using mechanisms that
are outside the scope of this specification, it is then an
externally-determined ID attribute. This includes using schema
languages different from XML schema and DTD.

If validation occurred while invoking

Document.normalizeDocument()

, all user-determined ID
attributes are reset and all attribute nodes ID information are then
reevaluated in accordance to the schema used. As a consequence, if
the

Attr.schemaTypeInfo

attribute contains an ID type,

isId

will always return true.

If validation
occurred using an XML Schema [

XML Schema Part 1

]
while loading the document or while invoking

Document.normalizeDocument()

, the post-schema-validation
infoset contributions (PSVI contributions) values are used to
determine if this attribute is a schema-determined ID attribute using
the

schema-determined ID

definition in [

XPointer

]
.

If validation occurred using a DTD while loading the document or
while invoking

Document.normalizeDocument()

, the infoset

[type definition]

value is used to determine if this attribute is a DTD-determined ID
attribute using the

DTD-determined ID

definition in [

XPointer

]
.

from the use of the methods

Element.setIdAttribute()

,

Element.setIdAttributeNS()

, or

Element.setIdAttributeNode()

, i.e. it is an
user-determined ID attribute;

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.

using mechanisms that
are outside the scope of this specification, it is then an
externally-determined ID attribute. This includes using schema
languages different from XML schema and DTD.

Note:

XPointer framework (see section 3.2 in [

XPointer

]
) consider the DOM user-determined ID attribute as being part of the
XPointer externally-determined ID definition.

---

