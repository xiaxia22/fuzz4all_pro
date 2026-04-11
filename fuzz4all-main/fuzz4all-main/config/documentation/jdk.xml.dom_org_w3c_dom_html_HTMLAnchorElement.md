# Interface HTMLAnchorElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLAnchorElement.html`

### Class Description

```java
public interface
HTMLAnchorElement

extends
HTMLElement
```

The anchor element. See the A element definition in HTML 4.0.

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
getAccessKey()

A single character access key to give access to the form control. See
the accesskey attribute definition in HTML 4.0.

---

#### void setAccessKey​(
String
accessKey)

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

#### String
getCoords()

Comma-separated list of lengths, defining an active region geometry.
See also

shape

for the shape of the region. See the
coords attribute definition in HTML 4.0.

---

#### void setCoords​(
String
coords)

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
getName()

Anchor name. See the name attribute definition in HTML 4.0.

---

#### void setName​(
String
name)

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
getShape()

The shape of the active area. The coordinates are given by

coords

. See the shape attribute definition in HTML 4.0.

---

#### void setShape​(
String
shape)

*No description found.*

---

#### int getTabIndex()

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

---

#### void setTabIndex​(int tabIndex)

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

#### void blur()

Removes keyboard focus from this element.

---

#### void focus()

Gives keyboard focus to this element.

---

### Additional Sections

#### Interface HTMLAnchorElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLAnchorElement

extends
HTMLElement
```

The anchor element. See the A element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLAnchorElement

extends

HTMLElement

The anchor element. See the A element definition in HTML 4.0.

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

void

blur

()

Removes keyboard focus from this element.

void

focus

()

Gives keyboard focus to this element.

String

getAccessKey

()

A single character access key to give access to the form control.

String

getCharset

()

The character encoding of the linked resource.

String

getCoords

()

Comma-separated list of lengths, defining an active region geometry.

String

getHref

()

The URI of the linked resource.

String

getHreflang

()

Language code of the linked resource.

String

getName

()

Anchor name.

String

getRel

()

Forward link type.

String

getRev

()

Reverse link type.

String

getShape

()

The shape of the active area.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getTarget

()

Frame to render the resource in.

String

getType

()

Advisory content type.

void

setAccessKey

​(

String

accessKey)

void

setCharset

​(

String

charset)

void

setCoords

​(

String

coords)

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

setName

​(

String

name)

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

setShape

​(

String

shape)

void

setTabIndex

​(int tabIndex)

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

void

blur

()

Removes keyboard focus from this element.

void

focus

()

Gives keyboard focus to this element.

String

getAccessKey

()

A single character access key to give access to the form control.

String

getCharset

()

The character encoding of the linked resource.

String

getCoords

()

Comma-separated list of lengths, defining an active region geometry.

String

getHref

()

The URI of the linked resource.

String

getHreflang

()

Language code of the linked resource.

String

getName

()

Anchor name.

String

getRel

()

Forward link type.

String

getRev

()

Reverse link type.

String

getShape

()

The shape of the active area.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getTarget

()

Frame to render the resource in.

String

getType

()

Advisory content type.

void

setAccessKey

​(

String

accessKey)

void

setCharset

​(

String

charset)

void

setCoords

​(

String

coords)

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

setName

​(

String

name)

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

setShape

​(

String

shape)

void

setTabIndex

​(int tabIndex)

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

Removes keyboard focus from this element.

Gives keyboard focus to this element.

A single character access key to give access to the form control.

The character encoding of the linked resource.

Comma-separated list of lengths, defining an active region geometry.

The URI of the linked resource.

Language code of the linked resource.

Anchor name.

Forward link type.

Reverse link type.

The shape of the active area.

Index that represents the element's position in the tabbing order.

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

- getAccessKey

```java
String
getAccessKey()
```

A single character access key to give access to the form control. See
the accesskey attribute definition in HTML 4.0.

- setAccessKey

```java
void setAccessKey​(
String
accessKey)
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

- getCoords

```java
String
getCoords()
```

Comma-separated list of lengths, defining an active region geometry.
See also

