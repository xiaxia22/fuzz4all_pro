# Class IIOMetadataNode

**Source:** `java.desktop\javax\imageio\metadata\IIOMetadataNode.html`

### Class Description

```java
public class
IIOMetadataNode

extends
Object

implements
Element
,
NodeList
```

A class representing a node in a meta-data tree, which implements
the

org.w3c.dom.Element

interface and additionally allows
for the storage of non-textual objects via the

getUserObject

and

setUserObject

methods.

This class is not intended to be used for general XML
processing. In particular,

Element

nodes created
within the Image I/O API are not compatible with those created by
Sun's standard implementation of the

org.w3.dom

API.
In particular, the implementation is tuned for simple uses and may
not perform well for intensive processing.

Namespaces are ignored in this implementation. The terms "tag
name" and "node name" are always considered to be synonymous.

Note:

The DOM Level 3 specification added a number of new methods to the

Node

,

Element

and

Attr

interfaces that are not
of value to the

IIOMetadataNode

implementation or specification.

Calling such methods on an

IIOMetadataNode

, or an

Attr

instance returned from an

IIOMetadataNode

will result in a

DOMException

being thrown.

**All Implemented Interfaces:** Element

,

Node

,

NodeList

---

### Field Details

*No entries found.*

### Constructor Details

#### public IIOMetadataNode()

Constructs an empty

IIOMetadataNode

.

---

#### public IIOMetadataNode​(
String
nodeName)

Constructs an

IIOMetadataNode

with a given node
name.

**Parameters:**
- nodeName

- the name of the node, as a

String

.

---

### Method Details

#### public
String
getNodeName()

Returns the node name associated with this node.

**Specified by:**
- getNodeName

in interface

Node

**Returns:**
- the node name, as a

String

.

---

#### public
String
getNodeValue()

Returns the value associated with this node.

**Specified by:**
- getNodeValue

in interface

Node

**Returns:**
- the node value, as a

String

.

---

#### public void setNodeValue​(
String
nodeValue)

Sets the

String

value associated with this node.

**Specified by:**
- setNodeValue

in interface

Node

---

#### public short getNodeType()

Returns the node type, which is always

ELEMENT_NODE

.

**Specified by:**
- getNodeType

in interface

Node

**Returns:**
- the

short

value

ELEMENT_NODE

.

---

#### public
Node
getParentNode()

Returns the parent of this node. A

null

value
indicates that the node is the root of its own tree. To add a
node to an existing tree, use one of the

insertBefore

,

replaceChild

, or

appendChild

methods.

**Specified by:**
- getParentNode

in interface

Node

**Returns:**
- the parent, as a

Node

.

**See Also:**
- insertBefore(org.w3c.dom.Node, org.w3c.dom.Node)

,

replaceChild(org.w3c.dom.Node, org.w3c.dom.Node)

,

appendChild(org.w3c.dom.Node)

---

#### public
NodeList
getChildNodes()

Returns a

NodeList

that contains all children of this node.
If there are no children, this is a

NodeList

containing
no nodes.

**Specified by:**
- getChildNodes

in interface

Node

**Returns:**
- the children as a

NodeList

---

#### public
Node
getFirstChild()

Returns the first child of this node, or

null

if
the node has no children.

**Specified by:**
- getFirstChild

in interface

Node

**Returns:**
- the first child, as a

Node

, or

null

---

#### public
Node
getLastChild()

Returns the last child of this node, or

null

if
the node has no children.

**Specified by:**
- getLastChild

in interface

Node

**Returns:**
- the last child, as a

Node

, or

null

.

---

#### public
Node
getPreviousSibling()

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

**Specified by:**
- getPreviousSibling

in interface

Node

**Returns:**
- the previous sibling, as a

Node

, or

null

.

---

#### public
Node
getNextSibling()

Returns the next sibling of this node, or

null

if
the node has no next sibling.

**Specified by:**
- getNextSibling

in interface

Node

**Returns:**
- the next sibling, as a

Node

, or

null

.

---

#### public
NamedNodeMap
getAttributes()

Returns a

NamedNodeMap

containing the attributes of
this node.

**Specified by:**
- getAttributes

in interface

Node

**Returns:**
- a

NamedNodeMap

containing the attributes of
this node.

---

#### public
Document
getOwnerDocument()

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

**Specified by:**
- getOwnerDocument

in interface

Node

**Returns:**
- null

.

---

#### public
Node
insertBefore​(
Node
newChild,

Node
refChild)

Inserts the node

newChild

before the existing
child node

refChild

. If

refChild

is

null

, insert

newChild

at the end of
the list of children.

**Specified by:**
- insertBefore

in interface

Node

**Parameters:**
- newChild

- the

Node

to insert.
- refChild

- the reference

Node

.

**Returns:**
- the node being inserted.

**Throws:**
- IllegalArgumentException

- if

newChild

is

null

.

---

#### public
Node
replaceChild​(
Node
newChild,

Node
oldChild)

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

**Specified by:**
- replaceChild

in interface

Node

**Parameters:**
- newChild

- the

Node

to insert.
- oldChild

- the

Node

to be replaced.

**Returns:**
- the node replaced.

**Throws:**
- IllegalArgumentException

- if

newChild

is

null

.

---

#### public
Node
removeChild​(
Node
oldChild)

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

**Specified by:**
- removeChild

in interface

Node

**Parameters:**
- oldChild

- the

Node

to be removed.

**Returns:**
- the node removed.

**Throws:**
- IllegalArgumentException

- if

oldChild

is

null

.

---

#### public
Node
appendChild​(
Node
newChild)

Adds the node

newChild

to the end of the list of
children of this node.

**Specified by:**
- appendChild

in interface

Node

**Parameters:**
- newChild

- the

Node

to insert.

**Returns:**
- the node added.

**Throws:**
- IllegalArgumentException

- if

newChild

is

null

.

---

#### public boolean hasChildNodes()

Returns

true

if this node has child nodes.

**Specified by:**
- hasChildNodes

in interface

Node

**Returns:**
- true

if this node has children.

---

#### public
Node
cloneNode​(boolean deep)

Returns a duplicate of this node. The duplicate node has no
parent (

getParentNode

returns

null

).
If a shallow clone is being performed (

deep

is

false

), the new node will not have any children or
siblings. If a deep clone is being performed, the new node
will form the root of a complete cloned subtree.

**Specified by:**
- cloneNode

in interface

Node

**Parameters:**
- deep

- if

true

, recursively clone the subtree
under the specified node; if

false

, clone only the
node itself.

**Returns:**
- the duplicate node.

---

#### public void normalize()

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

**Specified by:**
- normalize

in interface

Node

---

#### public boolean isSupported​(
String
feature,

String
version)

Returns

false

since DOM features are not
supported.

**Specified by:**
- isSupported

in interface

Node

**Parameters:**
- feature

- a

String

, which is ignored.
- version

- a

String

, which is ignored.

**Returns:**
- false

.

---

#### public
String
getNamespaceURI()
throws
DOMException

Returns

null

, since namespaces are not supported.

**Specified by:**
- getNamespaceURI

in interface

Node

**Throws:**
- DOMException

---

#### public
String
getPrefix()

Returns

null

, since namespaces are not supported.

**Specified by:**
- getPrefix

in interface

Node

**Returns:**
- null

.

**See Also:**
- setPrefix(java.lang.String)

---

#### public void setPrefix​(
String
prefix)

Does nothing, since namespaces are not supported.

**Specified by:**
- setPrefix

in interface

Node

**Parameters:**
- prefix

- a

String

, which is ignored.

**See Also:**
- getPrefix()

---

#### public
String
getLocalName()

Equivalent to

getNodeName

.

**Specified by:**
- getLocalName

in interface

Node

**Returns:**
- the node name, as a

String

.

---

#### public
String
getTagName()

Equivalent to

getNodeName

.

**Specified by:**
- getTagName

in interface

Element

**Returns:**
- the node name, as a

String

---

#### public
String
getAttribute​(
String
name)

Retrieves an attribute value by name.

**Specified by:**
- getAttribute

in interface

Element

**Parameters:**
- name

- The name of the attribute to retrieve.

**Returns:**
- The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.

---

#### public
String
getAttributeNS​(
String
namespaceURI,

String
localName)

Equivalent to

getAttribute(localName)

.

**Specified by:**
- getAttributeNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the attribute to retrieve.
- localName

- The local name of the attribute to retrieve.

**Returns:**
- The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.

**See Also:**
- setAttributeNS(java.lang.String, java.lang.String, java.lang.String)

---

#### public void setAttributeNS​(
String
namespaceURI,

String
qualifiedName,

String
value)

Equivalent to

setAttribute(qualifiedName, value)

.

**Specified by:**
- setAttributeNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the attribute to create or
alter.
- qualifiedName

- The qualified name of the attribute to create or
alter.
- value

- The value to set in string form.

**See Also:**
- getAttributeNS(java.lang.String, java.lang.String)

---

#### public void removeAttributeNS​(
String
namespaceURI,

String
localName)

Equivalent to

removeAttribute(localName)

.

**Specified by:**
- removeAttributeNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the attribute to remove.
- localName

- The local name of the attribute to remove.

---

#### public
Attr
getAttributeNodeNS​(
String
namespaceURI,

String
localName)

Equivalent to

getAttributeNode(localName)

.

**Specified by:**
- getAttributeNodeNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the attribute to retrieve.
- localName

- The local name of the attribute to retrieve.

**Returns:**
- The

Attr

node with the specified attribute local
name and namespace URI or

null

if there is no such
attribute.

**See Also:**
- setAttributeNodeNS(org.w3c.dom.Attr)

---

#### public
Attr
setAttributeNodeNS​(
Attr
newAttr)

Equivalent to

setAttributeNode(newAttr)

.

**Specified by:**
- setAttributeNodeNS

in interface

Element

**Parameters:**
- newAttr

- The

Attr

node to add to the attribute list.

**Returns:**
- If the

newAttr

