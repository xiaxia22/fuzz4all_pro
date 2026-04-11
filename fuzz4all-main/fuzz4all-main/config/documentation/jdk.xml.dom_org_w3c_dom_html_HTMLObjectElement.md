# Interface HTMLObjectElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLObjectElement.html`

### Class Description

```java
public interface
HTMLObjectElement

extends
HTMLElement
```

Generic embedded object. Note. In principle, all properties on the object
element are read-write but in some environments some properties may be
read-only once the underlying object is instantiated. See the OBJECT
element definition in HTML 4.0.

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

#### HTMLFormElement
getForm()

Returns the

FORM

element containing this control. Returns

null

if this control is not within the context of a form.

---

#### String
getCode()

Applet class file. See the

code

attribute for
HTMLAppletElement.

---

#### void setCode​(
String
code)

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
getArchive()

Space-separated list of archives. See the archive attribute definition
in HTML 4.0.

---

#### void setArchive​(
String
archive)

*No description found.*

---

#### String
getBorder()

Width of border around the object. See the border attribute definition
in HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### void setBorder​(
String
border)

*No description found.*

---

#### String
getCodeBase()

Base URI for

classid

,

data

, and

archive

attributes. See the codebase attribute definition
in HTML 4.0.

---

#### void setCodeBase​(
String
codeBase)

*No description found.*

---

#### String
getCodeType()

Content type for data downloaded via

classid

attribute.
See the codetype attribute definition in HTML 4.0.

---

#### void setCodeType​(
String
codeType)

*No description found.*

---

#### String
getData()

A URI specifying the location of the object's data. See the data
attribute definition in HTML 4.0.

---

#### void setData​(
String
data)

*No description found.*

---

#### boolean getDeclare()

Declare (for future reference), but do not instantiate, this object.
See the declare attribute definition in HTML 4.0.

---

#### void setDeclare​(boolean declare)

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

Horizontal space to the left and right of this image, applet, or
object. See the hspace attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### void setHspace​(
String
hspace)

*No description found.*

---

#### String
getName()

Form control or object name when submitted with a form. See the name
attribute definition in HTML 4.0.

---

#### void setName​(
String
name)

*No description found.*

---

#### String
getStandby()

Message to render while loading the object. See the standby attribute
definition in HTML 4.0.

---

#### void setStandby​(
String
standby)

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
getType()

Content type for data downloaded via

data

attribute. See
the type attribute definition in HTML 4.0.

---

#### void setType​(
String
type)

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

Vertical space above and below this image, applet, or object. See the
vspace attribute definition in HTML 4.0. This attribute is deprecated
in HTML 4.0.

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

#### Document
getContentDocument()

The document this object contains, if there is any and it is
available, or

null

otherwise.

**Since:**
- 1.4, DOM Level 2

---

### Additional Sections

#### Interface HTMLObjectElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLObjectElement

extends
HTMLElement
```

Generic embedded object. Note. In principle, all properties on the object
element are read-write but in some environments some properties may be
read-only once the underlying object is instantiated. See the OBJECT
element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLObjectElement

extends

HTMLElement

Generic embedded object. Note. In principle, all properties on the object
element are read-write but in some environments some properties may be
read-only once the underlying object is instantiated. See the OBJECT
element definition in HTML 4.0.

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

getArchive

()

Space-separated list of archives.

String

getBorder

()

Width of border around the object.

String

getCode

()

Applet class file.

String

getCodeBase

()

Base URI for

classid

,

data

, and

archive

attributes.

String

getCodeType

()

Content type for data downloaded via

classid

attribute.

Document

getContentDocument

()

The document this object contains, if there is any and it is
available, or

null

otherwise.

String

getData

()

A URI specifying the location of the object's data.

boolean

getDeclare

()

Declare (for future reference), but do not instantiate, this object.

HTMLFormElement

getForm

()

Returns the

FORM

element containing this control.

String

getHeight

()

Override height.

String

getHspace

()

Horizontal space to the left and right of this image, applet, or
object.

String

getName

()

Form control or object name when submitted with a form.

String

getStandby

()

Message to render while loading the object.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

Content type for data downloaded via

data

attribute.

String

getUseMap

()

Use client-side image map.

String

getVspace

()

Vertical space above and below this image, applet, or object.

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

setArchive

​(

String

archive)

void

setBorder

​(

String

border)

void

setCode

​(

String

code)

void

setCodeBase

​(

String

codeBase)

void

setCodeType

​(

String

codeType)

void

setData

​(

String

data)

void

setDeclare

​(boolean declare)

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

setName

​(

String

name)

void

setStandby

​(

String

standby)

void

setTabIndex

​(int tabIndex)

void

setType

​(

String

type)

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

getArchive

()

Space-separated list of archives.

String

getBorder

()

Width of border around the object.

String

getCode

()

Applet class file.

String

getCodeBase

()

Base URI for

classid

,

data

, and

archive

attributes.

String

getCodeType

()

Content type for data downloaded via

classid

attribute.

Document

getContentDocument

()

The document this object contains, if there is any and it is
available, or

null

otherwise.

String

getData

()

A URI specifying the location of the object's data.

boolean

getDeclare

()

Declare (for future reference), but do not instantiate, this object.

HTMLFormElement

getForm

()

Returns the

FORM

element containing this control.

String

getHeight

()

Override height.

String

getHspace

()

Horizontal space to the left and right of this image, applet, or
object.

String

getName

()

Form control or object name when submitted with a form.

String

getStandby

()

Message to render while loading the object.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

Content type for data downloaded via

data

attribute.

String

getUseMap

()

Use client-side image map.

String

getVspace

()

Vertical space above and below this image, applet, or object.

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

setArchive

​(

String

archive)

void

setBorder

​(

String

border)

void

setCode

​(

String

code)

void

setCodeBase

​(

String

codeBase)

void

setCodeType

​(

String

codeType)

void

setData

​(

String

data)

void

setDeclare

​(boolean declare)

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

setName

​(

String

name)

void

setStandby

​(

String

standby)

void

setTabIndex

​(int tabIndex)

void

setType

​(

String

type)

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

Space-separated list of archives.

Width of border around the object.

Applet class file.

Base URI for

classid

,

data

, and

archive

attributes.

Content type for data downloaded via

classid

attribute.

The document this object contains, if there is any and it is
available, or

null

otherwise.

A URI specifying the location of the object's data.

Declare (for future reference), but do not instantiate, this object.

Returns the

FORM

element containing this control.

Override height.

Horizontal space to the left and right of this image, applet, or
object.

Form control or object name when submitted with a form.

Message to render while loading the object.

Index that represents the element's position in the tabbing order.

Content type for data downloaded via

data

attribute.

Use client-side image map.

Vertical space above and below this image, applet, or object.

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

- getForm

```java
HTMLFormElement
getForm()
```

Returns the

FORM

element containing this control. Returns

null

if this control is not within the context of a form.

- getCode

```java
String
getCode()
```

Applet class file. See the

code

attribute for
HTMLAppletElement.

- setCode

```java
void setCode​(
String
code)
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

- getArchive

```java
String
getArchive()
```

Space-separated list of archives. See the archive attribute definition
in HTML 4.0.

- setArchive

```java
void setArchive​(
String
archive)
```

- getBorder

```java
String
getBorder()
```

Width of border around the object. See the border attribute definition
in HTML 4.0. This attribute is deprecated in HTML 4.0.

- setBorder

```java
void setBorder​(
String
border)
```

- getCodeBase

```java
String
getCodeBase()
```

Base URI for

classid

,

data

, and

archive

attributes. See the codebase attribute definition
in HTML 4.0.

- setCodeBase

```java
void setCodeBase​(
String
codeBase)
```

- getCodeType

```java
String
getCodeType()
```

Content type for data downloaded via

classid

attribute.
See the codetype attribute definition in HTML 4.0.

- setCodeType

```java
void setCodeType​(
String
codeType)
```

- getData

```java
String
getData()
```

A URI specifying the location of the object's data. See the data
attribute definition in HTML 4.0.

- setData

```java
void setData​(
String
data)
```

- getDeclare

```java
boolean getDeclare()
```

Declare (for future reference), but do not instantiate, this object.
See the declare attribute definition in HTML 4.0.

