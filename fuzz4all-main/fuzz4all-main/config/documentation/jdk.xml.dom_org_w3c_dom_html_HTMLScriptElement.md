# Interface HTMLScriptElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLScriptElement.html`

### Class Description

```java
public interface
HTMLScriptElement

extends
HTMLElement
```

Script statements. See the SCRIPT element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**All Superinterfaces:** Element

,

HTMLElement

,

Node

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getText()

The script content of the element.

---

#### void setText​(
String
text)

*No description found.*

---

#### String
getHtmlFor()

Reserved for future use.

---

#### void setHtmlFor​(
String
htmlFor)

*No description found.*

---

#### String
getEvent()

Reserved for future use.

---

#### void setEvent​(
String
event)

*No description found.*

---

#### String
getCharset()

The character encoding of the linked resource. See the charset
attribute definition in HTML 4.0.

---

#### void setCharset​(
String
charset)

*No description found.*

---

#### boolean getDefer()

Indicates that the user agent can defer processing of the script. See
the defer attribute definition in HTML 4.0.

---

#### void setDefer​(boolean defer)

*No description found.*

---

#### String
getSrc()

URI designating an external script. See the src attribute definition
in HTML 4.0.

---

#### void setSrc​(
String
src)

*No description found.*

---

#### String
getType()

The content type of the script language. See the type attribute
definition in HTML 4.0.

---

#### void setType​(
String
type)

*No description found.*

---

### Additional Sections

#### Interface HTMLScriptElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLScriptElement

extends
HTMLElement
```

Script statements. See the SCRIPT element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLScriptElement

extends

HTMLElement

Script statements. See the SCRIPT element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

See also the

Document Object Model (DOM) Level 2 Specification

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

getCharset

()

The character encoding of the linked resource.

boolean

getDefer

()

Indicates that the user agent can defer processing of the script.

String

getEvent

()

Reserved for future use.

String

getHtmlFor

()

Reserved for future use.

String

getSrc

()

URI designating an external script.

String

getText

()

The script content of the element.

String

getType

()

The content type of the script language.

void

setCharset

​(

String

charset)

void

setDefer

​(boolean defer)

void

setEvent

​(

String

event)

void

setHtmlFor

​(

String

htmlFor)

void

setSrc

​(

String

src)

void

setText

​(

String

text)

void

setType

​(

String

type)

- Methods declared in interface org.w3c.dom.

Element

getAttribute

,

getAttributeNode

,

getAttributeNodeNS

,

getAttributeNS

,

getElementsByTagName

,

getElementsByTagNameNS

,

getSchemaTypeInfo

,

getTagName

,

hasAttribute

,

hasAttributeNS

,

removeAttribute

,

removeAttributeNode

,

removeAttributeNS

,

setAttribute

,

setAttributeNode

,

setAttributeNodeNS

,

setAttributeNS

,

setIdAttribute

,

setIdAttributeNode

,

setIdAttributeNS

- Methods declared in interface org.w3c.dom.html.

HTMLElement

getClassName

,

getDir

,

getId

,

getLang

,

getTitle

,

setClassName

,

setDir

,

setId

,

setLang

,

setTitle

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

getCharset

()

The character encoding of the linked resource.

boolean

getDefer

()

Indicates that the user agent can defer processing of the script.

String

getEvent

()

Reserved for future use.

String

getHtmlFor

()

Reserved for future use.

String

getSrc

()

URI designating an external script.

String

getText

()

The script content of the element.

String

getType

()

The content type of the script language.

void

setCharset

​(

String

charset)

void

setDefer

​(boolean defer)

void

setEvent

​(

String

event)

void

setHtmlFor

​(

String

htmlFor)

void

setSrc

​(

String

src)

void

setText

​(

String

text)

void

setType

​(

String

type)

- Methods declared in interface org.w3c.dom.

Element

getAttribute

,

getAttributeNode

,

getAttributeNodeNS

,

getAttributeNS

,

getElementsByTagName

,

getElementsByTagNameNS

,

getSchemaTypeInfo

,

getTagName

,

hasAttribute

,

hasAttributeNS

,

removeAttribute

,

removeAttributeNode

,

removeAttributeNS

,

setAttribute

,

setAttributeNode

,

setAttributeNodeNS

,

setAttributeNS

,

setIdAttribute

,

setIdAttributeNode

,

setIdAttributeNS

- Methods declared in interface org.w3c.dom.html.

HTMLElement

getClassName

,

getDir

,

getId

,

getLang

,

getTitle

,

setClassName

,

setDir

,

setId

,

setLang

,

setTitle

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

The character encoding of the linked resource.

Indicates that the user agent can defer processing of the script.

Reserved for future use.

URI designating an external script.

The script content of the element.

The content type of the script language.

Methods declared in interface org.w3c.dom.

Element

getAttribute

,

getAttributeNode

,

getAttributeNodeNS

,

getAttributeNS

,

getElementsByTagName

,

getElementsByTagNameNS

,

getSchemaTypeInfo

,

getTagName

,

hasAttribute

,

hasAttributeNS

,

removeAttribute

,

removeAttributeNode

,

removeAttributeNS

,

setAttribute

,

setAttributeNode

,

setAttributeNodeNS

,

setAttributeNS

,

setIdAttribute

,

setIdAttributeNode

,

setIdAttributeNS

---

#### Methods declared in interface org.w3c.dom. Element

Methods declared in interface org.w3c.dom.html.

HTMLElement

getClassName

,

getDir

,

getId

,

getLang

,

getTitle

,

setClassName

,

setDir

,

setId

,

setLang

,

setTitle

---

#### Methods declared in interface org.w3c.dom.html. HTMLElement

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

- getText

```java
String
getText()
```

The script content of the element.

- setText

```java
void setText​(
String
text)
```

- getHtmlFor

```java
String
getHtmlFor()
```

Reserved for future use.

- setHtmlFor

```java
void setHtmlFor​(
String
htmlFor)
```

- getEvent

```java
String
getEvent()
```

Reserved for future use.

- setEvent

```java
void setEvent​(
String
event)
```

- getCharset

```java
String
getCharset()
```

The character encoding of the linked resource. See the charset
attribute definition in HTML 4.0.

- setCharset

```java
void setCharset​(
String
charset)
```

- getDefer

```java
boolean getDefer()
```

Indicates that the user agent can defer processing of the script. See
the defer attribute definition in HTML 4.0.

- setDefer

```java
void setDefer​(boolean defer)
```

- getSrc

```java
String
getSrc()
```

URI designating an external script. See the src attribute definition
in HTML 4.0.

- setSrc

```java
void setSrc​(
String
src)
```

- getType

```java
String
getType()
```

The content type of the script language. See the type attribute
definition in HTML 4.0.

- setType

```java
void setType​(
String
type)
```

Method Detail

- getText

```java
String
getText()
```

The script content of the element.

- setText

```java
void setText​(
String
text)
```

- getHtmlFor

```java
String
getHtmlFor()
```

Reserved for future use.

- setHtmlFor

```java
void setHtmlFor​(
String
htmlFor)
```

- getEvent

```java
String
getEvent()
```

Reserved for future use.

- setEvent

```java
void setEvent​(
String
event)
```

- getCharset

```java
String
getCharset()
```

The character encoding of the linked resource. See the charset
attribute definition in HTML 4.0.

- setCharset

```java
void setCharset​(
String
charset)
```

- getDefer

```java
boolean getDefer()
```

Indicates that the user agent can defer processing of the script. See
the defer attribute definition in HTML 4.0.

- setDefer

```java
void setDefer​(boolean defer)
```

- getSrc

```java
String
getSrc()
```

URI designating an external script. See the src attribute definition
in HTML 4.0.

- setSrc

```java
void setSrc​(
String
src)
```

- getType

```java
String
getType()
```

The content type of the script language. See the type attribute
definition in HTML 4.0.

- setType

```java
void setType​(
String
type)
```

---

#### Method Detail

getText

```java
String
getText()
```

The script content of the element.

---

#### getText

String

getText()

The script content of the element.

setText

```java
void setText​(
String
text)
```

---

#### setText

void setText​(

String

text)

getHtmlFor

```java
String
getHtmlFor()
```

Reserved for future use.

---

#### getHtmlFor

String

getHtmlFor()

Reserved for future use.

setHtmlFor

```java
void setHtmlFor​(
String
htmlFor)
```

---

#### setHtmlFor

void setHtmlFor​(

String

htmlFor)

getEvent

```java
String
getEvent()
```

Reserved for future use.

---

#### getEvent

String

getEvent()

Reserved for future use.

setEvent

```java
void setEvent​(
String
event)
```

---

#### setEvent

void setEvent​(

String

event)

getCharset

```java
String
getCharset()
```

The character encoding of the linked resource. See the charset
attribute definition in HTML 4.0.

---

#### getCharset

String

getCharset()

The character encoding of the linked resource. See the charset
attribute definition in HTML 4.0.

setCharset

```java
void setCharset​(
String
charset)
```

---

#### setCharset

void setCharset​(

String

charset)

getDefer

```java
boolean getDefer()
```

Indicates that the user agent can defer processing of the script. See
the defer attribute definition in HTML 4.0.

---

#### getDefer

boolean getDefer()

Indicates that the user agent can defer processing of the script. See
the defer attribute definition in HTML 4.0.

setDefer

```java
void setDefer​(boolean defer)
```

---

#### setDefer

void setDefer​(boolean defer)

getSrc

```java
String
getSrc()
```

URI designating an external script. See the src attribute definition
in HTML 4.0.

---

#### getSrc

String

getSrc()

URI designating an external script. See the src attribute definition
in HTML 4.0.

setSrc

```java
void setSrc​(
String
src)
```

---

#### setSrc

void setSrc​(

String

src)

getType

```java
String
getType()
```

The content type of the script language. See the type attribute
definition in HTML 4.0.

---

#### getType

String

getType()

The content type of the script language. See the type attribute
definition in HTML 4.0.

setType

```java
void setType​(
String
type)
```

---

#### setType

void setType​(

String

type)

---