attribute replaces an existing
attribute with the same local name and namespace URI, the replaced

Attr

node is returned, otherwise

null

is
returned.

**See Also:**
- getAttributeNodeNS(java.lang.String, java.lang.String)

---

#### public
NodeList
getElementsByTagNameNS​(
String
namespaceURI,

String
localName)

Equivalent to

getElementsByTagName(localName)

.

**Specified by:**
- getElementsByTagNameNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the elements to match on. The
special value "*" matches all namespaces.
- localName

- The local name of the elements to match on. The
special value "*" matches all local names.

**Returns:**
- A new

NodeList

object containing all the matched

Elements

.

---

#### public boolean hasAttributeNS​(
String
namespaceURI,

String
localName)

Equivalent to

hasAttribute(localName)

.

**Specified by:**
- hasAttributeNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the attribute to look for.
- localName

- The local name of the attribute to look for.

**Returns:**
- true

if an attribute with the given local name
and namespace URI is specified or has a default value on this
element,

false

otherwise.

---

#### public
Object
getUserObject()

Returns the

Object

value associated with this node.

**Returns:**
- the user

Object

.

**See Also:**
- setUserObject(java.lang.Object)

---

#### public void setUserObject​(
Object
userObject)

Sets the value associated with this node.

**Parameters:**
- userObject

- the user

Object

.

**See Also:**
- getUserObject()

---

#### public void setIdAttribute​(
String
name,
boolean isId)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- setIdAttribute

in interface

Element

**Parameters:**
- name

- The name of the attribute.
- isId

- Whether the attribute is a of type ID.

**Throws:**
- DOMException

- always.

---

#### public void setIdAttributeNS​(
String
namespaceURI,

String
localName,
boolean isId)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- setIdAttributeNS

in interface

Element

**Parameters:**
- namespaceURI

- The namespace URI of the attribute.
- localName

- The local name of the attribute.
- isId

- Whether the attribute is a of type ID.

**Throws:**
- DOMException

- always.

---

#### public void setIdAttributeNode​(
Attr
idAttr,
boolean isId)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- setIdAttributeNode

in interface

Element

**Parameters:**
- idAttr

- The attribute node.
- isId

- Whether the attribute is a of type ID.

**Throws:**
- DOMException

- always.

---

#### public
TypeInfo
getSchemaTypeInfo()
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- getSchemaTypeInfo

in interface

Element

**Throws:**
- DOMException

- always.

---

#### public
Object
setUserData​(
String
key,

Object
data,

UserDataHandler
handler)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- setUserData

in interface

Node

**Parameters:**
- key

- The key to associate the object to.
- data

- The object to associate to the given key, or

null

to remove any existing association to that key.
- handler

- The handler to associate to that key, or

null

.

**Returns:**
- Returns the

DOMUserData

previously associated to
the given key on this node, or

null

if there was none.

**Throws:**
- DOMException

- always.

---

#### public
Object
getUserData​(
String
key)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- getUserData

in interface

Node

**Parameters:**
- key

- The key the object is associated to.

**Returns:**
- Returns the

DOMUserData

associated to the given
key on this node, or

null

if there was none.

**Throws:**
- DOMException

- always.

---

#### public
Object
getFeature​(
String
feature,

String
version)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- getFeature

in interface

Node

**Parameters:**
- feature

- The name of the feature requested. Note that any plus
sign "+" prepended to the name of the feature will be ignored since
it is not significant in the context of this method.
- version

- This is the version number of the feature to test.

**Returns:**
- Returns an object which implements the specialized APIs of
the specified feature and version, if any, or

null

if
there is no object which implements interfaces associated with that
feature. If the

DOMObject

returned by this method
implements the

Node

interface, it must delegate to the
primary core

Node

and not return results inconsistent
with the primary core

Node

such as attributes,
childNodes, etc.

**Throws:**
- DOMException

- always.

---

#### public boolean isSameNode​(
Node
node)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- isSameNode

in interface

Node

**Parameters:**
- node

- The node to test against.

**Returns:**
- Returns

true

if the nodes are the same,

false

otherwise.

**Throws:**
- DOMException

- always.

---

#### public boolean isEqualNode​(
Node
node)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- isEqualNode

in interface

Node

**Parameters:**
- node

- The node to compare equality with.

**Returns:**
- Returns

true

if the nodes are equal,

false

otherwise.

**Throws:**
- DOMException

- always.

---

#### public
String
lookupNamespaceURI​(
String
prefix)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- lookupNamespaceURI

in interface

Node

**Parameters:**
- prefix

- The prefix to look for. If this parameter is

null

, the method will return the default namespace URI
if any.

**Returns:**
- Returns the associated namespace URI or

null

if
none is found.

**Throws:**
- DOMException

- always.

---

#### public boolean isDefaultNamespace​(
String
namespaceURI)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- isDefaultNamespace

in interface

Node

**Parameters:**
- namespaceURI

- The namespace URI to look for.

**Returns:**
- Returns

true

if the specified

namespaceURI

is the default namespace,

false

otherwise.

**Throws:**
- DOMException

- always.

---

#### public
String
lookupPrefix​(
String
namespaceURI)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- lookupPrefix

in interface

Node

**Parameters:**
- namespaceURI

- The namespace URI to look for.

**Returns:**
- Returns an associated namespace prefix if found or

null

if none is found. If more than one prefix are
associated to the namespace prefix, the returned namespace prefix
is implementation dependent.

**Throws:**
- DOMException

- always.

---

#### public
String
getTextContent()
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- getTextContent

in interface

Node

**Throws:**
- DOMException

- always.

---

#### public void setTextContent​(
String
textContent)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- setTextContent

in interface

Node

**Throws:**
- DOMException

- always.

---

#### public short compareDocumentPosition​(
Node
other)
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- compareDocumentPosition

in interface

Node

**Parameters:**
- other

- The node to compare against the reference node.

**Returns:**
- Returns how the node is positioned relatively to the reference
node.

**Throws:**
- DOMException

- always.

---

#### public
String
getBaseURI()
throws
DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:**
- getBaseURI

in interface

Node

**Throws:**
- DOMException

- always.

---

### Additional Sections

#### Class IIOMetadataNode

java.lang.Object

- javax.imageio.metadata.IIOMetadataNode

javax.imageio.metadata.IIOMetadataNode

**All Implemented Interfaces:** Element

,

Node

,

NodeList

```java
public class
IIOMetadataNode

extends
Object

implements
Element
,
NodeList
```

A class representing a node in a meta-data tree, which implements
the

org.w3c.dom.Element

interface and additionally allows
for the storage of non-textual objects via the

getUserObject

and

setUserObject

methods.

This class is not intended to be used for general XML
processing. In particular,

Element

nodes created
within the Image I/O API are not compatible with those created by
Sun's standard implementation of the

org.w3.dom

API.
In particular, the implementation is tuned for simple uses and may
not perform well for intensive processing.

Namespaces are ignored in this implementation. The terms "tag
name" and "node name" are always considered to be synonymous.

Note:

The DOM Level 3 specification added a number of new methods to the

Node

,

Element

and

Attr

interfaces that are not
of value to the

IIOMetadataNode

implementation or specification.

Calling such methods on an

IIOMetadataNode

, or an

Attr

instance returned from an

IIOMetadataNode

will result in a

DOMException

being thrown.

**See Also:** IIOMetadata.getAsTree(java.lang.String)

,

IIOMetadata.setFromTree(java.lang.String, org.w3c.dom.Node)

,

IIOMetadata.mergeTree(java.lang.String, org.w3c.dom.Node)

public class

IIOMetadataNode

extends

Object

implements

Element

,

NodeList

A class representing a node in a meta-data tree, which implements
the

org.w3c.dom.Element

interface and additionally allows
for the storage of non-textual objects via the

getUserObject

and

setUserObject

methods.

This class is not intended to be used for general XML
processing. In particular,

Element

nodes created
within the Image I/O API are not compatible with those created by
Sun's standard implementation of the

org.w3.dom

API.
In particular, the implementation is tuned for simple uses and may
not perform well for intensive processing.

Namespaces are ignored in this implementation. The terms "tag
name" and "node name" are always considered to be synonymous.

Note:

The DOM Level 3 specification added a number of new methods to the

Node

,

Element

and

Attr

interfaces that are not
of value to the

IIOMetadataNode

implementation or specification.

Calling such methods on an

IIOMetadataNode

, or an

Attr

instance returned from an

IIOMetadataNode

will result in a

DOMException

being thrown.

This class is not intended to be used for general XML
processing. In particular,

Element

nodes created
within the Image I/O API are not compatible with those created by
Sun's standard implementation of the

org.w3.dom

API.
In particular, the implementation is tuned for simple uses and may
not perform well for intensive processing.

Namespaces are ignored in this implementation. The terms "tag
name" and "node name" are always considered to be synonymous.

Note:

The DOM Level 3 specification added a number of new methods to the

Node

,

Element

and

Attr

interfaces that are not
of value to the

IIOMetadataNode

implementation or specification.

Calling such methods on an

IIOMetadataNode

, or an

Attr

instance returned from an

IIOMetadataNode

will result in a

DOMException

being thrown.

Namespaces are ignored in this implementation. The terms "tag
name" and "node name" are always considered to be synonymous.

Note:

The DOM Level 3 specification added a number of new methods to the

Node

,

Element

and

Attr

interfaces that are not
of value to the

IIOMetadataNode

implementation or specification.

Calling such methods on an

IIOMetadataNode

, or an

Attr

instance returned from an

IIOMetadataNode

will result in a

DOMException

being thrown.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IIOMetadataNode

()

Constructs an empty

IIOMetadataNode

.

IIOMetadataNode

​(

String

nodeName)

Constructs an

IIOMetadataNode

with a given node
name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

appendChild

​(

Node

newChild)

Adds the node

newChild

to the end of the list of
children of this node.

Node

cloneNode

​(boolean deep)

Returns a duplicate of this node.

short

