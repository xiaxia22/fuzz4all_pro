# Interface Notation

**Source:** `java.xml\org\w3c\dom\Notation.html`

### Class Description

```java
public interface
Notation

extends
Node
```

This interface represents a notation declared in the DTD. A notation either
declares, by name, the format of an unparsed entity (see

section 4.7

of the XML 1.0 specification [

XML 1.0

]), or is
used for formal declaration of processing instruction targets (see

section 2.6

of the XML 1.0 specification [

XML 1.0

]). The

nodeName

attribute inherited from

Node

is set
to the declared name of the notation.

The DOM Core does not support editing

Notation

nodes; they
are therefore readonly.

A

Notation

node does not have any parent.

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
getPublicId()

The public identifier of this notation. If the public identifier was
not specified, this is

null

.

---

#### String
getSystemId()

The system identifier of this notation. If the system identifier was
not specified, this is

null

. This may be an absolute URI
or not.

---

### Additional Sections

#### Interface Notation

**All Superinterfaces:** Node

```java
public interface
Notation

extends
Node
```

This interface represents a notation declared in the DTD. A notation either
declares, by name, the format of an unparsed entity (see

section 4.7

of the XML 1.0 specification [

XML 1.0

]), or is
used for formal declaration of processing instruction targets (see

section 2.6

of the XML 1.0 specification [

XML 1.0

]). The

nodeName

attribute inherited from

Node

is set
to the declared name of the notation.

The DOM Core does not support editing

Notation

nodes; they
are therefore readonly.

A

Notation

node does not have any parent.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

Notation

extends

Node

This interface represents a notation declared in the DTD. A notation either
declares, by name, the format of an unparsed entity (see

section 4.7

of the XML 1.0 specification [

XML 1.0

]), or is
used for formal declaration of processing instruction targets (see

section 2.6

of the XML 1.0 specification [

XML 1.0

]). The

nodeName

attribute inherited from

Node

is set
to the declared name of the notation.

The DOM Core does not support editing

Notation

nodes; they
are therefore readonly.

A

Notation

node does not have any parent.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The DOM Core does not support editing

Notation

nodes; they
are therefore readonly.

A

Notation

node does not have any parent.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

A

Notation

node does not have any parent.

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

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getPublicId

()

The public identifier of this notation.

String

getSystemId

()

The system identifier of this notation.

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

getPublicId

()

The public identifier of this notation.

String

getSystemId

()

The system identifier of this notation.

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

The public identifier of this notation.

The system identifier of this notation.

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

- getPublicId

```java
String
getPublicId()
```

The public identifier of this notation. If the public identifier was
not specified, this is

null

.

- getSystemId

```java
String
getSystemId()
```

The system identifier of this notation. If the system identifier was
not specified, this is

null

. This may be an absolute URI
or not.

Method Detail

- getPublicId

```java
String
getPublicId()
```

The public identifier of this notation. If the public identifier was
not specified, this is

null

.

- getSystemId

```java
String
getSystemId()
```

The system identifier of this notation. If the system identifier was
not specified, this is

null

. This may be an absolute URI
or not.

---

#### Method Detail

getPublicId

```java
String
getPublicId()
```

The public identifier of this notation. If the public identifier was
not specified, this is

null

.

---

#### getPublicId

String

getPublicId()

The public identifier of this notation. If the public identifier was
not specified, this is

null

.

getSystemId

```java
String
getSystemId()
```

The system identifier of this notation. If the system identifier was
not specified, this is

null

. This may be an absolute URI
or not.

---

#### getSystemId

String

getSystemId()

The system identifier of this notation. If the system identifier was
not specified, this is

null

. This may be an absolute URI
or not.

---

