# Interface DocumentFragment

**Source:** `java.xml\org\w3c\dom\DocumentFragment.html`

### Class Description

```java
public interface
DocumentFragment

extends
Node
```

DocumentFragment

is a "lightweight" or "minimal"

Document

object. It is very common to want to be able to
extract a portion of a document's tree or to create a new fragment of a
document. Imagine implementing a user command like cut or rearranging a
document by moving fragments around. It is desirable to have an object
which can hold such fragments and it is quite natural to use a Node for
this purpose. While it is true that a

Document

object could
fulfill this role, a

Document

object can potentially be a
heavyweight object, depending on the underlying implementation. What is
really needed for this is a very lightweight object.

DocumentFragment

is such an object.

Furthermore, various operations -- such as inserting nodes as children
of another

Node

-- may take

DocumentFragment

objects as arguments; this results in all the child nodes of the

DocumentFragment

being moved to the child list of this node.

The children of a

DocumentFragment

node are zero or more
nodes representing the tops of any sub-trees defining the structure of
the document.

DocumentFragment

nodes do not need to be
well-formed XML documents (although they do need to follow the rules
imposed upon well-formed XML parsed entities, which can have multiple top
nodes). For example, a

DocumentFragment

might have only one
child and that child node could be a

Text

node. Such a
structure model represents neither an HTML document nor a well-formed XML
document.

When a

DocumentFragment

is inserted into a

Document

(or indeed any other

Node

that may
take children) the children of the

DocumentFragment

and not
the

DocumentFragment

itself are inserted into the

Node

. This makes the

DocumentFragment

very
useful when the user wishes to create nodes that are siblings; the

DocumentFragment

acts as the parent of these nodes so that
the user can use the standard methods from the

Node

interface, such as

Node.insertBefore

and

Node.appendChild

.

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

*No entries found.*

### Additional Sections

#### Interface DocumentFragment

**All Superinterfaces:** Node

```java
public interface
DocumentFragment

extends
Node
```

DocumentFragment

is a "lightweight" or "minimal"

Document

object. It is very common to want to be able to
extract a portion of a document's tree or to create a new fragment of a
document. Imagine implementing a user command like cut or rearranging a
document by moving fragments around. It is desirable to have an object
which can hold such fragments and it is quite natural to use a Node for
this purpose. While it is true that a

Document

object could
fulfill this role, a

Document

object can potentially be a
heavyweight object, depending on the underlying implementation. What is
really needed for this is a very lightweight object.

DocumentFragment

is such an object.

Furthermore, various operations -- such as inserting nodes as children
of another

Node

-- may take

DocumentFragment

objects as arguments; this results in all the child nodes of the

DocumentFragment

being moved to the child list of this node.

The children of a

DocumentFragment

node are zero or more
nodes representing the tops of any sub-trees defining the structure of
the document.

DocumentFragment

nodes do not need to be
well-formed XML documents (although they do need to follow the rules
imposed upon well-formed XML parsed entities, which can have multiple top
nodes). For example, a

DocumentFragment

might have only one
child and that child node could be a

Text

node. Such a
structure model represents neither an HTML document nor a well-formed XML
document.

When a

DocumentFragment

is inserted into a

Document

(or indeed any other

Node

that may
take children) the children of the

DocumentFragment

and not
the

DocumentFragment

itself are inserted into the

Node

. This makes the

DocumentFragment

very
useful when the user wishes to create nodes that are siblings; the

DocumentFragment

acts as the parent of these nodes so that
the user can use the standard methods from the

Node

interface, such as

Node.insertBefore

and

Node.appendChild

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

DocumentFragment

extends

Node

DocumentFragment

is a "lightweight" or "minimal"

Document

object. It is very common to want to be able to
extract a portion of a document's tree or to create a new fragment of a
document. Imagine implementing a user command like cut or rearranging a
document by moving fragments around. It is desirable to have an object
which can hold such fragments and it is quite natural to use a Node for
this purpose. While it is true that a

Document

object could
fulfill this role, a

Document

object can potentially be a
heavyweight object, depending on the underlying implementation. What is
really needed for this is a very lightweight object.

DocumentFragment

is such an object.

Furthermore, various operations -- such as inserting nodes as children
of another

Node

-- may take

DocumentFragment

objects as arguments; this results in all the child nodes of the

DocumentFragment

being moved to the child list of this node.

The children of a

DocumentFragment

node are zero or more
nodes representing the tops of any sub-trees defining the structure of
the document.

DocumentFragment

nodes do not need to be
well-formed XML documents (although they do need to follow the rules
imposed upon well-formed XML parsed entities, which can have multiple top
nodes). For example, a

DocumentFragment

might have only one
child and that child node could be a

Text

node. Such a
structure model represents neither an HTML document nor a well-formed XML
document.

When a

DocumentFragment

is inserted into a

Document

(or indeed any other

Node

that may
take children) the children of the

DocumentFragment

and not
the

DocumentFragment

itself are inserted into the

Node

. This makes the

DocumentFragment

very
useful when the user wishes to create nodes that are siblings; the

DocumentFragment

acts as the parent of these nodes so that
the user can use the standard methods from the

Node

interface, such as

Node.insertBefore

and

Node.appendChild

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

Furthermore, various operations -- such as inserting nodes as children
of another

Node

-- may take

DocumentFragment

objects as arguments; this results in all the child nodes of the

DocumentFragment

being moved to the child list of this node.

The children of a

DocumentFragment

node are zero or more
nodes representing the tops of any sub-trees defining the structure of
the document.

DocumentFragment

nodes do not need to be
well-formed XML documents (although they do need to follow the rules
imposed upon well-formed XML parsed entities, which can have multiple top
nodes). For example, a

DocumentFragment

might have only one
child and that child node could be a

Text

node. Such a
structure model represents neither an HTML document nor a well-formed XML
document.

When a

DocumentFragment

is inserted into a

Document

(or indeed any other

Node

that may
take children) the children of the

DocumentFragment

and not
the

DocumentFragment

itself are inserted into the

Node

. This makes the

DocumentFragment

very
useful when the user wishes to create nodes that are siblings; the

DocumentFragment

acts as the parent of these nodes so that
the user can use the standard methods from the

Node

interface, such as

Node.insertBefore

and

Node.appendChild

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The children of a

DocumentFragment

node are zero or more
nodes representing the tops of any sub-trees defining the structure of
the document.

DocumentFragment

nodes do not need to be
well-formed XML documents (although they do need to follow the rules
imposed upon well-formed XML parsed entities, which can have multiple top
nodes). For example, a

DocumentFragment

might have only one
child and that child node could be a

Text

node. Such a
structure model represents neither an HTML document nor a well-formed XML
document.

When a

DocumentFragment

is inserted into a

Document

(or indeed any other

Node

that may
take children) the children of the

DocumentFragment

and not
the

DocumentFragment

itself are inserted into the

Node

. This makes the

DocumentFragment

very
useful when the user wishes to create nodes that are siblings; the

DocumentFragment

acts as the parent of these nodes so that
the user can use the standard methods from the

Node

interface, such as

Node.insertBefore

and

Node.appendChild

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

When a

DocumentFragment

is inserted into a

Document

(or indeed any other

Node

that may
take children) the children of the

DocumentFragment

and not
the

DocumentFragment

itself are inserted into the

Node

. This makes the

DocumentFragment

very
useful when the user wishes to create nodes that are siblings; the

DocumentFragment

acts as the parent of these nodes so that
the user can use the standard methods from the

Node

interface, such as

Node.insertBefore

and

Node.appendChild

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

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

