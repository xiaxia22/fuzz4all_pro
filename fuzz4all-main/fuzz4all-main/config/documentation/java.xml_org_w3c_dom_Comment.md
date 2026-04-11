# Interface Comment

**Source:** `java.xml\org\w3c\dom\Comment.html`

### Class Description

```java
public interface
Comment

extends
CharacterData
```

This interface inherits from

CharacterData

and represents the
content of a comment, i.e., all the characters between the starting
'

<!--

' and ending '

-->

'. Note that this is
the definition of a comment in XML, and, in practice, HTML, although some
HTML tools may implement the full SGML comment structure.

No lexical check is done on the content of a comment and it is
therefore possible to have the character sequence

"--"

(double-hyphen) in the content, which is illegal in a comment per section
2.5 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**All Superinterfaces:** CharacterData

,

Node

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface Comment

**All Superinterfaces:** CharacterData

,

Node

```java
public interface
Comment

extends
CharacterData
```

This interface inherits from

CharacterData

and represents the
content of a comment, i.e., all the characters between the starting
'

<!--

' and ending '

-->

'. Note that this is
the definition of a comment in XML, and, in practice, HTML, although some
HTML tools may implement the full SGML comment structure.

No lexical check is done on the content of a comment and it is
therefore possible to have the character sequence

"--"

(double-hyphen) in the content, which is illegal in a comment per section
2.5 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

Comment

extends

CharacterData

This interface inherits from

CharacterData

and represents the
content of a comment, i.e., all the characters between the starting
'

<!--

' and ending '

-->

'. Note that this is
the definition of a comment in XML, and, in practice, HTML, although some
HTML tools may implement the full SGML comment structure.

No lexical check is done on the content of a comment and it is
therefore possible to have the character sequence

"--"

(double-hyphen) in the content, which is illegal in a comment per section
2.5 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

No lexical check is done on the content of a comment and it is
therefore possible to have the character sequence

"--"

(double-hyphen) in the content, which is illegal in a comment per section
2.5 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

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

CharacterData

appendData

,

deleteData

,

getData

,

getLength

,

insertData

,

replaceData

,

setData

,

substringData

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

CharacterData

appendData

,

deleteData

,

getData

,

getLength

,

insertData

,

replaceData

,

setData

,

substringData

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

CharacterData

appendData

,

deleteData

,

getData

,

getLength

,

insertData

,

replaceData

,

setData

,

substringData

---

#### Methods declared in interface org.w3c.dom. CharacterData

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