- setDeclare

```java
void setDeclare​(boolean declare)
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

Horizontal space to the left and right of this image, applet, or
object. See the hspace attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setHspace

```java
void setHspace​(
String
hspace)
```

- getName

```java
String
getName()
```

Form control or object name when submitted with a form. See the name
attribute definition in HTML 4.0.

- setName

```java
void setName​(
String
name)
```

- getStandby

```java
String
getStandby()
```

Message to render while loading the object. See the standby attribute
definition in HTML 4.0.

- setStandby

```java
void setStandby​(
String
standby)
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

- getType

```java
String
getType()
```

Content type for data downloaded via

data

attribute. See
the type attribute definition in HTML 4.0.

- setType

```java
void setType​(
String
type)
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

Vertical space above and below this image, applet, or object. See the
vspace attribute definition in HTML 4.0. This attribute is deprecated
in HTML 4.0.

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

- getContentDocument

```java
Document
getContentDocument()
```

The document this object contains, if there is any and it is
available, or

null

otherwise.

**Since:** 1.4, DOM Level 2

Method Detail

- getForm

```java
HTMLFormElement
getForm()
```

Returns the

FORM

element containing this control. Returns

null

if this control is not within the context of a form.

- getCode

```java
String
getCode()
```

Applet class file. See the

code

attribute for
HTMLAppletElement.

- setCode

```java
void setCode​(
String
code)
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

- getArchive

```java
String
getArchive()
```

Space-separated list of archives. See the archive attribute definition
in HTML 4.0.

- setArchive

```java
void setArchive​(
String
archive)
```

- getBorder

```java
String
getBorder()
```

Width of border around the object. See the border attribute definition
in HTML 4.0. This attribute is deprecated in HTML 4.0.

- setBorder

```java
void setBorder​(
String
border)
```

- getCodeBase

```java
String
getCodeBase()
```

Base URI for

classid

,

data

, and

archive

attributes. See the codebase attribute definition
in HTML 4.0.

- setCodeBase

```java
void setCodeBase​(
String
codeBase)
```

- getCodeType

```java
String
getCodeType()
```

Content type for data downloaded via

classid

attribute.
See the codetype attribute definition in HTML 4.0.

- setCodeType

```java
void setCodeType​(
String
codeType)
```

- getData

```java
String
getData()
```

A URI specifying the location of the object's data. See the data
attribute definition in HTML 4.0.

- setData

```java
void setData​(
String
data)
```

- getDeclare

```java
boolean getDeclare()
```

Declare (for future reference), but do not instantiate, this object.
See the declare attribute definition in HTML 4.0.

- setDeclare

```java
void setDeclare​(boolean declare)
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

Horizontal space to the left and right of this image, applet, or
object. See the hspace attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setHspace

```java
void setHspace​(
String
hspace)
```

- getName

```java
String
getName()
```

Form control or object name when submitted with a form. See the name
attribute definition in HTML 4.0.

- setName

```java
void setName​(
String
name)
```

- getStandby

```java
String
getStandby()
```

Message to render while loading the object. See the standby attribute
definition in HTML 4.0.

- setStandby

```java
void setStandby​(
String
standby)
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

- getType

```java
String
getType()
```

Content type for data downloaded via

data

attribute. See
the type attribute definition in HTML 4.0.

- setType

