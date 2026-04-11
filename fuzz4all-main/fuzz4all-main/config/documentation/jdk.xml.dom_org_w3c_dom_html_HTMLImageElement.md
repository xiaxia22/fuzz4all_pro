# Interface HTMLImageElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLImageElement.html`

### Class Description

```java
public interface
HTMLImageElement

extends
HTMLElement
```

Embedded image. See the IMG element definition in HTML 4.0.

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
getLowSrc()

URI designating the source of this image, for low-resolution output.

---

#### void setLowSrc​(
String
lowSrc)

*No description found.*

---

#### String
getName()

The name of the element (for backwards compatibility).

---

#### void setName​(
String
name)

*No description found.*

---

#### String
getAlign()

Aligns this object (vertically or horizontally) with respect to its
surrounding text. See the align attribute definition in HTML 4.0.
This attribute is deprecated in HTML 4.0.

---

#### void setAlign​(
String
align)

*No description found.*

---

#### String
getAlt()

Alternate text for user agents not rendering the normal content of
this element. See the alt attribute definition in HTML 4.0.

---

#### void setAlt​(
String
alt)

*No description found.*

---

#### String
getBorder()

Width of border around image. See the border attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### void setBorder​(
String
border)

*No description found.*

---

#### String
getHeight()

Override height. See the height attribute definition in HTML 4.0.

---

#### void setHeight​(
String
height)

*No description found.*

---

#### String
getHspace()

Horizontal space to the left and right of this image. See the hspace
attribute definition in HTML 4.0. This attribute is deprecated in HTML
4.0.

---

#### void setHspace​(
String
hspace)

*No description found.*

---

#### boolean getIsMap()

Use server-side image map. See the ismap attribute definition in HTML
4.0.

---

#### void setIsMap​(boolean isMap)

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
getSrc()

URI designating the source of this image. See the src attribute
definition in HTML 4.0.

---

#### void setSrc​(
String
src)

*No description found.*

---

#### String
getUseMap()

Use client-side image map. See the usemap attribute definition in
HTML 4.0.

---

#### void setUseMap​(
String
useMap)

*No description found.*

---

#### String
getVspace()

Vertical space above and below this image. See the vspace attribute
definition in HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### void setVspace​(
String
vspace)

*No description found.*

---

#### String
getWidth()

Override width. See the width attribute definition in HTML 4.0.

---

#### void setWidth​(
String
width)

*No description found.*

---

### Additional Sections

#### Interface HTMLImageElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLImageElement

extends
HTMLElement
```

Embedded image. See the IMG element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLImageElement

extends

HTMLElement

Embedded image. See the IMG element definition in HTML 4.0.

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

getAlign

()

Aligns this object (vertically or horizontally) with respect to its
surrounding text.

String

getAlt

()

Alternate text for user agents not rendering the normal content of
this element.

String

getBorder

()

Width of border around image.

String

getHeight

()

Override height.

String

getHspace

()

Horizontal space to the left and right of this image.

boolean

getIsMap

()

Use server-side image map.

String

getLongDesc

()

URI designating a long description of this image or frame.

String

getLowSrc

()

URI designating the source of this image, for low-resolution output.

String

getName

()

The name of the element (for backwards compatibility).

String

getSrc

()

URI designating the source of this image.

String

getUseMap

()

Use client-side image map.

String

getVspace

()

Vertical space above and below this image.

String

getWidth

()

Override width.

void

setAlign

​(

String

align)

void

setAlt

​(

String

alt)

void

setBorder

​(

String

border)

void

setHeight

​(

String

height)

void

setHspace

​(

String

hspace)

void

setIsMap

​(boolean isMap)

void

setLongDesc

​(

String

longDesc)

void

setLowSrc

​(

String

lowSrc)

void

setName

​(

String

name)

void

setSrc

​(

String

src)

void

setUseMap

​(

String

useMap)

void

setVspace

​(

String

vspace)

void

setWidth

​(

String

width)

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

getAlign

()

Aligns this object (vertically or horizontally) with respect to its
surrounding text.

String

getAlt

()

Alternate text for user agents not rendering the normal content of
this element.

String

getBorder

()

Width of border around image.

String

getHeight

()

Override height.

String

getHspace

()

Horizontal space to the left and right of this image.

boolean

getIsMap

()

Use server-side image map.

String

getLongDesc

()

URI designating a long description of this image or frame.

String

getLowSrc

()

URI designating the source of this image, for low-resolution output.

String

getName

()

The name of the element (for backwards compatibility).

String

getSrc

()

URI designating the source of this image.

String

getUseMap

()

Use client-side image map.

String

getVspace

()

Vertical space above and below this image.

String

getWidth

()

Override width.

void

setAlign

​(

String

align)

void

setAlt

​(

String

alt)

void

setBorder

​(

String

border)

void

setHeight

​(

String

height)

void

setHspace

​(

String

hspace)

void

setIsMap

​(boolean isMap)

void

setLongDesc

​(

String

longDesc)

void

setLowSrc

​(

String

lowSrc)

void

setName

​(

String

name)

void

setSrc

​(

String

src)

void

setUseMap

​(

String

useMap)

void

setVspace

​(

String

vspace)

void

setWidth

​(

String

width)

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

Aligns this object (vertically or horizontally) with respect to its
surrounding text.

Alternate text for user agents not rendering the normal content of
this element.

Width of border around image.

Override height.

Horizontal space to the left and right of this image.

Use server-side image map.

URI designating a long description of this image or frame.

URI designating the source of this image, for low-resolution output.

The name of the element (for backwards compatibility).

URI designating the source of this image.

Use client-side image map.

Vertical space above and below this image.

Override width.

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

- getLowSrc

```java
String
getLowSrc()
```

URI designating the source of this image, for low-resolution output.

- setLowSrc

```java
void setLowSrc​(
String
lowSrc)
```

- getName

```java
String
getName()
```

The name of the element (for backwards compatibility).

- setName

```java
void setName​(
String
name)
```

- getAlign

```java
String
getAlign()
```

Aligns this object (vertically or horizontally) with respect to its
surrounding text. See the align attribute definition in HTML 4.0.
This attribute is deprecated in HTML 4.0.

- setAlign

```java
void setAlign​(
String
align)
```

- getAlt

```java
String
getAlt()
```

Alternate text for user agents not rendering the normal content of
this element. See the alt attribute definition in HTML 4.0.

- setAlt

```java
void setAlt​(
String
alt)
```

- getBorder

```java
String
getBorder()
```

Width of border around image. See the border attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

- setBorder

```java
void setBorder​(
String
border)
```

- getHeight

```java
String
getHeight()
```

Override height. See the height attribute definition in HTML 4.0.

- setHeight

```java
void setHeight​(
String
height)
```

- getHspace

```java
String
getHspace()
```

Horizontal space to the left and right of this image. See the hspace
attribute definition in HTML 4.0. This attribute is deprecated in HTML
4.0.

- setHspace

```java
void setHspace​(
String
hspace)
```

- getIsMap

```java
boolean getIsMap()
```

Use server-side image map. See the ismap attribute definition in HTML
4.0.

- setIsMap

```java
void setIsMap​(boolean isMap)
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

- getSrc

```java
String
getSrc()
```

URI designating the source of this image. See the src attribute
definition in HTML 4.0.

- setSrc

```java
void setSrc​(
String
src)
```

- getUseMap

```java
String
getUseMap()
```

Use client-side image map. See the usemap attribute definition in
HTML 4.0.

- setUseMap

```java
void setUseMap​(
String
useMap)
```

- getVspace

```java
String
getVspace()
```

Vertical space above and below this image. See the vspace attribute
definition in HTML 4.0. This attribute is deprecated in HTML 4.0.

- setVspace

```java
void setVspace​(
String
vspace)
```

- getWidth

```java
String
getWidth()
```

Override width. See the width attribute definition in HTML 4.0.

- setWidth

```java
void setWidth​(
String
width)
```

Method Detail

- getLowSrc

```java
String
getLowSrc()
```

URI designating the source of this image, for low-resolution output.

- setLowSrc

```java
void setLowSrc​(
String
lowSrc)
```

- getName

```java
String
getName()
```

The name of the element (for backwards compatibility).

- setName

```java
void setName​(
String
name)
```

- getAlign

```java
String
getAlign()
```

Aligns this object (vertically or horizontally) with respect to its
surrounding text. See the align attribute definition in HTML 4.0.
This attribute is deprecated in HTML 4.0.

- setAlign

```java
void setAlign​(
String
align)
```

- getAlt

```java
String
getAlt()
```

Alternate text for user agents not rendering the normal content of
this element. See the alt attribute definition in HTML 4.0.

- setAlt

```java
void setAlt​(
String
alt)
```

- getBorder

```java
String
getBorder()
```

Width of border around image. See the border attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

- setBorder

```java
void setBorder​(
String
border)
```

- getHeight

```java
String
getHeight()
```

Override height. See the height attribute definition in HTML 4.0.

- setHeight

```java
void setHeight​(
String
height)
```

- getHspace

```java
String
getHspace()
```

Horizontal space to the left and right of this image. See the hspace
attribute definition in HTML 4.0. This attribute is deprecated in HTML
4.0.

- setHspace

```java
void setHspace​(
String
hspace)
```

- getIsMap

```java
boolean getIsMap()
```

Use server-side image map. See the ismap attribute definition in HTML
4.0.

- setIsMap