compareDocumentPosition

​(

Node

other)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

String

getAttribute

​(

String

name)

Retrieves an attribute value by name.

Attr

getAttributeNodeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

getAttributeNode(localName)

.

String

getAttributeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

getAttribute(localName)

.

NamedNodeMap

getAttributes

()

Returns a

NamedNodeMap

containing the attributes of
this node.

String

getBaseURI

()

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

NodeList

getChildNodes

()

Returns a

NodeList

that contains all children of this node.

NodeList

getElementsByTagNameNS

​(

String

namespaceURI,

String

localName)

Equivalent to

getElementsByTagName(localName)

.

Object

getFeature

​(

String

feature,

String

version)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Node

getFirstChild

()

Returns the first child of this node, or

null

if
the node has no children.

Node

getLastChild

()

Returns the last child of this node, or

null

if
the node has no children.

String

getLocalName

()

Equivalent to

getNodeName

.

String

getNamespaceURI

()

Returns

null

, since namespaces are not supported.

Node

getNextSibling

()

Returns the next sibling of this node, or

null

if
the node has no next sibling.

String

getNodeName

()

Returns the node name associated with this node.

short

getNodeType

()

Returns the node type, which is always

ELEMENT_NODE

.

String

getNodeValue

()

Returns the value associated with this node.

Document

getOwnerDocument

()

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

Node

getParentNode

()

Returns the parent of this node.

String

getPrefix

()

Returns

null

, since namespaces are not supported.

Node

getPreviousSibling

()

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

TypeInfo

getSchemaTypeInfo

()

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

String

getTagName

()

Equivalent to

getNodeName

.

String

getTextContent

()

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Object

getUserData

​(

String

key)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Object

getUserObject

()

Returns the

Object

value associated with this node.

boolean

hasAttributeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

hasAttribute(localName)

.

boolean

hasChildNodes

()

Returns

true

if this node has child nodes.

Node

insertBefore

​(

Node

newChild,

Node

refChild)

Inserts the node

newChild

before the existing
child node

refChild

.

boolean

isDefaultNamespace

​(

String

namespaceURI)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

boolean

isEqualNode

​(

Node

node)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

boolean

isSameNode

​(

Node

node)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

boolean

isSupported

​(

String

feature,

String

version)

Returns

false

since DOM features are not
supported.

String

lookupNamespaceURI

​(

String

prefix)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

String

lookupPrefix

​(

String

namespaceURI)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

normalize

()

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

void

removeAttributeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

removeAttribute(localName)

.

Node

removeChild

​(

Node

oldChild)

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

Node

replaceChild

​(

Node

newChild,

Node

oldChild)

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

Attr

setAttributeNodeNS

​(

Attr

newAttr)

Equivalent to

setAttributeNode(newAttr)

.

void

setAttributeNS

​(

String

namespaceURI,

String

qualifiedName,

String

value)

Equivalent to

setAttribute(qualifiedName, value)

.

void

setIdAttribute

​(

String

name,
boolean isId)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setIdAttributeNode

​(

Attr

idAttr,
boolean isId)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setIdAttributeNS

​(

String

namespaceURI,

String

localName,
boolean isId)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setNodeValue

​(

String

nodeValue)

Sets the

String

value associated with this node.

void

setPrefix

​(

String

prefix)

Does nothing, since namespaces are not supported.

void

setTextContent

​(

String

textContent)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Object

setUserData

​(

String

key,

Object

data,

UserDataHandler

handler)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setUserObject

​(

Object

userObject)

Sets the value associated with this node.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface org.w3c.dom.

Element

getAttributeNode

,

getElementsByTagName

,

hasAttribute

,

removeAttribute

,

removeAttributeNode

,

setAttribute

,

setAttributeNode

- Methods declared in interface org.w3c.dom.

Node

hasAttributes

- Methods declared in interface org.w3c.dom.

NodeList

getLength

,

item

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

Constructor Summary

Constructors

Constructor

Description

IIOMetadataNode

()

Constructs an empty

IIOMetadataNode

.

IIOMetadataNode

​(

String

nodeName)

Constructs an

IIOMetadataNode

with a given node
name.

---

#### Constructor Summary

Constructs an empty

IIOMetadataNode

.

Constructs an

IIOMetadataNode

with a given node
name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Node

appendChild

​(

Node

newChild)

Adds the node

newChild

to the end of the list of
children of this node.

Node

cloneNode

​(boolean deep)

Returns a duplicate of this node.

short

compareDocumentPosition

​(

Node

other)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

String

getAttribute

​(

String

name)

Retrieves an attribute value by name.

Attr

getAttributeNodeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

getAttributeNode(localName)

.

String

getAttributeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

getAttribute(localName)

.

NamedNodeMap

getAttributes

()

Returns a

NamedNodeMap

containing the attributes of
this node.

String

getBaseURI

()

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

NodeList

getChildNodes

()

Returns a

NodeList

that contains all children of this node.

NodeList

getElementsByTagNameNS

​(

String

namespaceURI,

String

localName)

Equivalent to

getElementsByTagName(localName)

.

Object

getFeature

​(

String

feature,

String

version)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Node

getFirstChild

()

Returns the first child of this node, or

null

if
the node has no children.

Node

getLastChild

()

Returns the last child of this node, or

null

if
the node has no children.

String

getLocalName

()

Equivalent to

getNodeName

.

String

getNamespaceURI

()

Returns

null

, since namespaces are not supported.

Node

getNextSibling

()

Returns the next sibling of this node, or

null

if
the node has no next sibling.

String

getNodeName

()

Returns the node name associated with this node.

short

getNodeType

()

Returns the node type, which is always

ELEMENT_NODE

.

String

getNodeValue

()

Returns the value associated with this node.

Document

getOwnerDocument

()

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

Node

getParentNode

()

Returns the parent of this node.

String

getPrefix

()

Returns

null

, since namespaces are not supported.

Node

getPreviousSibling

()

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

TypeInfo

getSchemaTypeInfo

()

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

String

getTagName

()

Equivalent to

getNodeName

.

String

getTextContent

()

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Object

getUserData

​(

String

key)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Object

getUserObject

()

Returns the

Object

value associated with this node.

boolean

hasAttributeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

hasAttribute(localName)

.

boolean

hasChildNodes

()

Returns

true

if this node has child nodes.

Node

insertBefore

​(

Node

newChild,

Node

refChild)

Inserts the node

newChild

before the existing
child node

refChild

.

boolean

isDefaultNamespace

​(

String

namespaceURI)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

boolean

isEqualNode

​(

Node

node)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

boolean

isSameNode

​(

Node

node)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

boolean

isSupported

​(

String

feature,

String

version)

Returns

false

since DOM features are not
supported.

String

lookupNamespaceURI

​(

String

prefix)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

String

lookupPrefix

​(

String

namespaceURI)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

normalize

()

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

void

removeAttributeNS

​(

String

namespaceURI,

String

localName)

Equivalent to

removeAttribute(localName)

.

Node

removeChild

​(

Node

oldChild)

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

Node

replaceChild

​(

Node

newChild,

Node

oldChild)

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

Attr

setAttributeNodeNS

​(

Attr

newAttr)

Equivalent to

setAttributeNode(newAttr)

.

void

setAttributeNS

​(

String

namespaceURI,

String

qualifiedName,

String

value)

Equivalent to

setAttribute(qualifiedName, value)

.

void

setIdAttribute

​(

String

name,
boolean isId)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setIdAttributeNode

​(

Attr

idAttr,
boolean isId)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setIdAttributeNS

​(

String

namespaceURI,

String

localName,
boolean isId)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setNodeValue

​(

String

nodeValue)

Sets the

String

value associated with this node.

void

setPrefix

​(

String

prefix)

Does nothing, since namespaces are not supported.

void

setTextContent

​(

String

textContent)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Object

setUserData

​(

String

key,

Object

data,

UserDataHandler

handler)

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

void

setUserObject

​(

Object

userObject)

Sets the value associated with this node.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

- Methods declared in interface org.w3c.dom.

Element

getAttributeNode

,

getElementsByTagName

,

hasAttribute

,

removeAttribute

,

removeAttributeNode

,

setAttribute

,

setAttributeNode

- Methods declared in interface org.w3c.dom.

Node

hasAttributes

- Methods declared in interface org.w3c.dom.

NodeList

getLength

,

item

---

#### Method Summary

Adds the node

newChild

to the end of the list of
children of this node.

Returns a duplicate of this node.

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

Retrieves an attribute value by name.

Equivalent to

getAttributeNode(localName)

.

Equivalent to

getAttribute(localName)

.

Returns a

NamedNodeMap

containing the attributes of
this node.

Returns a

NodeList

that contains all children of this node.

Equivalent to

getElementsByTagName(localName)

.

Returns the first child of this node, or

null

if
the node has no children.

Returns the last child of this node, or

null

if
the node has no children.

Equivalent to

getNodeName

.

Returns

null

, since namespaces are not supported.

Returns the next sibling of this node, or

null

if
the node has no next sibling.

Returns the node name associated with this node.

Returns the node type, which is always

ELEMENT_NODE

.

Returns the value associated with this node.

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

Returns the parent of this node.

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

Returns the

Object

value associated with this node.

Equivalent to

hasAttribute(localName)

.

Returns

true

if this node has child nodes.

Inserts the node

newChild

before the existing
child node

refChild

.

Returns

false

since DOM features are not
supported.

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

Equivalent to

removeAttribute(localName)

.

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

Equivalent to

setAttributeNode(newAttr)

.

Equivalent to

setAttribute(qualifiedName, value)

.

Sets the

String

value associated with this node.

Does nothing, since namespaces are not supported.

Sets the value associated with this node.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface org.w3c.dom.

Element

getAttributeNode

,

getElementsByTagName

,

hasAttribute

,

removeAttribute

,

removeAttributeNode

,

setAttribute

,

setAttributeNode

---

#### Methods declared in interface org.w3c.dom. Element

Methods declared in interface org.w3c.dom.

