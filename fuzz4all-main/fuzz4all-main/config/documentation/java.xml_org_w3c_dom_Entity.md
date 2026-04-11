# Interface Entity

**Source:** `java.xml\org\w3c\dom\Entity.html`

### Class Description

```java
public interface
Entity

extends
Node
```

This interface represents a known entity, either parsed or unparsed, in an
XML document. Note that this models the entity itself

not

the entity declaration.

The

nodeName

attribute that is inherited from

Node

contains the name of the entity.

An XML processor may choose to completely expand entities before the
structure model is passed to the DOM; in this case there will be no

EntityReference

nodes in the document tree.

XML does not mandate that a non-validating XML processor read and
process entity declarations made in the external subset or declared in
parameter entities. This means that parsed entities declared in the
external subset need not be expanded by some classes of applications, and
that the replacement text of the entity may not be available. When the

replacement text

is available, the corresponding

Entity

node's child list
represents the structure of that replacement value. Otherwise, the child
list is empty.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

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

The public identifier associated with the entity if specified, and

null

otherwise.

---

#### String
getSystemId()

The system identifier associated with the entity if specified, and

null

otherwise. This may be an absolute URI or not.

---

#### String
getNotationName()

For unparsed entities, the name of the notation for the entity. For
parsed entities, this is

null

.

---

#### String
getInputEncoding()

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity. This is

null

if it an entity from the internal subset or if it
is not known.

**Since:**
- 1.5, DOM Level 3

---

#### String
getXmlEncoding()

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:**
- 1.5, DOM Level 3

---

#### String
getXmlVersion()

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:**
- 1.5, DOM Level 3

---

### Additional Sections

#### Interface Entity

**All Superinterfaces:** Node

```java
public interface
Entity

extends
Node
```

This interface represents a known entity, either parsed or unparsed, in an
XML document. Note that this models the entity itself

not

the entity declaration.

The

nodeName

attribute that is inherited from

Node

contains the name of the entity.

An XML processor may choose to completely expand entities before the
structure model is passed to the DOM; in this case there will be no

EntityReference

nodes in the document tree.

XML does not mandate that a non-validating XML processor read and
process entity declarations made in the external subset or declared in
parameter entities. This means that parsed entities declared in the
external subset need not be expanded by some classes of applications, and
that the replacement text of the entity may not be available. When the

replacement text

is available, the corresponding

Entity

node's child list
represents the structure of that replacement value. Otherwise, the child
list is empty.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

Entity

extends

Node

This interface represents a known entity, either parsed or unparsed, in an
XML document. Note that this models the entity itself

not

the entity declaration.

The

nodeName

attribute that is inherited from

Node

contains the name of the entity.

An XML processor may choose to completely expand entities before the
structure model is passed to the DOM; in this case there will be no

EntityReference

nodes in the document tree.

XML does not mandate that a non-validating XML processor read and
process entity declarations made in the external subset or declared in
parameter entities. This means that parsed entities declared in the
external subset need not be expanded by some classes of applications, and
that the replacement text of the entity may not be available. When the

replacement text

is available, the corresponding

Entity

node's child list
represents the structure of that replacement value. Otherwise, the child
list is empty.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

The

nodeName

attribute that is inherited from

Node

contains the name of the entity.

An XML processor may choose to completely expand entities before the
structure model is passed to the DOM; in this case there will be no

EntityReference

nodes in the document tree.

XML does not mandate that a non-validating XML processor read and
process entity declarations made in the external subset or declared in
parameter entities. This means that parsed entities declared in the
external subset need not be expanded by some classes of applications, and
that the replacement text of the entity may not be available. When the

replacement text

is available, the corresponding

Entity

node's child list
represents the structure of that replacement value. Otherwise, the child
list is empty.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

An XML processor may choose to completely expand entities before the
structure model is passed to the DOM; in this case there will be no

EntityReference

nodes in the document tree.

XML does not mandate that a non-validating XML processor read and
process entity declarations made in the external subset or declared in
parameter entities. This means that parsed entities declared in the
external subset need not be expanded by some classes of applications, and
that the replacement text of the entity may not be available. When the

replacement text

is available, the corresponding

Entity

node's child list
represents the structure of that replacement value. Otherwise, the child
list is empty.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

XML does not mandate that a non-validating XML processor read and
process entity declarations made in the external subset or declared in
parameter entities. This means that parsed entities declared in the
external subset need not be expanded by some classes of applications, and
that the replacement text of the entity may not be available. When the

replacement text

is available, the corresponding

Entity

node's child list
represents the structure of that replacement value. Otherwise, the child
list is empty.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

DOM Level 3 does not support editing

Entity

nodes; if a
user wants to make changes to the contents of an

Entity

,
every related

EntityReference

node has to be replaced in the
structure model by a clone of the