```java
void setType​(
String
type)
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

Vertical space above and below this image, applet, or object. See the
vspace attribute definition in HTML 4.0. This attribute is deprecated
in HTML 4.0.

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

- getContentDocument

```java
Document
getContentDocument()
```

The document this object contains, if there is any and it is
available, or

null

otherwise.

**Since:** 1.4, DOM Level 2

---

#### Method Detail

getForm

```java
HTMLFormElement
getForm()
```

Returns the

FORM

element containing this control. Returns

null

if this control is not within the context of a form.

---

#### getForm

HTMLFormElement

getForm()

Returns the

FORM

element containing this control. Returns

null

if this control is not within the context of a form.

getCode

```java
String
getCode()
```

Applet class file. See the

code

attribute for
HTMLAppletElement.

---

#### getCode

String

getCode()

Applet class file. See the

code

attribute for
HTMLAppletElement.

setCode

```java
void setCode​(
String
code)
```

---

#### setCode

void setCode​(

String

code)

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

getArchive

```java
String
getArchive()
```

Space-separated list of archives. See the archive attribute definition
in HTML 4.0.

---

#### getArchive

String

getArchive()

Space-separated list of archives. See the archive attribute definition
in HTML 4.0.

setArchive

```java
void setArchive​(
String
archive)
```

---

#### setArchive

void setArchive​(

String

archive)

getBorder

```java
String
getBorder()
```

Width of border around the object. See the border attribute definition
in HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### getBorder

String

getBorder()

Width of border around the object. See the border attribute definition
in HTML 4.0. This attribute is deprecated in HTML 4.0.

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

getCodeBase

```java
String
getCodeBase()
```

Base URI for

classid

,

data

, and

archive

attributes. See the codebase attribute definition
in HTML 4.0.

---

#### getCodeBase

String

getCodeBase()

Base URI for

classid

,

data

, and

archive

attributes. See the codebase attribute definition
in HTML 4.0.

setCodeBase

```java
void setCodeBase​(
String
codeBase)
```

---

#### setCodeBase

void setCodeBase​(

String

codeBase)

getCodeType

```java
String
getCodeType()
```

Content type for data downloaded via

classid

attribute.
See the codetype attribute definition in HTML 4.0.

---

#### getCodeType

String

getCodeType()

Content type for data downloaded via

classid

attribute.
See the codetype attribute definition in HTML 4.0.

setCodeType

```java
void setCodeType​(
String
codeType)
```

---

#### setCodeType

void setCodeType​(

String

codeType)

getData

```java
String
getData()
```

A URI specifying the location of the object's data. See the data
attribute definition in HTML 4.0.

---

#### getData

String

getData()

A URI specifying the location of the object's data. See the data
attribute definition in HTML 4.0.

setData

```java
void setData​(
String
data)
```

---

#### setData

void setData​(

String

data)

getDeclare

```java
boolean getDeclare()
```

Declare (for future reference), but do not instantiate, this object.
See the declare attribute definition in HTML 4.0.

---

#### getDeclare

boolean getDeclare()

Declare (for future reference), but do not instantiate, this object.
See the declare attribute definition in HTML 4.0.

setDeclare

```java
void setDeclare​(boolean declare)
```

---

#### setDeclare

void setDeclare​(boolean declare)

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

Horizontal space to the left and right of this image, applet, or
object. See the hspace attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### getHspace

String

getHspace()

Horizontal space to the left and right of this image, applet, or
object. See the hspace attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

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

getName

```java
String
getName()
```

Form control or object name when submitted with a form. See the name
attribute definition in HTML 4.0.

---

#### getName

String

getName()

Form control or object name when submitted with a form. See the name
attribute definition in HTML 4.0.

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

getStandby

```java
String
getStandby()
```

Message to render while loading the object. See the standby attribute
definition in HTML 4.0.

---

#### getStandby

String

getStandby()

Message to render while loading the object. See the standby attribute
definition in HTML 4.0.

setStandby

```java
void setStandby​(
String
standby)
```

---

#### setStandby

void setStandby​(

String

standby)

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

getType

```java
String
getType()
```

Content type for data downloaded via

data

attribute. See
the type attribute definition in HTML 4.0.

---

#### getType

String

getType()

Content type for data downloaded via

data

attribute. See
the type attribute definition in HTML 4.0.

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

Vertical space above and below this image, applet, or object. See the
vspace attribute definition in HTML 4.0. This attribute is deprecated
in HTML 4.0.

---

#### getVspace

String

getVspace()

Vertical space above and below this image, applet, or object. See the
vspace attribute definition in HTML 4.0. This attribute is deprecated
in HTML 4.0.

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

getContentDocument

```java
Document
getContentDocument()
```

The document this object contains, if there is any and it is
available, or

null

otherwise.

**Since:** 1.4, DOM Level 2

---

#### getContentDocument

Document

getContentDocument()

The document this object contains, if there is any and it is
available, or

null

otherwise.

---