Node

hasAttributes

---

#### Methods declared in interface org.w3c.dom. Node

Methods declared in interface org.w3c.dom.

NodeList

getLength

,

item

---

#### Methods declared in interface org.w3c.dom. NodeList

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- IIOMetadataNode

```java
public IIOMetadataNode()
```

Constructs an empty

IIOMetadataNode

.

- IIOMetadataNode

```java
public IIOMetadataNode​(
String
nodeName)
```

Constructs an

IIOMetadataNode

with a given node
name.

**Parameters:** nodeName

- the name of the node, as a

String

.

============ METHOD DETAIL ==========

- Method Detail

- getNodeName

```java
public
String
getNodeName()
```

Returns the node name associated with this node.

**Specified by:** getNodeName

in interface

Node
**Returns:** the node name, as a

String

.

- getNodeValue

```java
public
String
getNodeValue()
```

Returns the value associated with this node.

**Specified by:** getNodeValue

in interface

Node
**Returns:** the node value, as a

String

.

- setNodeValue

```java
public void setNodeValue​(
String
nodeValue)
```

Sets the

String

value associated with this node.

**Specified by:** setNodeValue

in interface

Node

- getNodeType

```java
public short getNodeType()
```

Returns the node type, which is always

ELEMENT_NODE

.

**Specified by:** getNodeType

in interface

Node
**Returns:** the

short

value

ELEMENT_NODE

.

- getParentNode

```java
public
Node
getParentNode()
```

Returns the parent of this node. A

null

value
indicates that the node is the root of its own tree. To add a
node to an existing tree, use one of the

insertBefore

,

replaceChild

, or

appendChild

methods.

**Specified by:** getParentNode

in interface

Node
**Returns:** the parent, as a

Node

.
**See Also:** insertBefore(org.w3c.dom.Node, org.w3c.dom.Node)

,

replaceChild(org.w3c.dom.Node, org.w3c.dom.Node)

,

appendChild(org.w3c.dom.Node)

- getChildNodes

```java
public
NodeList
getChildNodes()
```

Returns a

NodeList

that contains all children of this node.
If there are no children, this is a

NodeList

containing
no nodes.

**Specified by:** getChildNodes

in interface

Node
**Returns:** the children as a

NodeList

- getFirstChild

```java
public
Node
getFirstChild()
```

Returns the first child of this node, or

null

if
the node has no children.

**Specified by:** getFirstChild

in interface

Node
**Returns:** the first child, as a

Node

, or

null

- getLastChild

```java
public
Node
getLastChild()
```

Returns the last child of this node, or

null

if
the node has no children.

**Specified by:** getLastChild

in interface

Node
**Returns:** the last child, as a

Node

, or

null

.

- getPreviousSibling

```java
public
Node
getPreviousSibling()
```

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

**Specified by:** getPreviousSibling

in interface

Node
**Returns:** the previous sibling, as a

Node

, or

null

.

- getNextSibling

```java
public
Node
getNextSibling()
```

Returns the next sibling of this node, or

null

if
the node has no next sibling.

**Specified by:** getNextSibling

in interface

Node
**Returns:** the next sibling, as a

Node

, or

null

.

- getAttributes

```java
public
NamedNodeMap
getAttributes()
```

Returns a

NamedNodeMap

containing the attributes of
this node.

**Specified by:** getAttributes

in interface

Node
**Returns:** a

NamedNodeMap

containing the attributes of
this node.

- getOwnerDocument

```java
public
Document
getOwnerDocument()
```

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

**Specified by:** getOwnerDocument

in interface

Node
**Returns:** null

.

- insertBefore

```java
public
Node
insertBefore​(
Node
newChild,

Node
refChild)
```

Inserts the node

newChild

before the existing
child node

refChild

. If

refChild

is

null

, insert

newChild

at the end of
the list of children.

**Specified by:** insertBefore

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Parameters:** refChild

- the reference

Node

.
**Returns:** the node being inserted.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

- replaceChild

```java
public
Node
replaceChild​(
Node
newChild,

Node
oldChild)
```

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

**Specified by:** replaceChild

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Parameters:** oldChild

- the

Node

to be replaced.
**Returns:** the node replaced.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

- removeChild

```java
public
Node
removeChild​(
Node
oldChild)
```

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

**Specified by:** removeChild

in interface

Node
**Parameters:** oldChild

- the

Node

to be removed.
**Returns:** the node removed.
**Throws:** IllegalArgumentException

- if

oldChild

is

null

.

- appendChild

```java
public
Node
appendChild​(
Node
newChild)
```

Adds the node

newChild

to the end of the list of
children of this node.

**Specified by:** appendChild

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Returns:** the node added.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

- hasChildNodes

```java
public boolean hasChildNodes()
```

Returns

true

if this node has child nodes.

**Specified by:** hasChildNodes

in interface

Node
**Returns:** true

if this node has children.

- cloneNode

```java
public
Node
cloneNode​(boolean deep)
```

Returns a duplicate of this node. The duplicate node has no
parent (

getParentNode

returns

null

).
If a shallow clone is being performed (

deep

is

false

), the new node will not have any children or
siblings. If a deep clone is being performed, the new node
will form the root of a complete cloned subtree.

**Specified by:** cloneNode

in interface

Node
**Parameters:** deep

- if

true

, recursively clone the subtree
under the specified node; if

false

, clone only the
node itself.
**Returns:** the duplicate node.

- normalize

```java
public void normalize()
```

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

**Specified by:** normalize

in interface

Node

- isSupported

```java
public boolean isSupported​(
String
feature,

String
version)
```

Returns

false

since DOM features are not
supported.

**Specified by:** isSupported

in interface

Node
**Parameters:** feature

- a

String

, which is ignored.
**Parameters:** version

- a

String

, which is ignored.
**Returns:** false

.

- getNamespaceURI

```java
public
String
getNamespaceURI()
throws
DOMException
```

Returns

null

, since namespaces are not supported.

**Specified by:** getNamespaceURI

in interface

Node
**Throws:** DOMException

- getPrefix

```java
public
String
getPrefix()
```

Returns

null

, since namespaces are not supported.

**Specified by:** getPrefix

in interface

Node
**Returns:** null

.
**See Also:** setPrefix(java.lang.String)

- setPrefix

```java
public void setPrefix​(
String
prefix)
```

Does nothing, since namespaces are not supported.

**Specified by:** setPrefix

in interface

Node
**Parameters:** prefix

- a

String

, which is ignored.
**See Also:** getPrefix()

- getLocalName

```java
public
String
getLocalName()
```

Equivalent to

getNodeName

.

**Specified by:** getLocalName

in interface

Node
**Returns:** the node name, as a

String

.

- getTagName

```java
public
String
getTagName()
```

Equivalent to

getNodeName

.

**Specified by:** getTagName

in interface

Element
**Returns:** the node name, as a

String

- getAttribute

```java
public
String
getAttribute​(
String
name)
```

Retrieves an attribute value by name.

**Specified by:** getAttribute

in interface

Element
**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.

- getAttributeNS

```java
public
String
getAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getAttribute(localName)

.

**Specified by:** getAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to retrieve.
**Parameters:** localName

- The local name of the attribute to retrieve.
**Returns:** The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.
**See Also:** setAttributeNS(java.lang.String, java.lang.String, java.lang.String)

- setAttributeNS

```java
public void setAttributeNS​(
String
namespaceURI,

String
qualifiedName,

String
value)
```

Equivalent to

setAttribute(qualifiedName, value)

.

**Specified by:** setAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to create or
alter.
**Parameters:** qualifiedName

- The qualified name of the attribute to create or
alter.
**Parameters:** value

- The value to set in string form.
**See Also:** getAttributeNS(java.lang.String, java.lang.String)

- removeAttributeNS

```java
public void removeAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

removeAttribute(localName)

.

**Specified by:** removeAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to remove.
**Parameters:** localName

- The local name of the attribute to remove.

- getAttributeNodeNS

```java
public
Attr
getAttributeNodeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getAttributeNode(localName)

.

**Specified by:** getAttributeNodeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to retrieve.
**Parameters:** localName

- The local name of the attribute to retrieve.
**Returns:** The

Attr

node with the specified attribute local
name and namespace URI or

null

if there is no such
attribute.
**See Also:** setAttributeNodeNS(org.w3c.dom.Attr)

- setAttributeNodeNS

```java
public
Attr
setAttributeNodeNS​(
Attr
newAttr)
```

Equivalent to

setAttributeNode(newAttr)

.

**Specified by:** setAttributeNodeNS

in interface

Element
**Parameters:** newAttr

- The

Attr

node to add to the attribute list.
**Returns:** If the

newAttr

attribute replaces an existing
attribute with the same local name and namespace URI, the replaced

Attr

node is returned, otherwise

null

is
returned.
**See Also:** getAttributeNodeNS(java.lang.String, java.lang.String)

- getElementsByTagNameNS

```java
public
NodeList
getElementsByTagNameNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getElementsByTagName(localName)

.

**Specified by:** getElementsByTagNameNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the elements to match on. The
special value "*" matches all namespaces.
**Parameters:** localName

- The local name of the elements to match on. The
special value "*" matches all local names.
**Returns:** A new

NodeList

object containing all the matched

Elements

.

- hasAttributeNS