shape

for the shape of the region. See the
coords attribute definition in HTML 4.0.

- setCoords

```java
void setCoords​(
String
coords)
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

- getName

```java
String
getName()
```

Anchor name. See the name attribute definition in HTML 4.0.

- setName

```java
void setName​(
String
name)
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

- getShape

```java
String
getShape()
```

The shape of the active area. The coordinates are given by

coords

. See the shape attribute definition in HTML 4.0.

- setShape

```java
void setShape​(
String
shape)
```

- getTabIndex

```java
int getTabIndex()
```

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

- setTabIndex

```java
void setTabIndex​(int tabIndex)
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

- blur

```java
void blur()
```

Removes keyboard focus from this element.

- focus

```java
void focus()
```

Gives keyboard focus to this element.

Method Detail

- getAccessKey

```java
String
getAccessKey()
```

A single character access key to give access to the form control. See
the accesskey attribute definition in HTML 4.0.

- setAccessKey

```java
void setAccessKey​(
String
accessKey)
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

- getCoords

```java
String
getCoords()
```

Comma-separated list of lengths, defining an active region geometry.
See also

shape

for the shape of the region. See the
coords attribute definition in HTML 4.0.

- setCoords

```java
void setCoords​(
String
coords)
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

- getName

```java
String
getName()
```

Anchor name. See the name attribute definition in HTML 4.0.

- setName

```java
void setName​(
String
name)
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

- getShape

```java
String
getShape()
```

The shape of the active area. The coordinates are given by

coords

. See the shape attribute definition in HTML 4.0.

- setShape

```java
void setShape​(
String
shape)
```

- getTabIndex

```java
int getTabIndex()
```

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

- setTabIndex

```java
void setTabIndex​(int tabIndex)
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

- blur

```java
void blur()
```

Removes keyboard focus from this element.

- focus

```java
void focus()
```

Gives keyboard focus to this element.

---

#### Method Detail

getAccessKey

```java
String
getAccessKey()
```

A single character access key to give access to the form control. See
the accesskey attribute definition in HTML 4.0.

---

#### getAccessKey

String

getAccessKey()

A single character access key to give access to the form control. See
the accesskey attribute definition in HTML 4.0.

setAccessKey

```java
void setAccessKey​(
String
accessKey)
```

---

#### setAccessKey

void setAccessKey​(

String

accessKey)

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

getCoords

```java
String
getCoords()
```

Comma-separated list of lengths, defining an active region geometry.
See also

shape

for the shape of the region. See the
coords attribute definition in HTML 4.0.

---

#### getCoords

String

getCoords()

Comma-separated list of lengths, defining an active region geometry.
See also

shape

for the shape of the region. See the
coords attribute definition in HTML 4.0.

setCoords

```java
void setCoords​(
String
coords)
```

---

#### setCoords

void setCoords​(

String

coords)

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

getName

```java
String
getName()
```

Anchor name. See the name attribute definition in HTML 4.0.

---

#### getName

String

getName()

Anchor name. See the name attribute definition in HTML 4.0.

setName

```java
void setName​(
String
name)
```

---

#### setName

void setName​(

String

name)

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

getShape

```java
String
getShape()
```

The shape of the active area. The coordinates are given by

coords

. See the shape attribute definition in HTML 4.0.

---

#### getShape

String

getShape()

The shape of the active area. The coordinates are given by

coords

. See the shape attribute definition in HTML 4.0.

setShape

```java
void setShape​(
String
shape)
```

---

#### setShape

void setShape​(

String

shape)

getTabIndex

```java
int getTabIndex()
```

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

---

#### getTabIndex

int getTabIndex()

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

setTabIndex

```java
void setTabIndex​(int tabIndex)
```

---

#### setTabIndex

void setTabIndex​(int tabIndex)

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

blur

```java
void blur()
```

Removes keyboard focus from this element.

---

#### blur

void blur()

Removes keyboard focus from this element.

focus

```java
void focus()
```

Gives keyboard focus to this element.

---

#### focus

void focus()

Gives keyboard focus to this element.

---