Entity

's contents, and
then the desired changes must be made to each of those clones instead.

Entity

nodes and all their descendants are readonly.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

An

Entity

node does not have any parent.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

Note:

If the entity contains an unbound namespace prefix, the

namespaceURI

of the corresponding node in the

Entity

node subtree is

null

. The same is true
for

EntityReference

nodes that refer to this entity, when
they are created using the

createEntityReference

method of
the

Document

interface.

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

getInputEncoding

()

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity.

String

getNotationName

()

For unparsed entities, the name of the notation for the entity.

String

getPublicId

()

The public identifier associated with the entity if specified, and

null

otherwise.

String

getSystemId

()

The system identifier associated with the entity if specified, and

null

otherwise.

String

getXmlEncoding

()

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity.

String

getXmlVersion

()

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity.

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

getInputEncoding

()

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity.

String

getNotationName

()

For unparsed entities, the name of the notation for the entity.

String

getPublicId

()

The public identifier associated with the entity if specified, and

null

otherwise.

String

getSystemId

()

The system identifier associated with the entity if specified, and

null

otherwise.

String

getXmlEncoding

()

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity.

String

getXmlVersion

()

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity.

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

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity.

For unparsed entities, the name of the notation for the entity.

The public identifier associated with the entity if specified, and

null

otherwise.

The system identifier associated with the entity if specified, and

null

otherwise.

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity.

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity.

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

The public identifier associated with the entity if specified, and

null

otherwise.

- getSystemId

```java
String
getSystemId()
```

The system identifier associated with the entity if specified, and

null

otherwise. This may be an absolute URI or not.

- getNotationName

```java
String
getNotationName()
```

For unparsed entities, the name of the notation for the entity. For
parsed entities, this is

null

.

- getInputEncoding

```java
String
getInputEncoding()
```

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity. This is

null

if it an entity from the internal subset or if it
is not known.

**Since:** 1.5, DOM Level 3

- getXmlEncoding

```java
String
getXmlEncoding()
```

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:** 1.5, DOM Level 3

- getXmlVersion

```java
String
getXmlVersion()
```

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:** 1.5, DOM Level 3

Method Detail

- getPublicId

```java
String
getPublicId()
```

The public identifier associated with the entity if specified, and

null

otherwise.

- getSystemId

```java
String
getSystemId()
```

The system identifier associated with the entity if specified, and

null

otherwise. This may be an absolute URI or not.

- getNotationName

```java
String
getNotationName()
```

For unparsed entities, the name of the notation for the entity. For
parsed entities, this is

null

.

- getInputEncoding

```java
String
getInputEncoding()
```

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity. This is

null

if it an entity from the internal subset or if it
is not known.

**Since:** 1.5, DOM Level 3

- getXmlEncoding

```java
String
getXmlEncoding()
```

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:** 1.5, DOM Level 3

- getXmlVersion

```java
String
getXmlVersion()
```

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:** 1.5, DOM Level 3

---

#### Method Detail

getPublicId

```java
String
getPublicId()
```

The public identifier associated with the entity if specified, and

null

otherwise.

---

#### getPublicId

String

getPublicId()

The public identifier associated with the entity if specified, and

null

otherwise.

getSystemId

```java
String
getSystemId()
```

The system identifier associated with the entity if specified, and

null

otherwise. This may be an absolute URI or not.

---

#### getSystemId

String

getSystemId()

The system identifier associated with the entity if specified, and

null

otherwise. This may be an absolute URI or not.

getNotationName

```java
String
getNotationName()
```

For unparsed entities, the name of the notation for the entity. For
parsed entities, this is

null

.

---

#### getNotationName

String

getNotationName()

For unparsed entities, the name of the notation for the entity. For
parsed entities, this is

null

.

getInputEncoding

```java
String
getInputEncoding()
```

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity. This is

null

if it an entity from the internal subset or if it
is not known.

**Since:** 1.5, DOM Level 3

---

#### getInputEncoding

String

getInputEncoding()

An attribute specifying the encoding used for this entity at the time
of parsing, when it is an external parsed entity. This is

null

if it an entity from the internal subset or if it
is not known.

getXmlEncoding

```java
String
getXmlEncoding()
```

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:** 1.5, DOM Level 3

---

#### getXmlEncoding

String

getXmlEncoding()

An attribute specifying, as part of the text declaration, the encoding
of this entity, when it is an external parsed entity. This is

null

otherwise.

getXmlVersion

```java
String
getXmlVersion()
```

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity. This is

null

otherwise.

**Since:** 1.5, DOM Level 3

---

#### getXmlVersion

String

getXmlVersion()

An attribute specifying, as part of the text declaration, the version
number of this entity, when it is an external parsed entity. This is

null

otherwise.

---

