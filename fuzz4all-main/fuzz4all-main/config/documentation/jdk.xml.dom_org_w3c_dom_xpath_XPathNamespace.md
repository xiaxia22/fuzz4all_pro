# Interface XPathNamespace

**Source:** `jdk.xml.dom\org\w3c\dom\xpath\XPathNamespace.html`

### Class Description

```java
public interface
XPathNamespace

extends
Node
```

The

XPathNamespace

interface is returned by

XPathResult

interfaces to represent the XPath namespace node
type that DOM lacks. There is no public constructor for this node type.
Attempts to place it into a hierarchy or a NamedNodeMap result in a

DOMException

with the code

HIERARCHY_REQUEST_ERR

. This node is read only, so methods or setting of attributes that would
mutate the node result in a DOMException with the code

NO_MODIFICATION_ALLOWED_ERR

.

The core specification describes attributes of the

Node

interface that are different for different node node types but does not
describe

XPATH_NAMESPACE_NODE

, so here is a description of
those attributes for this node type. All attributes of

Node

not described in this section have a

null

or

false

value.

ownerDocument

matches the

ownerDocument

of the

ownerElement

even if the element is later adopted.

prefix

is the prefix of the namespace represented by the
node.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

**All Superinterfaces:** Node

---

### Field Details

#### static final short XPATH_NAMESPACE_NODE

The node is a

Namespace

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Element
getOwnerElement()

The

Element

on which the namespace was in scope when it
was requested. This does not change on a returned namespace node even
if the document changes such that the namespace goes out of scope on
that element and this node is no longer found there by XPath.

---

### Additional Sections

#### Interface XPathNamespace

**All Superinterfaces:** Node

```java
public interface
XPathNamespace

extends
Node
```

The

XPathNamespace

interface is returned by

XPathResult

interfaces to represent the XPath namespace node
type that DOM lacks. There is no public constructor for this node type.
Attempts to place it into a hierarchy or a NamedNodeMap result in a

DOMException

with the code

HIERARCHY_REQUEST_ERR

. This node is read only, so methods or setting of attributes that would
mutate the node result in a DOMException with the code

NO_MODIFICATION_ALLOWED_ERR

.

The core specification describes attributes of the

Node

interface that are different for different node node types but does not
describe

XPATH_NAMESPACE_NODE

, so here is a description of
those attributes for this node type. All attributes of

Node

not described in this section have a

null

or

false

value.

ownerDocument

matches the

ownerDocument

of the

ownerElement

even if the element is later adopted.

prefix

is the prefix of the namespace represented by the
node.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

public interface

XPathNamespace

extends

Node

The

XPathNamespace

interface is returned by

XPathResult

interfaces to represent the XPath namespace node
type that DOM lacks. There is no public constructor for this node type.
Attempts to place it into a hierarchy or a NamedNodeMap result in a

DOMException

with the code

HIERARCHY_REQUEST_ERR

. This node is read only, so methods or setting of attributes that would
mutate the node result in a DOMException with the code

NO_MODIFICATION_ALLOWED_ERR

.

The core specification describes attributes of the

Node

interface that are different for different node node types but does not
describe

XPATH_NAMESPACE_NODE

, so here is a description of
those attributes for this node type. All attributes of

Node

not described in this section have a

null

or

false

value.

ownerDocument

matches the

ownerDocument

of the

ownerElement

even if the element is later adopted.

prefix

is the prefix of the namespace represented by the
node.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

The core specification describes attributes of the

Node

interface that are different for different node node types but does not
describe

XPATH_NAMESPACE_NODE

, so here is a description of
those attributes for this node type. All attributes of

Node

not described in this section have a

null

or

false

value.

ownerDocument

matches the

ownerDocument

of the

ownerElement

even if the element is later adopted.

prefix

is the prefix of the namespace represented by the
node.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

ownerDocument

matches the

ownerDocument

of the

ownerElement

even if the element is later adopted.

prefix

is the prefix of the namespace represented by the
node.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

prefix

is the prefix of the namespace represented by the
node.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

nodeName

is the same as

prefix

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

nodeType

is equal to

XPATH_NAMESPACE_NODE

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

namespaceURI

is the namespace URI of the namespace
represented by the node.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

adoptNode

,

cloneNode

, and

importNode

fail on this node type by raising a

DOMException

with the code

NOT_SUPPORTED_ERR

.In
future versions of the XPath specification, the definition of a namespace
node may be changed incomatibly, in which case incompatible changes to
field values may be required to implement versions beyond XPath 1.0.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

See also the

Document Object Model (DOM) Level 3 XPath Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

XPATH_NAMESPACE_NODE

The node is a

Namespace

.

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

Element

getOwnerElement

()

The

Element

on which the namespace was in scope when it
was requested.

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

Fields

Modifier and Type

Field

Description

static short

XPATH_NAMESPACE_NODE

The node is a

Namespace

.

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

The node is a

Namespace

.

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

Element

getOwnerElement

()

The

Element

on which the namespace was in scope when it
was requested.

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

The

Element

on which the namespace was in scope when it
was requested.

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

============ FIELD DETAIL ===========

- Field Detail

- XPATH_NAMESPACE_NODE

```java
static final short XPATH_NAMESPACE_NODE
```

The node is a

Namespace

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getOwnerElement

```java
Element
getOwnerElement()
```

The

Element

on which the namespace was in scope when it
was requested. This does not change on a returned namespace node even
if the document changes such that the namespace goes out of scope on
that element and this node is no longer found there by XPath.

Field Detail

- XPATH_NAMESPACE_NODE

```java
static final short XPATH_NAMESPACE_NODE
```

The node is a

Namespace

.

**See Also:** Constant Field Values

---

#### Field Detail

XPATH_NAMESPACE_NODE

```java
static final short XPATH_NAMESPACE_NODE
```

The node is a

Namespace

.

**See Also:** Constant Field Values

---

#### XPATH_NAMESPACE_NODE

static final short XPATH_NAMESPACE_NODE

The node is a

Namespace

.

Method Detail

- getOwnerElement

```java
Element
getOwnerElement()
```

The

Element

on which the namespace was in scope when it
was requested. This does not change on a returned namespace node even
if the document changes such that the namespace goes out of scope on
that element and this node is no longer found there by XPath.

---

#### Method Detail

getOwnerElement

```java
Element
getOwnerElement()
```

The

Element

on which the namespace was in scope when it
was requested. This does not change on a returned namespace node even
if the document changes such that the namespace goes out of scope on
that element and this node is no longer found there by XPath.

---

#### getOwnerElement

Element

getOwnerElement()

The

Element

on which the namespace was in scope when it
was requested. This does not change on a returned namespace node even
if the document changes such that the namespace goes out of scope on
that element and this node is no longer found there by XPath.

---