```java
void setIsMap​(boolean isMap)
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

- getSrc

```java
String
getSrc()
```

URI designating the source of this image. See the src attribute
definition in HTML 4.0.

- setSrc

```java
void setSrc​(
String
src)
```

- getUseMap

```java
String
getUseMap()
```

Use client-side image map. See the usemap attribute definition in
HTML 4.0.

- setUseMap

```java
void setUseMap​(
String
useMap)
```

- getVspace

```java
String
getVspace()
```

Vertical space above and below this image. See the vspace attribute
definition in HTML 4.0. This attribute is deprecated in HTML 4.0.

- setVspace

```java
void setVspace​(
String
vspace)
```

- getWidth

```java
String
getWidth()
```

Override width. See the width attribute definition in HTML 4.0.

- setWidth

```java
void setWidth​(
String
width)
```

---

#### Method Detail

getLowSrc

```java
String
getLowSrc()
```

URI designating the source of this image, for low-resolution output.

---

#### getLowSrc

String

getLowSrc()

URI designating the source of this image, for low-resolution output.

setLowSrc

```java
void setLowSrc​(
String
lowSrc)
```

---

#### setLowSrc

void setLowSrc​(

String

lowSrc)

getName

```java
String
getName()
```

The name of the element (for backwards compatibility).

---

#### getName

String

getName()

The name of the element (for backwards compatibility).

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

getAlign

```java
String
getAlign()
```

Aligns this object (vertically or horizontally) with respect to its
surrounding text. See the align attribute definition in HTML 4.0.
This attribute is deprecated in HTML 4.0.

---

#### getAlign

String

getAlign()

Aligns this object (vertically or horizontally) with respect to its
surrounding text. See the align attribute definition in HTML 4.0.
This attribute is deprecated in HTML 4.0.

setAlign

```java
void setAlign​(
String
align)
```

---

#### setAlign

void setAlign​(

String

align)

getAlt

```java
String
getAlt()
```

Alternate text for user agents not rendering the normal content of
this element. See the alt attribute definition in HTML 4.0.

---

#### getAlt

String

getAlt()

Alternate text for user agents not rendering the normal content of
this element. See the alt attribute definition in HTML 4.0.

setAlt

```java
void setAlt​(
String
alt)
```

---

#### setAlt

void setAlt​(

String

alt)

getBorder

```java
String
getBorder()
```

Width of border around image. See the border attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### getBorder

String

getBorder()

Width of border around image. See the border attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

setBorder

```java
void setBorder​(
String
border)
```

---

#### setBorder

void setBorder​(

String

border)

getHeight

```java
String
getHeight()
```

Override height. See the height attribute definition in HTML 4.0.

---

#### getHeight

String

getHeight()

Override height. See the height attribute definition in HTML 4.0.

setHeight

```java
void setHeight​(
String
height)
```

---

#### setHeight

void setHeight​(

String

height)

getHspace

```java
String
getHspace()
```

Horizontal space to the left and right of this image. See the hspace
attribute definition in HTML 4.0. This attribute is deprecated in HTML
4.0.

---

#### getHspace

String

getHspace()

Horizontal space to the left and right of this image. See the hspace
attribute definition in HTML 4.0. This attribute is deprecated in HTML
4.0.

setHspace

```java
void setHspace​(
String
hspace)
```

---

#### setHspace

void setHspace​(

String

hspace)

getIsMap

```java
boolean getIsMap()
```

Use server-side image map. See the ismap attribute definition in HTML
4.0.

---

#### getIsMap

boolean getIsMap()

Use server-side image map. See the ismap attribute definition in HTML
4.0.

setIsMap

```java
void setIsMap​(boolean isMap)
```

---

#### setIsMap

void setIsMap​(boolean isMap)

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

getSrc

```java
String
getSrc()
```

URI designating the source of this image. See the src attribute
definition in HTML 4.0.

---

#### getSrc

String

getSrc()

URI designating the source of this image. See the src attribute
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

getUseMap

```java
String
getUseMap()
```

Use client-side image map. See the usemap attribute definition in
HTML 4.0.

---

#### getUseMap

String

getUseMap()

Use client-side image map. See the usemap attribute definition in
HTML 4.0.

setUseMap

```java
void setUseMap​(
String
useMap)
```

---

#### setUseMap

void setUseMap​(

String

useMap)

getVspace

```java
String
getVspace()
```

Vertical space above and below this image. See the vspace attribute
definition in HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### getVspace

String

getVspace()

Vertical space above and below this image. See the vspace attribute
definition in HTML 4.0. This attribute is deprecated in HTML 4.0.

setVspace

```java
void setVspace​(
String
vspace)
```

---

#### setVspace

void setVspace​(

String

vspace)

getWidth

```java
String
getWidth()
```

Override width. See the width attribute definition in HTML 4.0.

---

#### getWidth

String

getWidth()

Override width. See the width attribute definition in HTML 4.0.

setWidth

```java
void setWidth​(
String
width)
```

---

#### setWidth

void setWidth​(

String

width)

---

