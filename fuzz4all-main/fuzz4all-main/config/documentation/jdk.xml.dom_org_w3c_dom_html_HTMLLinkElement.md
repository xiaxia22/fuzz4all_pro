# Interface HTMLLinkElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLLinkElement.html`

### Class Description

```java
public interface
HTMLLinkElement

extends
HTMLElement
```

The

LINK

element specifies a link to an external resource,
and defines this document's relationship to that resource (or vice versa).
See the LINK element definition in HTML 4.0 (see also the

LinkStyle

interface in the module).

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

#### boolean getDisabled()

Enables/disables the link. This is currently only used for style sheet
links, and may be used to activate or deactivate style sheets.

---

#### void setDisabled​(boolean disabled)

*No description found.*

---

#### String
getCharset()

The character encoding of the resource being linked to. See the
charset attribute definition in HTML 4.0.

---

#### void setCharset​(
String
charset)

*No description found.*

---

#### String
getHref()

The URI of the linked resource. See the href attribute definition in
HTML 4.0.

---

#### void setHref​(
String
href)

*No description found.*

---

#### String
getHreflang()

Language code of the linked resource. See the hreflang attribute
definition in HTML 4.0.

---

#### void setHreflang​(
String
hreflang)

*No description found.*

---

#### String
getMedia()

Designed for use with one or more target media. See the media
attribute definition in HTML 4.0.

---

#### void setMedia​(
String
media)

*No description found.*

---

#### String
getRel()

Forward link type. See the rel attribute definition in HTML 4.0.

---

#### void setRel​(
String
rel)

*No description found.*

---

#### String
getRev()

Reverse link type. See the rev attribute definition in HTML 4.0.

---

#### void setRev​(
String
rev)

*No description found.*

---

#### String
getTarget()

Frame to render the resource in. See the target attribute definition
in HTML 4.0.

---

#### void setTarget​(
String
target)

*No description found.*

---

#### String
getType()

Advisory content type. See the type attribute definition in HTML 4.0.

---

#### void setType​(
String
type)

*No description found.*

---

### Additional Sections

#### Interface HTMLLinkElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLLinkElement

