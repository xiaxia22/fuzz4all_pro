# Interface EntityReference

**Source:** `java.xml\org\w3c\dom\EntityReference.html`

### Class Description

```java
public interface
EntityReference

extends
Node
```

EntityReference

nodes may be used to represent an entity
reference in the tree. Note that character references and references to
predefined entities are considered to be expanded by the HTML or XML
processor so that characters are represented by their Unicode equivalent
rather than by an entity reference. Moreover, the XML processor may
completely expand references to entities while building the

Document

, instead of providing

EntityReference

nodes. If it does provide such nodes, then for an

EntityReference

node that represents a reference to a known
entity an

Entity

exists, and the subtree of the

EntityReference

node is a copy of the

Entity

node subtree. However, the latter may not be true when an entity contains
an unbound namespace prefix. In such a case, because the namespace prefix
resolution depends on where the entity reference is, the descendants of
the

EntityReference

node may be bound to different namespace
URIs. When an

EntityReference

node represents a reference to
an unknown entity, the node has no children and its replacement value,
when used by

Attr.value

for example, is empty.

As for

Entity

nodes,

EntityReference

nodes and
all their descendants are readonly.

Note:

EntityReference

nodes may cause element
content and attribute value normalization problems when, such as in XML
1.0 and XML Schema, the normalization is performed after entity reference
are expanded.

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

#### Interface EntityReference

**All Superinterfaces:** Node

```java
public interface
EntityReference

extends
Node
```

EntityReference

nodes may be used to represent an entity
reference in the tree. Note that character references and references to
predefined entities are considered to be expanded by the HTML or XML
processor so that characters are represented by their Unicode equivalent
rather than by an entity reference. Moreover, the XML processor may
completely expand references to entities while building the

Document

, instead of providing

EntityReference

nodes. If it does provide such nodes, then for an

EntityReference

node that represents a reference to a known
entity an

Entity

exists, and the subtree of the

EntityReference

node is a copy of the

Entity

node subtree. However, the latter may not be true when an entity contains
an unbound namespace prefix. In such a case, because the namespace prefix
resolution depends on where the entity reference is, the descendants of
the

EntityReference

node may be bound to different namespace
URIs. When an

EntityReference

node represents a reference to
an unknown entity, the node has no children and its replacement value,
when used by

Attr.value

for example, is empty.

As for

Entity

nodes,

EntityReference

nodes and
all their descendants are readonly.

Note:

EntityReference

nodes may cause element
content and attribute value normalization problems when, such as in XML
1.0 and XML Schema, the normalization is performed after entity reference
are expanded.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

EntityReference

extends

Node

EntityReference

nodes may be used to represent an entity
reference in the tree. Note that character references and references to
predefined entities are considered to be expanded by the HTML or XML
processor so that characters are represented by their Unicode equivalent
rather than by an entity reference. Moreover, the XML processor may
completely expand references to entities while building the

Document

, instead of providing

EntityReference

nodes. If it does provide such nodes, then for an

EntityReference

node that represents a reference to a known
entity an

Entity

exists, and the subtree of the

EntityReference

node is a copy of the

Entity

node subtree. However, the latter may not be true when an entity contains
an unbound namespace prefix. In such a case, because the namespace prefix
resolution depends on where the entity reference is, the descendants of
the

EntityReference

node may be bound to different namespace
URIs. When an

EntityReference

node represents a reference to
an unknown entity, the node has no children and its replacement value,
when used by

Attr.value

for example, is empty.

As for

Entity

nodes,

EntityReference

nodes and
all their descendants are readonly.

Note:

EntityReference

nodes may cause element
content and attribute value normalization problems when, such as in XML
1.0 and XML Schema, the normalization is performed after entity reference
are expanded.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

As for

Entity

nodes,

EntityReference

nodes and
all their descendants are readonly.

Note:

EntityReference

nodes may cause element
content and attribute value normalization problems when, such as in XML
1.0 and XML Schema, the normalization is performed after entity reference
are expanded.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

Note:

EntityReference

nodes may cause element
content and attribute value normalization problems when, such as in XML
1.0 and XML Schema, the normalization is performed after entity reference
are expanded.

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