```java
public boolean hasAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

hasAttribute(localName)

.

**Specified by:** hasAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to look for.
**Parameters:** localName

- The local name of the attribute to look for.
**Returns:** true

if an attribute with the given local name
and namespace URI is specified or has a default value on this
element,

false

otherwise.

- getUserObject

```java
public
Object
getUserObject()
```

Returns the

Object

value associated with this node.

**Returns:** the user

Object

.
**See Also:** setUserObject(java.lang.Object)

- setUserObject

```java
public void setUserObject​(
Object
userObject)
```

Sets the value associated with this node.

**Parameters:** userObject

- the user

Object

.
**See Also:** getUserObject()

- setIdAttribute

```java
public void setIdAttribute​(
String
name,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttribute

in interface

Element
**Parameters:** name

- The name of the attribute.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

- setIdAttributeNS

```java
public void setIdAttributeNS​(
String
namespaceURI,

String
localName,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute.
**Parameters:** localName

- The local name of the attribute.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

- setIdAttributeNode

```java
public void setIdAttributeNode​(
Attr
idAttr,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttributeNode

in interface

Element
**Parameters:** idAttr

- The attribute node.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

- getSchemaTypeInfo

```java
public
TypeInfo
getSchemaTypeInfo()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getSchemaTypeInfo

in interface

Element
**Throws:** DOMException

- always.

- setUserData

```java
public
Object
setUserData​(
String
key,

Object
data,

UserDataHandler
handler)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setUserData

in interface

Node
**Parameters:** key

- The key to associate the object to.
**Parameters:** data

- The object to associate to the given key, or

null

to remove any existing association to that key.
**Parameters:** handler

- The handler to associate to that key, or

null

.
**Returns:** Returns the

DOMUserData

previously associated to
the given key on this node, or

null

if there was none.
**Throws:** DOMException

- always.

- getUserData

```java
public
Object
getUserData​(
String
key)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getUserData

in interface

Node
**Parameters:** key

- The key the object is associated to.
**Returns:** Returns the

DOMUserData

associated to the given
key on this node, or

null

if there was none.
**Throws:** DOMException

- always.

- getFeature

```java
public
Object
getFeature​(
String
feature,

String
version)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getFeature

in interface

Node
**Parameters:** feature

- The name of the feature requested. Note that any plus
sign "+" prepended to the name of the feature will be ignored since
it is not significant in the context of this method.
**Parameters:** version

- This is the version number of the feature to test.
**Returns:** Returns an object which implements the specialized APIs of
the specified feature and version, if any, or

null

if
there is no object which implements interfaces associated with that
feature. If the

DOMObject

returned by this method
implements the

Node

interface, it must delegate to the
primary core

Node

and not return results inconsistent
with the primary core

Node

such as attributes,
childNodes, etc.
**Throws:** DOMException

- always.

- isSameNode

```java
public boolean isSameNode​(
Node
node)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isSameNode

in interface

Node
**Parameters:** node

- The node to test against.
**Returns:** Returns

true

if the nodes are the same,

false

otherwise.
**Throws:** DOMException

- always.

- isEqualNode

```java
public boolean isEqualNode​(
Node
node)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isEqualNode

in interface

Node
**Parameters:** node

- The node to compare equality with.
**Returns:** Returns

true

if the nodes are equal,

false

otherwise.
**Throws:** DOMException

- always.

- lookupNamespaceURI

```java
public
String
lookupNamespaceURI​(
String
prefix)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** lookupNamespaceURI

in interface

Node
**Parameters:** prefix

- The prefix to look for. If this parameter is

null

, the method will return the default namespace URI
if any.
**Returns:** Returns the associated namespace URI or

null

if
none is found.
**Throws:** DOMException

- always.

- isDefaultNamespace

```java
public boolean isDefaultNamespace​(
String
namespaceURI)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isDefaultNamespace

in interface

Node
**Parameters:** namespaceURI

- The namespace URI to look for.
**Returns:** Returns

true

if the specified

namespaceURI

is the default namespace,

false

otherwise.
**Throws:** DOMException

- always.

- lookupPrefix

```java
public
String
lookupPrefix​(
String
namespaceURI)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** lookupPrefix

in interface

Node
**Parameters:** namespaceURI

- The namespace URI to look for.
**Returns:** Returns an associated namespace prefix if found or

null

if none is found. If more than one prefix are
associated to the namespace prefix, the returned namespace prefix
is implementation dependent.
**Throws:** DOMException

- always.

- getTextContent

```java
public
String
getTextContent()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getTextContent

in interface

Node
**Throws:** DOMException

- always.

- setTextContent

```java
public void setTextContent​(
String
textContent)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setTextContent

in interface

Node
**Throws:** DOMException

- always.

- compareDocumentPosition

```java
public short compareDocumentPosition​(
Node
other)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** compareDocumentPosition

in interface

Node
**Parameters:** other

- The node to compare against the reference node.
**Returns:** Returns how the node is positioned relatively to the reference
node.
**Throws:** DOMException

- always.

- getBaseURI

```java
public
String
getBaseURI()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getBaseURI

in interface

Node
**Throws:** DOMException

- always.

Constructor Detail

- IIOMetadataNode

```java
public IIOMetadataNode()
```

Constructs an empty

IIOMetadataNode

.

- IIOMetadataNode

```java
public IIOMetadataNode​(
String
nodeName)
```

Constructs an

IIOMetadataNode

with a given node
name.

**Parameters:** nodeName

- the name of the node, as a

String

.

---

#### Constructor Detail

IIOMetadataNode

```java
public IIOMetadataNode()
```

Constructs an empty

IIOMetadataNode

.

---

#### IIOMetadataNode

public IIOMetadataNode()

Constructs an empty

IIOMetadataNode

.

IIOMetadataNode

```java
public IIOMetadataNode​(
String
nodeName)
```

Constructs an

IIOMetadataNode

with a given node
name.

**Parameters:** nodeName

- the name of the node, as a

String

.

---

#### IIOMetadataNode

public IIOMetadataNode​(

String

nodeName)

Constructs an

IIOMetadataNode

with a given node
name.

Method Detail

- getNodeName

```java
public
String
getNodeName()
```

Returns the node name associated with this node.

**Specified by:** getNodeName

in interface

Node
**Returns:** the node name, as a

String

.

- getNodeValue

```java
public
String
getNodeValue()
```

Returns the value associated with this node.

**Specified by:** getNodeValue

in interface

Node
**Returns:** the node value, as a

String

.

- setNodeValue

```java
public void setNodeValue​(
String
nodeValue)
```

Sets the

String

value associated with this node.

**Specified by:** setNodeValue

in interface

Node

- getNodeType

```java
public short getNodeType()
```

Returns the node type, which is always

ELEMENT_NODE

.

**Specified by:** getNodeType

in interface

Node
**Returns:** the

short

value

ELEMENT_NODE

.

- getParentNode

```java
public
Node
getParentNode()
```

Returns the parent of this node. A

null

value
indicates that the node is the root of its own tree. To add a
node to an existing tree, use one of the

insertBefore

,

replaceChild

, or

appendChild

methods.

**Specified by:** getParentNode

in interface

Node
**Returns:** the parent, as a

Node

.
**See Also:** insertBefore(org.w3c.dom.Node, org.w3c.dom.Node)

,

replaceChild(org.w3c.dom.Node, org.w3c.dom.Node)

,

appendChild(org.w3c.dom.Node)

- getChildNodes

```java
public
NodeList
getChildNodes()
```

Returns a

NodeList

that contains all children of this node.
If there are no children, this is a

NodeList

containing
no nodes.

**Specified by:** getChildNodes

in interface

Node
**Returns:** the children as a

NodeList

- getFirstChild

```java
public
Node
getFirstChild()
```

Returns the first child of this node, or

null

if
the node has no children.

**Specified by:** getFirstChild

in interface

Node
**Returns:** the first child, as a

Node

, or

null

- getLastChild

```java
public
Node
getLastChild()
```

Returns the last child of this node, or

null

if
the node has no children.

**Specified by:** getLastChild

in interface

Node
**Returns:** the last child, as a

Node

, or

null

.

- getPreviousSibling

```java
public
Node
getPreviousSibling()
```

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

**Specified by:** getPreviousSibling

in interface

Node
**Returns:** the previous sibling, as a

Node

, or

null

.

- getNextSibling

```java
public
Node
getNextSibling()
```

Returns the next sibling of this node, or

null

if
the node has no next sibling.

**Specified by:** getNextSibling

in interface

Node
**Returns:** the next sibling, as a

Node

, or

null

.

- getAttributes

```java
public
NamedNodeMap
getAttributes()
```

Returns a

NamedNodeMap

containing the attributes of
this node.

**Specified by:** getAttributes

in interface

Node
**Returns:** a

NamedNodeMap

containing the attributes of
this node.

- getOwnerDocument

```java
public
Document
getOwnerDocument()
```

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

**Specified by:** getOwnerDocument

in interface

Node
**Returns:** null

.

- insertBefore

```java
public
Node
insertBefore​(
Node
newChild,

Node
refChild)
```

Inserts the node

newChild

before the existing
child node

refChild

. If

refChild

is

null

, insert

newChild

at the end of
the list of children.

**Specified by:** insertBefore

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Parameters:** refChild

- the reference

Node

.
**Returns:** the node being inserted.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

- replaceChild

```java
public
Node
replaceChild​(
Node
newChild,

Node
oldChild)
```

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

**Specified by:** replaceChild

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Parameters:** oldChild

- the

Node

to be replaced.
**Returns:** the node replaced.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

- removeChild

```java
public
Node
removeChild​(
Node
oldChild)
```

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

**Specified by:** removeChild

in interface

Node
**Parameters:** oldChild

- the

Node

to be removed.
**Returns:** the node removed.
**Throws:** IllegalArgumentException

- if

oldChild

is

null

.

- appendChild

```java
public
Node
appendChild​(
Node
newChild)
```

Adds the node

newChild

to the end of the list of
children of this node.

**Specified by:** appendChild

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Returns:** the node added.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

- hasChildNodes

```java
public boolean hasChildNodes()
```

Returns

true

if this node has child nodes.

**Specified by:** hasChildNodes

in interface

Node
**Returns:** true

if this node has children.

- cloneNode

```java
public
Node
cloneNode​(boolean deep)
```

Returns a duplicate of this node. The duplicate node has no
parent (

getParentNode

returns

null

).
If a shallow clone is being performed (

deep

is

false

), the new node will not have any children or
siblings. If a deep clone is being performed, the new node
will form the root of a complete cloned subtree.

**Specified by:** cloneNode

in interface

Node
**Parameters:** deep

- if

true

, recursively clone the subtree
under the specified node; if

false

, clone only the
node itself.
**Returns:** the duplicate node.

- normalize

```java
public void normalize()
```

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

**Specified by:** normalize

in interface

Node

- isSupported

```java
public boolean isSupported​(
String
feature,

String
version)
```

Returns

false

since DOM features are not
supported.

**Specified by:** isSupported

in interface

Node
**Parameters:** feature

- a

String

, which is ignored.
**Parameters:** version

- a

String

, which is ignored.
**Returns:** false

.

- getNamespaceURI

```java
public
String
getNamespaceURI()
throws
DOMException
```

Returns

null

, since namespaces are not supported.

**Specified by:** getNamespaceURI

in interface

Node
**Throws:** DOMException

- getPrefix

```java
public
String
getPrefix()
```

Returns

null

, since namespaces are not supported.

**Specified by:** getPrefix

in interface

Node
**Returns:** null

.
**See Also:** setPrefix(java.lang.String)

- setPrefix

```java
public void setPrefix​(
String
prefix)
```

Does nothing, since namespaces are not supported.

**Specified by:** setPrefix

in interface

Node
**Parameters:** prefix

- a

String

, which is ignored.
**See Also:** getPrefix()

- getLocalName

```java
public
String
getLocalName()
```

Equivalent to

getNodeName

.

**Specified by:** getLocalName

in interface

Node
**Returns:** the node name, as a

String

.

- getTagName

```java
public
String
getTagName()
```

Equivalent to

getNodeName

.

**Specified by:** getTagName

in interface

Element
**Returns:** the node name, as a

String

- getAttribute

```java
public
String
getAttribute​(
String
name)
```

Retrieves an attribute value by name.

**Specified by:** getAttribute

in interface

Element
**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.

- getAttributeNS

```java
public
String
getAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getAttribute(localName)

.

**Specified by:** getAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to retrieve.
**Parameters:** localName

- The local name of the attribute to retrieve.
**Returns:** The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.
**See Also:** setAttributeNS(java.lang.String, java.lang.String, java.lang.String)

- setAttributeNS

```java
public void setAttributeNS​(
String
namespaceURI,

String
qualifiedName,

String
value)
```

Equivalent to

setAttribute(qualifiedName, value)

.

**Specified by:** setAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to create or
alter.
**Parameters:** qualifiedName

- The qualified name of the attribute to create or
alter.
**Parameters:** value

- The value to set in string form.
**See Also:** getAttributeNS(java.lang.String, java.lang.String)

- removeAttributeNS

```java
public void removeAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

removeAttribute(localName)

.

**Specified by:** removeAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to remove.
**Parameters:** localName

- The local name of the attribute to remove.

- getAttributeNodeNS

```java
public
Attr
getAttributeNodeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getAttributeNode(localName)

.

**Specified by:** getAttributeNodeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to retrieve.
**Parameters:** localName

- The local name of the attribute to retrieve.
**Returns:** The

Attr

node with the specified attribute local
name and namespace URI or

null

if there is no such
attribute.
**See Also:** setAttributeNodeNS(org.w3c.dom.Attr)

- setAttributeNodeNS

```java
public
Attr
setAttributeNodeNS​(
Attr
newAttr)
```

Equivalent to

setAttributeNode(newAttr)

.

**Specified by:** setAttributeNodeNS

in interface

Element
**Parameters:** newAttr

- The

Attr

node to add to the attribute list.
**Returns:** If the

newAttr

attribute replaces an existing
attribute with the same local name and namespace URI, the replaced

Attr

node is returned, otherwise

null

is
returned.
**See Also:** getAttributeNodeNS(java.lang.String, java.lang.String)

- getElementsByTagNameNS

```java
public
NodeList
getElementsByTagNameNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getElementsByTagName(localName)

.

**Specified by:** getElementsByTagNameNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the elements to match on. The
special value "*" matches all namespaces.
**Parameters:** localName

- The local name of the elements to match on. The
special value "*" matches all local names.
**Returns:** A new

NodeList

object containing all the matched

Elements

.

- hasAttributeNS

```java
public boolean hasAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

hasAttribute(localName)

.

**Specified by:** hasAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to look for.
**Parameters:** localName

- The local name of the attribute to look for.
**Returns:** true

if an attribute with the given local name
and namespace URI is specified or has a default value on this
element,

false

otherwise.

- getUserObject

```java
public
Object
getUserObject()
```

Returns the

Object

value associated with this node.

**Returns:** the user

Object

.
**See Also:** setUserObject(java.lang.Object)

- setUserObject

```java
public void setUserObject​(
Object
userObject)
```

Sets the value associated with this node.

**Parameters:** userObject

- the user

Object

.
**See Also:** getUserObject()

- setIdAttribute

```java
public void setIdAttribute​(
String
name,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttribute

in interface

Element
**Parameters:** name

- The name of the attribute.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

- setIdAttributeNS

```java
public void setIdAttributeNS​(
String
namespaceURI,

String
localName,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute.
**Parameters:** localName

- The local name of the attribute.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

- setIdAttributeNode

```java
public void setIdAttributeNode​(
Attr
idAttr,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttributeNode

in interface

Element
**Parameters:** idAttr

- The attribute node.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

- getSchemaTypeInfo

```java
public
TypeInfo
getSchemaTypeInfo()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getSchemaTypeInfo

in interface

Element
**Throws:** DOMException

- always.

- setUserData

```java
public
Object
setUserData​(
String
key,

Object
data,

UserDataHandler
handler)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setUserData

in interface

Node
**Parameters:** key

- The key to associate the object to.
**Parameters:** data

- The object to associate to the given key, or

null

to remove any existing association to that key.
**Parameters:** handler

- The handler to associate to that key, or

null

.
**Returns:** Returns the

DOMUserData

previously associated to
the given key on this node, or

null

if there was none.
**Throws:** DOMException

- always.

- getUserData

```java
public
Object
getUserData​(
String
key)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getUserData

in interface

Node
**Parameters:** key

- The key the object is associated to.
**Returns:** Returns the

DOMUserData

associated to the given
key on this node, or

null

if there was none.
**Throws:** DOMException

- always.

- getFeature

```java
public
Object
getFeature​(
String
feature,

String
version)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getFeature

in interface

Node
**Parameters:** feature

- The name of the feature requested. Note that any plus
sign "+" prepended to the name of the feature will be ignored since
it is not significant in the context of this method.
**Parameters:** version

- This is the version number of the feature to test.
**Returns:** Returns an object which implements the specialized APIs of
the specified feature and version, if any, or

null

if
there is no object which implements interfaces associated with that
feature. If the

DOMObject

returned by this method
implements the

Node

interface, it must delegate to the
primary core

Node

and not return results inconsistent
with the primary core

Node

such as attributes,
childNodes, etc.
**Throws:** DOMException

- always.

- isSameNode

```java
public boolean isSameNode​(
Node
node)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isSameNode

in interface

Node
**Parameters:** node

- The node to test against.
**Returns:** Returns

true

if the nodes are the same,

false

otherwise.
**Throws:** DOMException

- always.

- isEqualNode

```java
public boolean isEqualNode​(
Node
node)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isEqualNode

in interface

Node
**Parameters:** node

- The node to compare equality with.
**Returns:** Returns

true

if the nodes are equal,

false

otherwise.
**Throws:** DOMException

- always.

- lookupNamespaceURI

```java
public
String
lookupNamespaceURI​(
String
prefix)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** lookupNamespaceURI

in interface

Node
**Parameters:** prefix

- The prefix to look for. If this parameter is

null

, the method will return the default namespace URI
if any.
**Returns:** Returns the associated namespace URI or

null

if
none is found.
**Throws:** DOMException

- always.

- isDefaultNamespace

```java
public boolean isDefaultNamespace​(
String
namespaceURI)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isDefaultNamespace

in interface

Node
**Parameters:** namespaceURI

- The namespace URI to look for.
**Returns:** Returns

true

if the specified

namespaceURI

is the default namespace,

false

otherwise.
**Throws:** DOMException

- always.

- lookupPrefix

```java
public
String
lookupPrefix​(
String
namespaceURI)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** lookupPrefix

in interface

Node
**Parameters:** namespaceURI

- The namespace URI to look for.
**Returns:** Returns an associated namespace prefix if found or

null

if none is found. If more than one prefix are
associated to the namespace prefix, the returned namespace prefix
is implementation dependent.
**Throws:** DOMException

- always.

- getTextContent

```java
public
String
getTextContent()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getTextContent

in interface

Node
**Throws:** DOMException

- always.

- setTextContent

```java
public void setTextContent​(
String
textContent)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setTextContent

in interface

Node
**Throws:** DOMException

- always.

- compareDocumentPosition

```java
public short compareDocumentPosition​(
Node
other)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** compareDocumentPosition

in interface

Node
**Parameters:** other

- The node to compare against the reference node.
**Returns:** Returns how the node is positioned relatively to the reference
node.
**Throws:** DOMException

- always.

- getBaseURI

```java
public
String
getBaseURI()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getBaseURI

in interface

Node
**Throws:** DOMException

- always.

---

#### Method Detail

getNodeName

```java
public
String
getNodeName()
```

Returns the node name associated with this node.

**Specified by:** getNodeName

in interface

Node
**Returns:** the node name, as a

String

.

---

#### getNodeName

public

String

getNodeName()

Returns the node name associated with this node.

getNodeValue

```java
public
String
getNodeValue()
```

Returns the value associated with this node.

**Specified by:** getNodeValue

in interface

Node
**Returns:** the node value, as a

String

.

---

#### getNodeValue

public

String

getNodeValue()

Returns the value associated with this node.

setNodeValue

```java
public void setNodeValue​(
String
nodeValue)
```

Sets the

String

value associated with this node.

**Specified by:** setNodeValue

in interface

Node

---

#### setNodeValue

public void setNodeValue​(

String

nodeValue)

Sets the

String

value associated with this node.

getNodeType

```java
public short getNodeType()
```

Returns the node type, which is always

ELEMENT_NODE

.

**Specified by:** getNodeType

in interface

Node
**Returns:** the

short

value

ELEMENT_NODE

.

---

#### getNodeType

public short getNodeType()

Returns the node type, which is always

ELEMENT_NODE

.

getParentNode

```java
public
Node
getParentNode()
```

Returns the parent of this node. A

null

value
indicates that the node is the root of its own tree. To add a
node to an existing tree, use one of the

insertBefore

,

replaceChild

, or

appendChild

methods.

**Specified by:** getParentNode

in interface

Node
**Returns:** the parent, as a

Node

.
**See Also:** insertBefore(org.w3c.dom.Node, org.w3c.dom.Node)

,

replaceChild(org.w3c.dom.Node, org.w3c.dom.Node)

,

appendChild(org.w3c.dom.Node)

---

#### getParentNode

public

Node

getParentNode()

Returns the parent of this node. A

null

value
indicates that the node is the root of its own tree. To add a
node to an existing tree, use one of the

insertBefore

,

replaceChild

, or

appendChild

methods.

getChildNodes

```java
public
NodeList
getChildNodes()
```

Returns a

NodeList

that contains all children of this node.
If there are no children, this is a

NodeList

containing
no nodes.

**Specified by:** getChildNodes

in interface

Node
**Returns:** the children as a

NodeList

---

#### getChildNodes

public

NodeList

getChildNodes()

Returns a

NodeList

that contains all children of this node.
If there are no children, this is a

NodeList

containing
no nodes.

getFirstChild

```java
public
Node
getFirstChild()
```

Returns the first child of this node, or

null

if
the node has no children.

**Specified by:** getFirstChild

in interface

Node
**Returns:** the first child, as a

Node

, or

null

---

#### getFirstChild

public

Node

getFirstChild()

Returns the first child of this node, or

null

if
the node has no children.

getLastChild

```java
public
Node
getLastChild()
```

Returns the last child of this node, or

null

if
the node has no children.

**Specified by:** getLastChild

in interface

Node
**Returns:** the last child, as a

Node

, or

null

.

---

#### getLastChild

public

Node

getLastChild()

Returns the last child of this node, or

null

if
the node has no children.

getPreviousSibling

```java
public
Node
getPreviousSibling()
```

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

**Specified by:** getPreviousSibling

in interface

Node
**Returns:** the previous sibling, as a

Node

, or

null

.

---

#### getPreviousSibling

public

Node

getPreviousSibling()

Returns the previous sibling of this node, or

null

if this node has no previous sibling.

getNextSibling

```java
public
Node
getNextSibling()
```

Returns the next sibling of this node, or

null

if
the node has no next sibling.

**Specified by:** getNextSibling

in interface

Node
**Returns:** the next sibling, as a

Node

, or

null

.

---

#### getNextSibling

public

Node

getNextSibling()

Returns the next sibling of this node, or

null

if
the node has no next sibling.

getAttributes

```java
public
NamedNodeMap
getAttributes()
```

Returns a

NamedNodeMap

containing the attributes of
this node.

**Specified by:** getAttributes

in interface

Node
**Returns:** a

NamedNodeMap

containing the attributes of
this node.

---

#### getAttributes

public

NamedNodeMap

getAttributes()

Returns a

NamedNodeMap

containing the attributes of
this node.

getOwnerDocument

```java
public
Document
getOwnerDocument()
```

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

**Specified by:** getOwnerDocument

in interface

Node
**Returns:** null

.

---

#### getOwnerDocument

public

Document

getOwnerDocument()

Returns

null

, since

IIOMetadataNode

s
do not belong to any

Document

.

insertBefore

```java
public
Node
insertBefore​(
Node
newChild,

Node
refChild)
```

Inserts the node

newChild

before the existing
child node

refChild

. If

refChild

is

null

, insert

newChild

at the end of
the list of children.

**Specified by:** insertBefore

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Parameters:** refChild

- the reference

Node

.
**Returns:** the node being inserted.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

---

#### insertBefore

public

Node

insertBefore​(

Node

newChild,

Node

refChild)

Inserts the node

newChild

before the existing
child node

refChild

. If

refChild

is

null

, insert

newChild

at the end of
the list of children.

replaceChild

```java
public
Node
replaceChild​(
Node
newChild,

Node
oldChild)
```

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

**Specified by:** replaceChild

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Parameters:** oldChild

- the

Node

to be replaced.
**Returns:** the node replaced.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

---

#### replaceChild

public

Node

replaceChild​(

Node

newChild,

Node

oldChild)

Replaces the child node

oldChild

with

newChild

in the list of children, and returns the

oldChild

node.

removeChild

```java
public
Node
removeChild​(
Node
oldChild)
```

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

**Specified by:** removeChild

in interface

Node
**Parameters:** oldChild

- the

Node

to be removed.
**Returns:** the node removed.
**Throws:** IllegalArgumentException

- if

oldChild

is

null

.

---

#### removeChild

public

Node

removeChild​(

Node

oldChild)

Removes the child node indicated by

oldChild

from
the list of children, and returns it.

appendChild

```java
public
Node
appendChild​(
Node
newChild)
```

Adds the node

newChild

to the end of the list of
children of this node.

**Specified by:** appendChild

in interface

Node
**Parameters:** newChild

- the

Node

to insert.
**Returns:** the node added.
**Throws:** IllegalArgumentException

- if

newChild

is

null

.

---

#### appendChild

public

Node

appendChild​(

Node

newChild)

Adds the node

newChild

to the end of the list of
children of this node.

hasChildNodes

```java
public boolean hasChildNodes()
```

Returns

true

if this node has child nodes.

**Specified by:** hasChildNodes

in interface

Node
**Returns:** true

if this node has children.

---

#### hasChildNodes

public boolean hasChildNodes()

Returns

true

if this node has child nodes.

cloneNode

```java
public
Node
cloneNode​(boolean deep)
```

Returns a duplicate of this node. The duplicate node has no
parent (

getParentNode

returns

null

).
If a shallow clone is being performed (

deep

is

false

), the new node will not have any children or
siblings. If a deep clone is being performed, the new node
will form the root of a complete cloned subtree.

**Specified by:** cloneNode

in interface

Node
**Parameters:** deep

- if

true

, recursively clone the subtree
under the specified node; if

false

, clone only the
node itself.
**Returns:** the duplicate node.

---

#### cloneNode

public

Node

cloneNode​(boolean deep)

Returns a duplicate of this node. The duplicate node has no
parent (

getParentNode

returns

null

).
If a shallow clone is being performed (

deep

is

false

), the new node will not have any children or
siblings. If a deep clone is being performed, the new node
will form the root of a complete cloned subtree.

normalize

```java
public void normalize()
```

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

**Specified by:** normalize

in interface

Node

---

#### normalize

public void normalize()

Does nothing, since

IIOMetadataNode

s do not
contain

Text

children.

isSupported

```java
public boolean isSupported​(
String
feature,

String
version)
```

Returns

false

since DOM features are not
supported.

**Specified by:** isSupported

in interface

Node
**Parameters:** feature

- a

String

, which is ignored.
**Parameters:** version

- a

String

, which is ignored.
**Returns:** false

.

---

#### isSupported

public boolean isSupported​(

String

feature,

String

version)

Returns

false

since DOM features are not
supported.

getNamespaceURI

```java
public
String
getNamespaceURI()
throws
DOMException
```

Returns

null

, since namespaces are not supported.

**Specified by:** getNamespaceURI

in interface

Node
**Throws:** DOMException

---

#### getNamespaceURI

public

String

getNamespaceURI()
throws

DOMException

Returns

null

, since namespaces are not supported.

getPrefix

```java
public
String
getPrefix()
```

Returns

null

, since namespaces are not supported.

**Specified by:** getPrefix

in interface

Node
**Returns:** null

.
**See Also:** setPrefix(java.lang.String)

---

#### getPrefix

public

String

getPrefix()

Returns

null

, since namespaces are not supported.

setPrefix

```java
public void setPrefix​(
String
prefix)
```

Does nothing, since namespaces are not supported.

**Specified by:** setPrefix

in interface

Node
**Parameters:** prefix

- a

String

, which is ignored.
**See Also:** getPrefix()

---

#### setPrefix

public void setPrefix​(

String

prefix)

Does nothing, since namespaces are not supported.

getLocalName

```java
public
String
getLocalName()
```

Equivalent to

getNodeName

.

**Specified by:** getLocalName

in interface

Node
**Returns:** the node name, as a

String

.

---

#### getLocalName

public

String

getLocalName()

Equivalent to

getNodeName

.

getTagName

```java
public
String
getTagName()
```

Equivalent to

getNodeName

.

**Specified by:** getTagName

in interface

Element
**Returns:** the node name, as a

String

---

#### getTagName

public

String

getTagName()

Equivalent to

getNodeName

.

getAttribute

```java
public
String
getAttribute​(
String
name)
```

Retrieves an attribute value by name.

**Specified by:** getAttribute

in interface

Element
**Parameters:** name

- The name of the attribute to retrieve.
**Returns:** The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.

---

#### getAttribute

public

String

getAttribute​(

String

name)

Retrieves an attribute value by name.

getAttributeNS

```java
public
String
getAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getAttribute(localName)

.

**Specified by:** getAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to retrieve.
**Parameters:** localName

- The local name of the attribute to retrieve.
**Returns:** The

Attr

value as a string, or the empty string
if that attribute does not have a specified or default value.
**See Also:** setAttributeNS(java.lang.String, java.lang.String, java.lang.String)

---

#### getAttributeNS

public

String

getAttributeNS​(

String

namespaceURI,

String

localName)

Equivalent to

getAttribute(localName)

.

setAttributeNS

```java
public void setAttributeNS​(
String
namespaceURI,

String
qualifiedName,

String
value)
```

Equivalent to

setAttribute(qualifiedName, value)

.

**Specified by:** setAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to create or
alter.
**Parameters:** qualifiedName

- The qualified name of the attribute to create or
alter.
**Parameters:** value

- The value to set in string form.
**See Also:** getAttributeNS(java.lang.String, java.lang.String)

---

#### setAttributeNS

public void setAttributeNS​(

String

namespaceURI,

String

qualifiedName,

String

value)

Equivalent to

setAttribute(qualifiedName, value)

.

removeAttributeNS

```java
public void removeAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

removeAttribute(localName)

.

**Specified by:** removeAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to remove.
**Parameters:** localName

- The local name of the attribute to remove.

---

#### removeAttributeNS

public void removeAttributeNS​(

String

namespaceURI,

String

localName)

Equivalent to

removeAttribute(localName)

.

getAttributeNodeNS

```java
public
Attr
getAttributeNodeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getAttributeNode(localName)

.

**Specified by:** getAttributeNodeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to retrieve.
**Parameters:** localName

- The local name of the attribute to retrieve.
**Returns:** The

Attr

node with the specified attribute local
name and namespace URI or

null

if there is no such
attribute.
**See Also:** setAttributeNodeNS(org.w3c.dom.Attr)

---

#### getAttributeNodeNS

public

Attr

getAttributeNodeNS​(

String

namespaceURI,

String

localName)

Equivalent to

getAttributeNode(localName)

.

setAttributeNodeNS

```java
public
Attr
setAttributeNodeNS​(
Attr
newAttr)
```

Equivalent to

setAttributeNode(newAttr)

.

**Specified by:** setAttributeNodeNS

in interface

Element
**Parameters:** newAttr

- The

Attr

node to add to the attribute list.
**Returns:** If the

newAttr

attribute replaces an existing
attribute with the same local name and namespace URI, the replaced

Attr

node is returned, otherwise

null

is
returned.
**See Also:** getAttributeNodeNS(java.lang.String, java.lang.String)

---

#### setAttributeNodeNS

public

Attr

setAttributeNodeNS​(

Attr

newAttr)

Equivalent to

setAttributeNode(newAttr)

.

getElementsByTagNameNS

```java
public
NodeList
getElementsByTagNameNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

getElementsByTagName(localName)

.

**Specified by:** getElementsByTagNameNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the elements to match on. The
special value "*" matches all namespaces.
**Parameters:** localName

- The local name of the elements to match on. The
special value "*" matches all local names.
**Returns:** A new

NodeList

object containing all the matched

Elements

.

---

#### getElementsByTagNameNS

public

NodeList

getElementsByTagNameNS​(

String

namespaceURI,

String

localName)

Equivalent to

getElementsByTagName(localName)

.

hasAttributeNS

```java
public boolean hasAttributeNS​(
String
namespaceURI,

String
localName)
```

Equivalent to

hasAttribute(localName)

.

**Specified by:** hasAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute to look for.
**Parameters:** localName

- The local name of the attribute to look for.
**Returns:** true

if an attribute with the given local name
and namespace URI is specified or has a default value on this
element,

false

otherwise.

---

#### hasAttributeNS

public boolean hasAttributeNS​(

String

namespaceURI,

String

localName)

Equivalent to

hasAttribute(localName)

.

getUserObject

```java
public
Object
getUserObject()
```

Returns the

Object

value associated with this node.

**Returns:** the user

Object

.
**See Also:** setUserObject(java.lang.Object)

---

#### getUserObject

public

Object

getUserObject()

Returns the

Object

value associated with this node.

setUserObject

```java
public void setUserObject​(
Object
userObject)
```

Sets the value associated with this node.

**Parameters:** userObject

- the user

Object

.
**See Also:** getUserObject()

---

#### setUserObject

public void setUserObject​(

Object

userObject)

Sets the value associated with this node.

setIdAttribute

```java
public void setIdAttribute​(
String
name,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttribute

in interface

Element
**Parameters:** name

- The name of the attribute.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

---

#### setIdAttribute

public void setIdAttribute​(

String

name,
boolean isId)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

setIdAttributeNS

```java
public void setIdAttributeNS​(
String
namespaceURI,

String
localName,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttributeNS

in interface

Element
**Parameters:** namespaceURI

- The namespace URI of the attribute.
**Parameters:** localName

- The local name of the attribute.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

---

#### setIdAttributeNS

public void setIdAttributeNS​(

String

namespaceURI,

String

localName,
boolean isId)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

setIdAttributeNode

```java
public void setIdAttributeNode​(
Attr
idAttr,
boolean isId)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setIdAttributeNode

in interface

Element
**Parameters:** idAttr

- The attribute node.
**Parameters:** isId

- Whether the attribute is a of type ID.
**Throws:** DOMException

- always.

---

#### setIdAttributeNode

public void setIdAttributeNode​(

Attr

idAttr,
boolean isId)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

getSchemaTypeInfo

```java
public
TypeInfo
getSchemaTypeInfo()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getSchemaTypeInfo

in interface

Element
**Throws:** DOMException

- always.

---

#### getSchemaTypeInfo

public

TypeInfo

getSchemaTypeInfo()
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

setUserData

```java
public
Object
setUserData​(
String
key,

Object
data,

UserDataHandler
handler)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setUserData

in interface

Node
**Parameters:** key

- The key to associate the object to.
**Parameters:** data

- The object to associate to the given key, or

null

to remove any existing association to that key.
**Parameters:** handler

- The handler to associate to that key, or

null

.
**Returns:** Returns the

DOMUserData

previously associated to
the given key on this node, or

null

if there was none.
**Throws:** DOMException

- always.

---

#### setUserData

public

Object

setUserData​(

String

key,

Object

data,

UserDataHandler

handler)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

getUserData

```java
public
Object
getUserData​(
String
key)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getUserData

in interface

Node
**Parameters:** key

- The key the object is associated to.
**Returns:** Returns the

DOMUserData

associated to the given
key on this node, or

null

if there was none.
**Throws:** DOMException

- always.

---

#### getUserData

public

Object

getUserData​(

String

key)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

getFeature

```java
public
Object
getFeature​(
String
feature,

String
version)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getFeature

in interface

Node
**Parameters:** feature

- The name of the feature requested. Note that any plus
sign "+" prepended to the name of the feature will be ignored since
it is not significant in the context of this method.
**Parameters:** version

- This is the version number of the feature to test.
**Returns:** Returns an object which implements the specialized APIs of
the specified feature and version, if any, or

null

if
there is no object which implements interfaces associated with that
feature. If the

DOMObject

returned by this method
implements the

Node

interface, it must delegate to the
primary core

Node

and not return results inconsistent
with the primary core

Node

such as attributes,
childNodes, etc.
**Throws:** DOMException

- always.

---

#### getFeature

public

Object

getFeature​(

String

feature,

String

version)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

isSameNode

```java
public boolean isSameNode​(
Node
node)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isSameNode

in interface

Node
**Parameters:** node

- The node to test against.
**Returns:** Returns

true

if the nodes are the same,

false

otherwise.
**Throws:** DOMException

- always.

---

#### isSameNode

public boolean isSameNode​(

Node

node)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

isEqualNode

```java
public boolean isEqualNode​(
Node
node)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isEqualNode

in interface

Node
**Parameters:** node

- The node to compare equality with.
**Returns:** Returns

true

if the nodes are equal,

false

otherwise.
**Throws:** DOMException

- always.

---

#### isEqualNode

public boolean isEqualNode​(

Node

node)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

lookupNamespaceURI

```java
public
String
lookupNamespaceURI​(
String
prefix)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** lookupNamespaceURI

in interface

Node
**Parameters:** prefix

- The prefix to look for. If this parameter is

null

, the method will return the default namespace URI
if any.
**Returns:** Returns the associated namespace URI or

null

if
none is found.
**Throws:** DOMException

- always.

---

#### lookupNamespaceURI

public

String

lookupNamespaceURI​(

String

prefix)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

isDefaultNamespace

```java
public boolean isDefaultNamespace​(
String
namespaceURI)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** isDefaultNamespace

in interface

Node
**Parameters:** namespaceURI

- The namespace URI to look for.
**Returns:** Returns

true

if the specified

namespaceURI

is the default namespace,

false

otherwise.
**Throws:** DOMException

- always.

---

#### isDefaultNamespace

public boolean isDefaultNamespace​(

String

namespaceURI)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

lookupPrefix

```java
public
String
lookupPrefix​(
String
namespaceURI)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** lookupPrefix

in interface

Node
**Parameters:** namespaceURI

- The namespace URI to look for.
**Returns:** Returns an associated namespace prefix if found or

null

if none is found. If more than one prefix are
associated to the namespace prefix, the returned namespace prefix
is implementation dependent.
**Throws:** DOMException

- always.

---

#### lookupPrefix

public

String

lookupPrefix​(

String

namespaceURI)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

getTextContent

```java
public
String
getTextContent()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getTextContent

in interface

Node
**Throws:** DOMException

- always.

---

#### getTextContent

public

String

getTextContent()
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

setTextContent

```java
public void setTextContent​(
String
textContent)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** setTextContent

in interface

Node
**Throws:** DOMException

- always.

---

#### setTextContent

public void setTextContent​(

String

textContent)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

compareDocumentPosition

```java
public short compareDocumentPosition​(
Node
other)
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** compareDocumentPosition

in interface

Node
**Parameters:** other

- The node to compare against the reference node.
**Returns:** Returns how the node is positioned relatively to the reference
node.
**Throws:** DOMException

- always.

---

#### compareDocumentPosition

public short compareDocumentPosition​(

Node

other)
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

getBaseURI

```java
public
String
getBaseURI()
throws
DOMException
```

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

**Specified by:** getBaseURI

in interface

Node
**Throws:** DOMException

- always.

---

#### getBaseURI

public

String

getBaseURI()
throws

DOMException

This DOM Level 3 method is not supported for

IIOMetadataNode

and will throw a

DOMException

.

---

