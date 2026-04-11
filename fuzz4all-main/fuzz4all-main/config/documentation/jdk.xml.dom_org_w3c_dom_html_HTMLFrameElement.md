# Interface HTMLFrameElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLFrameElement.html`

### Class Description

```java
public interface
HTMLFrameElement

extends
HTMLElement
```

Create a frame. See the FRAME element definition in HTML 4.0.

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
getFrameBorder()

Request frame borders. See the frameborder attribute definition in
HTML 4.0.

---

#### void setFrameBorder​(
String
frameBorder)

*No description found.*

---

#### String
getLongDesc()

URI designating a long description of this image or frame. See the
longdesc attribute definition in HTML 4.0.

---

#### void setLongDesc​(
String
longDesc)

*No description found.*

---

#### String
getMarginHeight()

Frame margin height, in pixels. See the marginheight attribute
definition in HTML 4.0.

---

#### void setMarginHeight​(
String
marginHeight)

*No description found.*

---

#### String
getMarginWidth()

Frame margin width, in pixels. See the marginwidth attribute
definition in HTML 4.0.

---

#### void setMarginWidth​(
String
marginWidth)

*No description found.*

---

#### String
getName()

The frame name (object of the

target

attribute). See the
name attribute definition in HTML 4.0.

---

#### void setName​(
String
name)

*No description found.*

---

#### boolean getNoResize()

When true, forbid user from resizing frame. See the noresize
attribute definition in HTML 4.0.

---

#### void setNoResize​(boolean noResize)

*No description found.*

---

#### String
getScrolling()

Specify whether or not the frame should have scrollbars. See the
scrolling attribute definition in HTML 4.0.

---

#### void setScrolling​(
String
scrolling)

*No description found.*

---

#### String
getSrc()

A URI designating the initial frame contents. See the src attribute
definition in HTML 4.0.

---

#### void setSrc​(
String
src)

*No description found.*

---

#### Document
getContentDocument()

The document this frame contains, if there is any and it is available,
or

null

otherwise.

**Since:**
- 1.4, DOM Level 2

---

### Additional Sections

#### Interface HTMLFrameElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLFrameElement

extends
HTMLElement
```

Create a frame. See the FRAME element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLFrameElement

extends

HTMLElement

Create a frame. See the FRAME element definition in HTML 4.0.

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

Document

getContentDocument

()

The document this frame contains, if there is any and it is available,
or

null

otherwise.

String

getFrameBorder

()

Request frame borders.

String

getLongDesc

()

URI designating a long description of this image or frame.

String

getMarginHeight

()

Frame margin height, in pixels.

String

getMarginWidth

()

Frame margin width, in pixels.

String

getName

()

The frame name (object of the

target

attribute).

boolean

getNoResize

()

When true, forbid user from resizing frame.

String

getScrolling

()

Specify whether or not the frame should have scrollbars.

String

getSrc

()

A URI designating the initial frame contents.

void

setFrameBorder

​(

String

frameBorder)

void

setLongDesc

​(

String

longDesc)

void

setMarginHeight

​(

String

marginHeight)

void

setMarginWidth

​(

String

marginWidth)

void

setName

​(

String

name)

void

setNoResize

​(boolean noResize)

void

setScrolling

​(

String

scrolling)

void

setSrc

​(

String

src)

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

Document

getContentDocument

()

The document this frame contains, if there is any and it is available,
or

null

otherwise.

String

getFrameBorder

()

Request frame borders.

String

getLongDesc

()

URI designating a long description of this image or frame.

String

getMarginHeight

()

Frame margin height, in pixels.

String

getMarginWidth

()

Frame margin width, in pixels.

String

getName

()

The frame name (object of the

target

attribute).

boolean

getNoResize

()

When true, forbid user from resizing frame.

String

getScrolling

()

Specify whether or not the frame should have scrollbars.

String

getSrc

()

A URI designating the initial frame contents.

void

setFrameBorder

​(

String

frameBorder)

void

setLongDesc

​(

String

longDesc)

void

setMarginHeight

​(

String

marginHeight)

void

setMarginWidth

​(

String

marginWidth)

void

setName

​(

String

name)

void

setNoResize

​(boolean noResize)

void

setScrolling

​(

String

scrolling)

void

setSrc

​(

String

src)

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

The document this frame contains, if there is any and it is available,
or

null

otherwise.

Request frame borders.

URI designating a long description of this image or frame.

Frame margin height, in pixels.

Frame margin width, in pixels.

The frame name (object of the

target

attribute).

When true, forbid user from resizing frame.

Specify whether or not the frame should have scrollbars.

A URI designating the initial frame contents.

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

- getFrameBorder

```java
String
getFrameBorder()
```

Request frame borders. See the frameborder attribute definition in
HTML 4.0.

- setFrameBorder

```java
void setFrameBorder​(
String
frameBorder)
```

- getLongDesc

```java
String
getLongDesc()
```

URI designating a long description of this image or frame. See the
longdesc attribute definition in HTML 4.0.

- setLongDesc

```java
void setLongDesc​(
String
longDesc)
```

- getMarginHeight

```java
String
getMarginHeight()
```

Frame margin height, in pixels. See the marginheight attribute
definition in HTML 4.0.

- setMarginHeight

```java
void setMarginHeight​(
String
marginHeight)
```

- getMarginWidth

```java
String
getMarginWidth()
```

Frame margin width, in pixels. See the marginwidth attribute
definition in HTML 4.0.

- setMarginWidth

```java
void setMarginWidth​(
String
marginWidth)
```

- getName

```java
String
getName()
```

The frame name (object of the

target

attribute). See the
name attribute definition in HTML 4.0.

- setName

```java
void setName​(
String
name)
```

- getNoResize

```java
boolean getNoResize()
```

When true, forbid user from resizing frame. See the noresize
attribute definition in HTML 4.0.

- setNoResize

```java
void setNoResize​(boolean noResize)
```

- getScrolling

```java
String
getScrolling()
```

Specify whether or not the frame should have scrollbars. See the
scrolling attribute definition in HTML 4.0.

- setScrolling

```java
void setScrolling​(
String
scrolling)
```

- getSrc

```java
String
getSrc()
```

A URI designating the initial frame contents. See the src attribute
definition in HTML 4.0.

- setSrc

```java
void setSrc​(
String
src)
```

- getContentDocument

```java
Document
getContentDocument()
```

The document this frame contains, if there is any and it is available,
or

null

otherwise.

**Since:** 1.4, DOM Level 2

Method Detail

- getFrameBorder

```java
String
getFrameBorder()
```

Request frame borders. See the frameborder attribute definition in
HTML 4.0.

- setFrameBorder

```java
void setFrameBorder​(
String
frameBorder)
```

- getLongDesc

```java
String
getLongDesc()
```

URI designating a long description of this image or frame. See the
longdesc attribute definition in HTML 4.0.

- setLongDesc

```java
void setLongDesc​(
String
longDesc)
```

- getMarginHeight

```java
String
getMarginHeight()
```

Frame margin height, in pixels. See the marginheight attribute
definition in HTML 4.0.

- setMarginHeight

```java
void setMarginHeight​(
String
marginHeight)
```

- getMarginWidth

```java
String
getMarginWidth()
```

Frame margin width, in pixels. See the marginwidth attribute
definition in HTML 4.0.

- setMarginWidth

```java
void setMarginWidth​(
String
marginWidth)
```

- getName

```java
String
getName()
```

The frame name (object of the

target

attribute). See the
name attribute definition in HTML 4.0.

- setName

```java
void setName​(
String
name)
```

- getNoResize

```java
boolean getNoResize()
```

When true, forbid user from resizing frame. See the noresize
attribute definition in HTML 4.0.

- setNoResize

```java
void setNoResize​(boolean noResize)
```

- getScrolling

```java
String
getScrolling()
```

Specify whether or not the frame should have scrollbars. See the
scrolling attribute definition in HTML 4.0.

- setScrolling

```java
void setScrolling​(
String
scrolling)
```

- getSrc

```java
String
getSrc()
```

A URI designating the initial frame contents. See the src attribute
definition in HTML 4.0.

- setSrc

```java
void setSrc​(
String
src)
```

- getContentDocument

```java
Document
getContentDocument()
```

The document this frame contains, if there is any and it is available,
or

null

otherwise.

**Since:** 1.4, DOM Level 2

---

#### Method Detail

getFrameBorder

```java
String
getFrameBorder()
```

Request frame borders. See the frameborder attribute definition in
HTML 4.0.

---

#### getFrameBorder

String

getFrameBorder()

Request frame borders. See the frameborder attribute definition in
HTML 4.0.

setFrameBorder

```java
void setFrameBorder​(
String
frameBorder)
```

---

#### setFrameBorder

void setFrameBorder​(

String

frameBorder)

getLongDesc

```java
String
getLongDesc()
```

URI designating a long description of this image or frame. See the
longdesc attribute definition in HTML 4.0.

---

#### getLongDesc

String

getLongDesc()

URI designating a long description of this image or frame. See the
longdesc attribute definition in HTML 4.0.

setLongDesc

```java
void setLongDesc​(
String
longDesc)
```

---

#### setLongDesc

void setLongDesc​(

String

longDesc)

getMarginHeight

```java
String
getMarginHeight()
```

Frame margin height, in pixels. See the marginheight attribute
definition in HTML 4.0.

---

#### getMarginHeight

String

getMarginHeight()

Frame margin height, in pixels. See the marginheight attribute
definition in HTML 4.0.

setMarginHeight

```java
void setMarginHeight​(
String
marginHeight)
```

---

#### setMarginHeight

void setMarginHeight​(

String

marginHeight)

getMarginWidth

```java
String
getMarginWidth()
```

Frame margin width, in pixels. See the marginwidth attribute
definition in HTML 4.0.

---

#### getMarginWidth

String

getMarginWidth()

Frame margin width, in pixels. See the marginwidth attribute
definition in HTML 4.0.

setMarginWidth

```java
void setMarginWidth​(
String
marginWidth)
```

---

#### setMarginWidth

void setMarginWidth​(

String

marginWidth)

getName

```java
String
getName()
```

The frame name (object of the

target

attribute). See the
name attribute definition in HTML 4.0.

---

#### getName

String

getName()

The frame name (object of the

target

attribute). See the
name attribute definition in HTML 4.0.

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

getNoResize

```java
boolean getNoResize()
```

When true, forbid user from resizing frame. See the noresize
attribute definition in HTML 4.0.

---

#### getNoResize

boolean getNoResize()

When true, forbid user from resizing frame. See the noresize
attribute definition in HTML 4.0.

setNoResize

```java
void setNoResize​(boolean noResize)
```

---

#### setNoResize

void setNoResize​(boolean noResize)

getScrolling

```java
String
getScrolling()
```

Specify whether or not the frame should have scrollbars. See the
scrolling attribute definition in HTML 4.0.

---

#### getScrolling

String

getScrolling()

Specify whether or not the frame should have scrollbars. See the
scrolling attribute definition in HTML 4.0.

setScrolling

```java
void setScrolling​(
String
scrolling)
```

---

#### setScrolling

void setScrolling​(

String

scrolling)

getSrc

```java
String
getSrc()
```

A URI designating the initial frame contents. See the src attribute
definition in HTML 4.0.

---

#### getSrc

String

getSrc()

A URI designating the initial frame contents. See the src attribute
definition in HTML 4.0.

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

getContentDocument

```java
Document
getContentDocument()
```

The document this frame contains, if there is any and it is available,
or

null

otherwise.

**Since:** 1.4, DOM Level 2

---

#### getContentDocument

Document

getContentDocument()

The document this frame contains, if there is any and it is available,
or

null

otherwise.

---