extends
HTMLElement
```

The

LINK

element specifies a link to an external resource,
and defines this document's relationship to that resource (or vice versa).
See the LINK element definition in HTML 4.0 (see also the

LinkStyle

interface in the module).

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLLinkElement

extends

HTMLElement

The

LINK

element specifies a link to an external resource,
and defines this document's relationship to that resource (or vice versa).
See the LINK element definition in HTML 4.0 (see also the

LinkStyle

interface in the module).

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

The character encoding of the resource being linked to.

boolean

getDisabled

()

Enables/disables the link.

String

getHref

()

The URI of the linked resource.

String

getHreflang

()

Language code of the linked resource.

String

getMedia

()

Designed for use with one or more target media.

String

getRel

()

Forward link type.

String

getRev

()

Reverse link type.

String

getTarget

()

Frame to render the resource in.

String

getType

()

Advisory content type.

void

setCharset

​(

String

charset)

void

setDisabled

​(boolean disabled)

void

setHref

​(

String

href)

void

setHreflang

​(

String

hreflang)

void

setMedia

​(

String

media)

void

setRel

​(

String

rel)

void

setRev

​(

String

rev)

void

setTarget

​(

String

target)

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

The character encoding of the resource being linked to.

boolean

getDisabled

()

Enables/disables the link.

String

getHref

()

The URI of the linked resource.

String

getHreflang

()

Language code of the linked resource.

String

getMedia

()

Designed for use with one or more target media.

String

getRel

()

Forward link type.

String

getRev

()

Reverse link type.

String

getTarget

()

Frame to render the resource in.

String

getType

()

Advisory content type.

void

setCharset

​(

String

charset)

void

setDisabled

​(boolean disabled)

void

setHref

​(

String

href)

void

setHreflang

​(

String

hreflang)

void

setMedia

​(

String

media)

void

setRel

​(

String

rel)

void

setRev

​(

String

rev)

void

setTarget

​(

String

target)

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

The character encoding of the resource being linked to.

Enables/disables the link.

The URI of the linked resource.

Language code of the linked resource.

Designed for use with one or more target media.

Forward link type.

Reverse link type.

Frame to render the resource in.

Advisory content type.

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

- getDisabled

```java
boolean getDisabled()
```

Enables/disables the link. This is currently only used for style sheet
links, and may be used to activate or deactivate style sheets.

- setDisabled

```java
void setDisabled​(boolean disabled)
```

- getCharset

```java
String
getCharset()
```

The character encoding of the resource being linked to. See the
charset attribute definition in HTML 4.0.

- setCharset

```java
void setCharset​(
String
charset)
```

- getHref

```java
String
getHref()
```

The URI of the linked resource. See the href attribute definition in
HTML 4.0.

- setHref

```java
void setHref​(
String
href)
```

- getHreflang

```java
String
getHreflang()
```

Language code of the linked resource. See the hreflang attribute
definition in HTML 4.0.

- setHreflang

```java
void setHreflang​(
String
hreflang)
```

- getMedia

```java
String
getMedia()
```

Designed for use with one or more target media. See the media
attribute definition in HTML 4.0.

- setMedia

```java
void setMedia​(
String
media)
```

- getRel

```java
String
getRel()
```

Forward link type. See the rel attribute definition in HTML 4.0.

- setRel

```java
void setRel​(
String
rel)
```

- getRev

```java
String
getRev()
```

Reverse link type. See the rev attribute definition in HTML 4.0.

- setRev

```java
void setRev​(
String
rev)
```

- getTarget

```java
String
getTarget()
```

Frame to render the resource in. See the target attribute definition
in HTML 4.0.

- setTarget

```java
void setTarget​(
String
target)
```

- getType

```java
String
getType()
```

Advisory content type. See the type attribute definition in HTML 4.0.

- setType

```java
void setType​(
String
type)
```

Method Detail

- getDisabled

```java
boolean getDisabled()
```

Enables/disables the link. This is currently only used for style sheet
links, and may be used to activate or deactivate style sheets.

- setDisabled

```java
void setDisabled​(boolean disabled)
```

- getCharset

```java
String
getCharset()
```

The character encoding of the resource being linked to. See the
charset attribute definition in HTML 4.0.

- setCharset

```java
void setCharset​(
String
charset)
```

- getHref

```java
String
getHref()
```

The URI of the linked resource. See the href attribute definition in
HTML 4.0.

- setHref

```java
void setHref​(
String
href)
```

- getHreflang

```java
String
getHreflang()
```

Language code of the linked resource. See the hreflang attribute
definition in HTML 4.0.

- setHreflang

```java
void setHreflang​(
String
hreflang)
```

- getMedia

```java
String
getMedia()
```

Designed for use with one or more target media. See the media
attribute definition in HTML 4.0.

- setMedia

```java
void setMedia​(
String
media)
```

- getRel

```java
String
getRel()
```

Forward link type. See the rel attribute definition in HTML 4.0.

- setRel

```java
void setRel​(
String
rel)
```

- getRev

```java
String
getRev()
```

Reverse link type. See the rev attribute definition in HTML 4.0.

- setRev

```java
void setRev​(
String
rev)
```

- getTarget

```java
String
getTarget()
```

Frame to render the resource in. See the target attribute definition
in HTML 4.0.

- setTarget

```java
void setTarget​(
String
target)
```

- getType

```java
String
getType()
```

Advisory content type. See the type attribute definition in HTML 4.0.

- setType

```java
void setType​(
String
type)
```

---

#### Method Detail

getDisabled

```java
boolean getDisabled()
```

Enables/disables the link. This is currently only used for style sheet
links, and may be used to activate or deactivate style sheets.

---

#### getDisabled

boolean getDisabled()

Enables/disables the link. This is currently only used for style sheet
links, and may be used to activate or deactivate style sheets.

setDisabled

```java
void setDisabled​(boolean disabled)
```

---

#### setDisabled

void setDisabled​(boolean disabled)

getCharset

```java
String
getCharset()
```

The character encoding of the resource being linked to. See the
charset attribute definition in HTML 4.0.

---

#### getCharset

String

getCharset()

The character encoding of the resource being linked to. See the
charset attribute definition in HTML 4.0.

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

getHref

```java
String
getHref()
```

The URI of the linked resource. See the href attribute definition in
HTML 4.0.

---

#### getHref

String

getHref()

The URI of the linked resource. See the href attribute definition in
HTML 4.0.

setHref

```java
void setHref​(
String
href)
```

---

#### setHref

void setHref​(

String

href)

getHreflang

```java
String
getHreflang()
```

Language code of the linked resource. See the hreflang attribute
definition in HTML 4.0.

---

#### getHreflang

String

getHreflang()

Language code of the linked resource. See the hreflang attribute
definition in HTML 4.0.

setHreflang

```java
void setHreflang​(
String
hreflang)
```

---

#### setHreflang

void setHreflang​(

String

hreflang)

getMedia

```java
String
getMedia()
```

Designed for use with one or more target media. See the media
attribute definition in HTML 4.0.

---

#### getMedia

String

getMedia()

Designed for use with one or more target media. See the media
attribute definition in HTML 4.0.

setMedia

```java
void setMedia​(
String
media)
```

---

#### setMedia

void setMedia​(

String

media)

getRel

```java
String
getRel()
```

Forward link type. See the rel attribute definition in HTML 4.0.

---

#### getRel

String

getRel()

Forward link type. See the rel attribute definition in HTML 4.0.

setRel

```java
void setRel​(
String
rel)
```

---

#### setRel

void setRel​(

String

rel)

getRev

```java
String
getRev()
```

Reverse link type. See the rev attribute definition in HTML 4.0.

---

#### getRev

String

getRev()

Reverse link type. See the rev attribute definition in HTML 4.0.

setRev

```java
void setRev​(
String
rev)
```

---

#### setRev

void setRev​(

String

rev)

getTarget

```java
String
getTarget()
```

Frame to render the resource in. See the target attribute definition
in HTML 4.0.

---

#### getTarget

String

getTarget()

Frame to render the resource in. See the target attribute definition
in HTML 4.0.

setTarget

```java
void setTarget​(
String
target)
```

---

#### setTarget

void setTarget​(

String

target)

getType

```java
String
getType()
```

Advisory content type. See the type attribute definition in HTML 4.0.

---

#### getType

String

getType()

Advisory content type. See the type attribute definition in HTML 4.0.

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

