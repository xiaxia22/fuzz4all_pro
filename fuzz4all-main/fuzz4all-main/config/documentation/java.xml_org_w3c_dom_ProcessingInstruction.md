# Interface ProcessingInstruction

**Source:** `java.xml\org\w3c\dom\ProcessingInstruction.html`

### Class Description

```java
public interface
ProcessingInstruction

extends
Node
```

The

ProcessingInstruction

interface represents a "processing
instruction", used in XML as a way to keep processor-specific information
in the text of the document.

No lexical check is done on the content of a processing instruction and
it is therefore possible to have the character sequence

"?>"

in the content, which is illegal a processing
instruction per section 2.6 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

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
getTarget()

The target of this processing instruction. XML defines this as being
the first token following the markup that begins the processing
instruction.

---

#### String
getData()

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

---

#### void setData​(
String
data)
throws
DOMException

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

### Additional Sections

#### Interface ProcessingInstruction

**All Superinterfaces:** Node

```java
public interface
ProcessingInstruction

extends
Node
```

The

ProcessingInstruction

interface represents a "processing
instruction", used in XML as a way to keep processor-specific information
in the text of the document.

No lexical check is done on the content of a processing instruction and
it is therefore possible to have the character sequence

"?>"

in the content, which is illegal a processing
instruction per section 2.6 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

public interface

ProcessingInstruction

extends

Node

The

ProcessingInstruction

interface represents a "processing
instruction", used in XML as a way to keep processor-specific information
in the text of the document.

No lexical check is done on the content of a processing instruction and
it is therefore possible to have the character sequence

"?>"

in the content, which is illegal a processing
instruction per section 2.6 of [

XML 1.0

]. The
presence of this character sequence must generate a fatal error during
serialization.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

No lexical check is done on the content of a processing instruction and
it is therefore possible to have the character sequence

"?>"

in the content, which is illegal a processing
instruction per section 2.6 of [

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

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getData

()

The content of this processing instruction.

String

getTarget

()

The target of this processing instruction.

void

setData

​(

String

data)

The content of this processing instruction.

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

getData

()

The content of this processing instruction.

String

getTarget

()

The target of this processing instruction.

void

setData

​(

String

data)

The content of this processing instruction.

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

The content of this processing instruction.

The target of this processing instruction.

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

- getTarget

```java
String
getTarget()
```

The target of this processing instruction. XML defines this as being
the first token following the markup that begins the processing
instruction.

- getData

```java
String
getData()
```

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

- setData

```java
void setData​(
String
data)
throws
DOMException
```

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

Method Detail

- getTarget

```java
String
getTarget()
```

The target of this processing instruction. XML defines this as being
the first token following the markup that begins the processing
instruction.

- getData

```java
String
getData()
```

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

- setData

```java
void setData​(
String
data)
throws
DOMException
```

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

#### Method Detail

getTarget

```java
String
getTarget()
```

The target of this processing instruction. XML defines this as being
the first token following the markup that begins the processing
instruction.

---

#### getTarget

String

getTarget()

The target of this processing instruction. XML defines this as being
the first token following the markup that begins the processing
instruction.

getData

```java
String
getData()
```

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

---

#### getData

String

getData()

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

setData

```java
void setData​(
String
data)
throws
DOMException
```

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

---

#### setData

void setData​(

String

data)
throws

DOMException

The content of this processing instruction. This is from the first non
white space character after the target to the character immediately
preceding the

?>

.

---

