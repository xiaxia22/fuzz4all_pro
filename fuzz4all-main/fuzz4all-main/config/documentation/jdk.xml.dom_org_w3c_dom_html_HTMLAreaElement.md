# Interface HTMLAreaElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLAreaElement.html`

### Class Description

```java
public interface
HTMLAreaElement

extends
HTMLElement
```

Client-side image map area definition. See the AREA element definition in
HTML 4.0.

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

#### boolean getNoHref()

Specifies that this area is inactive, i.e., has no associated action.
See the nohref attribute definition in HTML 4.0.

---

#### void setNoHref​(boolean noHref)

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

### Additional Sections

#### Interface HTMLAreaElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLAreaElement

extends
HTMLElement
```

Client-side image map area definition. See the AREA element definition in
HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLAreaElement

extends

HTMLElement

Client-side image map area definition. See the AREA element definition in
HTML 4.0.

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

getAccessKey

()

A single character access key to give access to the form control.

String

getAlt

()

Alternate text for user agents not rendering the normal content of
this element.

String

getCoords

()

Comma-separated list of lengths, defining an active region geometry.

String

getHref

()

The URI of the linked resource.

boolean

getNoHref

()

Specifies that this area is inactive, i.e., has no associated action.

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

void

setAccessKey

​(

String

accessKey)

void

setAlt

​(

String

alt)

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

setNoHref

​(boolean noHref)

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

getAccessKey

()

A single character access key to give access to the form control.

String

getAlt

()

Alternate text for user agents not rendering the normal content of
this element.

String

getCoords

()

Comma-separated list of lengths, defining an active region geometry.

String

getHref

()

The URI of the linked resource.

boolean

getNoHref

()

Specifies that this area is inactive, i.e., has no associated action.

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

void

setAccessKey

​(

String

accessKey)

void

setAlt

​(

String

alt)

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

setNoHref

​(boolean noHref)

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

A single character access key to give access to the form control.

Alternate text for user agents not rendering the normal content of
this element.

Comma-separated list of lengths, defining an active region geometry.

The URI of the linked resource.

Specifies that this area is inactive, i.e., has no associated action.

The shape of the active area.

Index that represents the element's position in the tabbing order.

Frame to render the resource in.

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

- getNoHref

```java
boolean getNoHref()
```

Specifies that this area is inactive, i.e., has no associated action.
See the nohref attribute definition in HTML 4.0.

- setNoHref

```java
void setNoHref​(boolean noHref)
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

- getNoHref

```java
boolean getNoHref()
```

Specifies that this area is inactive, i.e., has no associated action.
See the nohref attribute definition in HTML 4.0.

- setNoHref

```java
void setNoHref​(boolean noHref)
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

getNoHref

```java
boolean getNoHref()
```

Specifies that this area is inactive, i.e., has no associated action.
See the nohref attribute definition in HTML 4.0.

---

#### getNoHref

boolean getNoHref()

Specifies that this area is inactive, i.e., has no associated action.
See the nohref attribute definition in HTML 4.0.

setNoHref

```java
void setNoHref​(boolean noHref)
```

---

#### setNoHref

void setNoHref​(boolean noHref)

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

---

