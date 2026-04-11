# Interface HTMLTableElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLTableElement.html`

### Class Description

```java
public interface
HTMLTableElement

extends
HTMLElement
```

The create* and delete* methods on the table allow authors to construct
and modify tables. HTML 4.0 specifies that only one of each of the

CAPTION

,

THEAD

, and

TFOOT

elements may exist in a table. Therefore, if one exists, and the
createTHead() or createTFoot() method is called, the method returns the
existing THead or TFoot element. See the TABLE element definition in HTML
4.0.

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

#### HTMLTableCaptionElement
getCaption()

Returns the table's

CAPTION

, or void if none exists.

---

#### void setCaption​(
HTMLTableCaptionElement
caption)

*No description found.*

---

#### HTMLTableSectionElement
getTHead()

Returns the table's

THEAD

, or

null

if none
exists.

---

#### void setTHead​(
HTMLTableSectionElement
tHead)

*No description found.*

---

#### HTMLTableSectionElement
getTFoot()

Returns the table's

TFOOT

, or

null

if none
exists.

---

#### void setTFoot​(
HTMLTableSectionElement
tFoot)

*No description found.*

---

#### HTMLCollection
getRows()

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

---

#### HTMLCollection
getTBodies()

Returns a collection of the defined table bodies.

---

#### String
getAlign()

Specifies the table's position with respect to the rest of the
document. See the align attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### void setAlign​(
String
align)

*No description found.*

---

#### String
getBgColor()

Cell background color. See the bgcolor attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

---

#### void setBgColor​(
String
bgColor)

*No description found.*

---

#### String
getBorder()

The width of the border around the table. See the border attribute
definition in HTML 4.0.

---

#### void setBorder​(
String
border)

*No description found.*

---

#### String
getCellPadding()

Specifies the horizontal and vertical space between cell content and
cell borders. See the cellpadding attribute definition in HTML 4.0.

---

#### void setCellPadding​(
String
cellPadding)

*No description found.*

---

#### String
getCellSpacing()

Specifies the horizontal and vertical separation between cells. See
the cellspacing attribute definition in HTML 4.0.

---

#### void setCellSpacing​(
String
cellSpacing)

*No description found.*

---

#### String
getFrame()

Specifies which external table borders to render. See the frame
attribute definition in HTML 4.0.

---

#### void setFrame​(
String
frame)

*No description found.*

---

#### String
getRules()

Specifies which internal table borders to render. See the rules
attribute definition in HTML 4.0.

---

#### void setRules​(
String
rules)

*No description found.*

---

#### String
getSummary()

Description about the purpose or structure of a table. See the
summary attribute definition in HTML 4.0.

---

#### void setSummary​(
String
summary)

*No description found.*

---

#### String
getWidth()

Specifies the desired table width. See the width attribute definition
in HTML 4.0.

---

#### void setWidth​(
String
width)

*No description found.*

---

#### HTMLElement
createTHead()

Create a table header row or return an existing one.

**Returns:**
- A new table header element (

THEAD

).

---

#### void deleteTHead()

Delete the header from the table, if one exists.

---

#### HTMLElement
createTFoot()

Create a table footer row or return an existing one.

**Returns:**
- A footer element (

TFOOT

).

---

#### void deleteTFoot()

Delete the footer from the table, if one exists.

---

#### HTMLElement
createCaption()

Create a new table caption object or return an existing one.

**Returns:**
- A

CAPTION

element.

---

#### void deleteCaption()

Delete the table caption, if one exists.

---

#### HTMLElement
insertRow​(int index)
throws
DOMException

Insert a new empty row in the table. The new row is inserted
immediately before and in the same section as the current

index

th row in the table. If

index

is equal
to the number of rows, the new row is appended. In addition, when the
table is empty the row is inserted into a

TBODY

which is
created and inserted into the table. Note. A table row cannot be empty
according to HTML 4.0 Recommendation.

**Parameters:**
- index

- The row number where to insert a new row. This index
starts from 0 and is relative to all the rows contained inside the
table, regardless of section parentage.

**Returns:**
- The newly created row.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows or if the index is negative.

---

#### void deleteRow​(int index)
throws
DOMException

Delete a table row.

**Parameters:**
- index

- The index of the row to be deleted. This index starts
from 0 and is relative to all the rows contained inside the table,
regardless of section parentage.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

---

### Additional Sections

#### Interface HTMLTableElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLTableElement

extends
HTMLElement
```

The create* and delete* methods on the table allow authors to construct
and modify tables. HTML 4.0 specifies that only one of each of the

CAPTION

,

THEAD

, and

TFOOT

elements may exist in a table. Therefore, if one exists, and the
createTHead() or createTFoot() method is called, the method returns the
existing THead or TFoot element. See the TABLE element definition in HTML
4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLTableElement

extends

HTMLElement

The create* and delete* methods on the table allow authors to construct
and modify tables. HTML 4.0 specifies that only one of each of the

CAPTION

,

THEAD

, and

TFOOT

elements may exist in a table. Therefore, if one exists, and the
createTHead() or createTFoot() method is called, the method returns the
existing THead or TFoot element. See the TABLE element definition in HTML
4.0.

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

HTMLElement

createCaption

()

Create a new table caption object or return an existing one.

HTMLElement

createTFoot

()

Create a table footer row or return an existing one.

HTMLElement

createTHead

()

Create a table header row or return an existing one.

void

deleteCaption

()

Delete the table caption, if one exists.

void

deleteRow

​(int index)

Delete a table row.

void

deleteTFoot

()

Delete the footer from the table, if one exists.

void

deleteTHead

()

Delete the header from the table, if one exists.

String

getAlign

()

Specifies the table's position with respect to the rest of the
document.

String

getBgColor

()

Cell background color.

String

getBorder

()

The width of the border around the table.

HTMLTableCaptionElement

getCaption

()

Returns the table's

CAPTION

, or void if none exists.

String

getCellPadding

()

Specifies the horizontal and vertical space between cell content and
cell borders.

String

getCellSpacing

()

Specifies the horizontal and vertical separation between cells.

String

getFrame

()

Specifies which external table borders to render.

HTMLCollection

getRows

()

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

String

getRules

()

Specifies which internal table borders to render.

String

getSummary

()

Description about the purpose or structure of a table.

HTMLCollection

getTBodies

()

Returns a collection of the defined table bodies.

HTMLTableSectionElement

getTFoot

()

Returns the table's

TFOOT

, or

null

if none
exists.

HTMLTableSectionElement

getTHead

()

Returns the table's

THEAD

, or

null

if none
exists.

String

getWidth

()

Specifies the desired table width.

HTMLElement

insertRow

​(int index)

Insert a new empty row in the table.

void

setAlign

​(

String

align)

void

setBgColor

​(

String

bgColor)

void

setBorder

​(

String

border)

void

setCaption

​(

HTMLTableCaptionElement

caption)

void

setCellPadding

​(

String

cellPadding)

void

setCellSpacing

​(

String

cellSpacing)

void

setFrame

​(

String

frame)

void

setRules

​(

String

rules)

void

setSummary

​(

String

summary)

void

setTFoot

​(

HTMLTableSectionElement

tFoot)

void

setTHead

​(

HTMLTableSectionElement

tHead)

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

HTMLElement

createCaption

()

Create a new table caption object or return an existing one.

HTMLElement

createTFoot

()

Create a table footer row or return an existing one.

HTMLElement

createTHead

()

Create a table header row or return an existing one.

void

deleteCaption

()

Delete the table caption, if one exists.

void

deleteRow

​(int index)

Delete a table row.

void

deleteTFoot

()

Delete the footer from the table, if one exists.

void

deleteTHead

()

Delete the header from the table, if one exists.

String

getAlign

()

Specifies the table's position with respect to the rest of the
document.

String

getBgColor

()

Cell background color.

String

getBorder

()

The width of the border around the table.

HTMLTableCaptionElement

getCaption

()

Returns the table's

CAPTION

, or void if none exists.

String

getCellPadding

()

Specifies the horizontal and vertical space between cell content and
cell borders.

String

getCellSpacing

()

Specifies the horizontal and vertical separation between cells.

String

getFrame

()

Specifies which external table borders to render.

HTMLCollection

getRows

()

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

String

getRules

()

Specifies which internal table borders to render.

String

getSummary

()

Description about the purpose or structure of a table.

HTMLCollection

getTBodies

()

Returns a collection of the defined table bodies.

HTMLTableSectionElement

getTFoot

()

Returns the table's

TFOOT

, or

null

if none
exists.

HTMLTableSectionElement

getTHead

()

Returns the table's

THEAD

, or

null

if none
exists.

String

getWidth

()

Specifies the desired table width.

HTMLElement

insertRow

​(int index)

Insert a new empty row in the table.

void

setAlign

​(

String

align)

void

setBgColor

​(

String

bgColor)

void

setBorder

​(

String

border)

void

setCaption

​(

HTMLTableCaptionElement

caption)

void

setCellPadding

​(

String

cellPadding)

void

setCellSpacing

​(

String

cellSpacing)

void

setFrame

​(

String

frame)

void

setRules

​(

String

rules)

void

setSummary

​(

String

summary)

void

setTFoot

​(

HTMLTableSectionElement

tFoot)

void

setTHead

​(

HTMLTableSectionElement

tHead)

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

Create a new table caption object or return an existing one.

Create a table footer row or return an existing one.

Create a table header row or return an existing one.

Delete the table caption, if one exists.

Delete a table row.

Delete the footer from the table, if one exists.

Delete the header from the table, if one exists.

Specifies the table's position with respect to the rest of the
document.

Cell background color.

The width of the border around the table.

Returns the table's

CAPTION

, or void if none exists.

Specifies the horizontal and vertical space between cell content and
cell borders.

Specifies the horizontal and vertical separation between cells.

Specifies which external table borders to render.

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

Specifies which internal table borders to render.

Description about the purpose or structure of a table.

Returns a collection of the defined table bodies.

Returns the table's

TFOOT

, or

null

if none
exists.

Returns the table's

THEAD

, or

null

if none
exists.

Specifies the desired table width.

Insert a new empty row in the table.

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

- getCaption

```java
HTMLTableCaptionElement
getCaption()
```

Returns the table's

CAPTION

, or void if none exists.

- setCaption

```java
void setCaption​(
HTMLTableCaptionElement
caption)
```

- getTHead

```java
HTMLTableSectionElement
getTHead()
```

Returns the table's

THEAD

, or

null

if none
exists.

- setTHead

```java
void setTHead​(
HTMLTableSectionElement
tHead)
```

- getTFoot

```java
HTMLTableSectionElement
getTFoot()
```

Returns the table's

TFOOT

, or

null

if none
exists.

- setTFoot

```java
void setTFoot​(
HTMLTableSectionElement
tFoot)
```

- getRows

```java
HTMLCollection
getRows()
```

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

- getTBodies

```java
HTMLCollection
getTBodies()
```

Returns a collection of the defined table bodies.

- getAlign

```java
String
getAlign()
```

Specifies the table's position with respect to the rest of the
document. See the align attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setAlign

```java
void setAlign​(
String
align)
```

- getBgColor

```java
String
getBgColor()
```

Cell background color. See the bgcolor attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

- setBgColor

```java
void setBgColor​(
String
bgColor)
```

- getBorder

```java
String
getBorder()
```

The width of the border around the table. See the border attribute
definition in HTML 4.0.

- setBorder

```java
void setBorder​(
String
border)
```

- getCellPadding

```java
String
getCellPadding()
```

Specifies the horizontal and vertical space between cell content and
cell borders. See the cellpadding attribute definition in HTML 4.0.

- setCellPadding

```java
void setCellPadding​(
String
cellPadding)
```

- getCellSpacing

```java
String
getCellSpacing()
```

Specifies the horizontal and vertical separation between cells. See
the cellspacing attribute definition in HTML 4.0.

- setCellSpacing

```java
void setCellSpacing​(
String
cellSpacing)
```

- getFrame

```java
String
getFrame()
```

Specifies which external table borders to render. See the frame
attribute definition in HTML 4.0.

- setFrame

```java
void setFrame​(
String
frame)
```

- getRules

```java
String
getRules()
```

Specifies which internal table borders to render. See the rules
attribute definition in HTML 4.0.

- setRules

```java
void setRules​(
String
rules)
```

- getSummary

```java
String
getSummary()
```

Description about the purpose or structure of a table. See the
summary attribute definition in HTML 4.0.

- setSummary

```java
void setSummary​(
String
summary)
```

- getWidth

```java
String
getWidth()
```

Specifies the desired table width. See the width attribute definition
in HTML 4.0.

- setWidth

```java
void setWidth​(
String
width)
```

- createTHead

```java
HTMLElement
createTHead()
```

Create a table header row or return an existing one.

**Returns:** A new table header element (

THEAD

).

- deleteTHead

```java
void deleteTHead()
```

Delete the header from the table, if one exists.

- createTFoot

```java
HTMLElement
createTFoot()
```

Create a table footer row or return an existing one.

**Returns:** A footer element (

TFOOT

).

- deleteTFoot

```java
void deleteTFoot()
```

Delete the footer from the table, if one exists.

- createCaption

```java
HTMLElement
createCaption()
```

Create a new table caption object or return an existing one.

**Returns:** A

CAPTION

element.

- deleteCaption

```java
void deleteCaption()
```

Delete the table caption, if one exists.

- insertRow

```java
HTMLElement
insertRow​(int index)
throws
DOMException
```

Insert a new empty row in the table. The new row is inserted
immediately before and in the same section as the current

index

th row in the table. If

index

is equal
to the number of rows, the new row is appended. In addition, when the
table is empty the row is inserted into a

TBODY

which is
created and inserted into the table. Note. A table row cannot be empty
according to HTML 4.0 Recommendation.

**Parameters:** index

- The row number where to insert a new row. This index
starts from 0 and is relative to all the rows contained inside the
table, regardless of section parentage.
**Returns:** The newly created row.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows or if the index is negative.

- deleteRow

```java
void deleteRow​(int index)
throws
DOMException
```

Delete a table row.

**Parameters:** index

- The index of the row to be deleted. This index starts
from 0 and is relative to all the rows contained inside the table,
regardless of section parentage.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

Method Detail

- getCaption

```java
HTMLTableCaptionElement
getCaption()
```

Returns the table's

CAPTION

, or void if none exists.

- setCaption

```java
void setCaption​(
HTMLTableCaptionElement
caption)
```

- getTHead

```java
HTMLTableSectionElement
getTHead()
```

Returns the table's

THEAD

, or

null

if none
exists.

- setTHead

```java
void setTHead​(
HTMLTableSectionElement
tHead)
```

- getTFoot

```java
HTMLTableSectionElement
getTFoot()
```

Returns the table's

TFOOT

, or

null

if none
exists.

- setTFoot

```java
void setTFoot​(
HTMLTableSectionElement
tFoot)
```

- getRows

```java
HTMLCollection
getRows()
```

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

- getTBodies

```java
HTMLCollection
getTBodies()
```

Returns a collection of the defined table bodies.

- getAlign

```java
String
getAlign()
```

Specifies the table's position with respect to the rest of the
document. See the align attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setAlign

```java
void setAlign​(
String
align)
```

- getBgColor

```java
String
getBgColor()
```

Cell background color. See the bgcolor attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

- setBgColor

```java
void setBgColor​(
String
bgColor)
```

- getBorder

```java
String
getBorder()
```

The width of the border around the table. See the border attribute
definition in HTML 4.0.

- setBorder

```java
void setBorder​(
String
border)
```

- getCellPadding

```java
String
getCellPadding()
```

Specifies the horizontal and vertical space between cell content and
cell borders. See the cellpadding attribute definition in HTML 4.0.

- setCellPadding

```java
void setCellPadding​(
String
cellPadding)
```

- getCellSpacing

```java
String
getCellSpacing()
```

Specifies the horizontal and vertical separation between cells. See
the cellspacing attribute definition in HTML 4.0.

- setCellSpacing

```java
void setCellSpacing​(
String
cellSpacing)
```

- getFrame

```java
String
getFrame()
```

Specifies which external table borders to render. See the frame
attribute definition in HTML 4.0.

- setFrame

```java
void setFrame​(
String
frame)
```

- getRules

```java
String
getRules()
```

Specifies which internal table borders to render. See the rules
attribute definition in HTML 4.0.

- setRules

```java
void setRules​(
String
rules)
```

- getSummary

```java
String
getSummary()
```

Description about the purpose or structure of a table. See the
summary attribute definition in HTML 4.0.

- setSummary

```java
void setSummary​(
String
summary)
```

- getWidth

```java
String
getWidth()
```

Specifies the desired table width. See the width attribute definition
in HTML 4.0.

- setWidth

```java
void setWidth​(
String
width)
```

- createTHead

```java
HTMLElement
createTHead()
```

Create a table header row or return an existing one.

**Returns:** A new table header element (

THEAD

).

- deleteTHead

```java
void deleteTHead()
```

Delete the header from the table, if one exists.

- createTFoot

```java
HTMLElement
createTFoot()
```

Create a table footer row or return an existing one.

**Returns:** A footer element (

TFOOT

).

- deleteTFoot

```java
void deleteTFoot()
```

Delete the footer from the table, if one exists.

- createCaption

```java
HTMLElement
createCaption()
```

Create a new table caption object or return an existing one.

**Returns:** A

CAPTION

element.

- deleteCaption

```java
void deleteCaption()
```

Delete the table caption, if one exists.

- insertRow

```java
HTMLElement
insertRow​(int index)
throws
DOMException
```

Insert a new empty row in the table. The new row is inserted
immediately before and in the same section as the current

index

th row in the table. If

index

is equal
to the number of rows, the new row is appended. In addition, when the
table is empty the row is inserted into a

TBODY

which is
created and inserted into the table. Note. A table row cannot be empty
according to HTML 4.0 Recommendation.

**Parameters:** index

- The row number where to insert a new row. This index
starts from 0 and is relative to all the rows contained inside the
table, regardless of section parentage.
**Returns:** The newly created row.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows or if the index is negative.

- deleteRow

```java
void deleteRow​(int index)
throws
DOMException
```

Delete a table row.

**Parameters:** index

- The index of the row to be deleted. This index starts
from 0 and is relative to all the rows contained inside the table,
regardless of section parentage.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

---

#### Method Detail

getCaption

```java
HTMLTableCaptionElement
getCaption()
```

Returns the table's

CAPTION

, or void if none exists.

---

#### getCaption

HTMLTableCaptionElement

getCaption()

Returns the table's

CAPTION

, or void if none exists.

setCaption

```java
void setCaption​(
HTMLTableCaptionElement
caption)
```

---

#### setCaption

void setCaption​(

HTMLTableCaptionElement

caption)

getTHead

```java
HTMLTableSectionElement
getTHead()
```

Returns the table's

THEAD

, or

null

if none
exists.

---

#### getTHead

HTMLTableSectionElement

getTHead()

Returns the table's

THEAD

, or

null

if none
exists.

setTHead

```java
void setTHead​(
HTMLTableSectionElement
tHead)
```

---

#### setTHead

void setTHead​(

HTMLTableSectionElement

tHead)

getTFoot

```java
HTMLTableSectionElement
getTFoot()
```

Returns the table's

TFOOT

, or

null

if none
exists.

---

#### getTFoot

HTMLTableSectionElement

getTFoot()

Returns the table's

TFOOT

, or

null

if none
exists.

setTFoot

```java
void setTFoot​(
HTMLTableSectionElement
tFoot)
```

---

#### setTFoot

void setTFoot​(

HTMLTableSectionElement

tFoot)

getRows

```java
HTMLCollection
getRows()
```

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

---

#### getRows

HTMLCollection

getRows()

Returns a collection of all the rows in the table, including all in

THEAD

,

TFOOT

, all

TBODY

elements.

getTBodies

```java
HTMLCollection
getTBodies()
```

Returns a collection of the defined table bodies.

---

#### getTBodies

HTMLCollection

getTBodies()

Returns a collection of the defined table bodies.

getAlign

```java
String
getAlign()
```

Specifies the table's position with respect to the rest of the
document. See the align attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### getAlign

String

getAlign()

Specifies the table's position with respect to the rest of the
document. See the align attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

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

getBgColor

```java
String
getBgColor()
```

Cell background color. See the bgcolor attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

---

#### getBgColor

String

getBgColor()

Cell background color. See the bgcolor attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

setBgColor

```java
void setBgColor​(
String
bgColor)
```

---

#### setBgColor

void setBgColor​(

String

bgColor)

getBorder

```java
String
getBorder()
```

The width of the border around the table. See the border attribute
definition in HTML 4.0.

---

#### getBorder

String

getBorder()

The width of the border around the table. See the border attribute
definition in HTML 4.0.

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

getCellPadding

```java
String
getCellPadding()
```

Specifies the horizontal and vertical space between cell content and
cell borders. See the cellpadding attribute definition in HTML 4.0.

---

#### getCellPadding

String

getCellPadding()

Specifies the horizontal and vertical space between cell content and
cell borders. See the cellpadding attribute definition in HTML 4.0.

setCellPadding

```java
void setCellPadding​(
String
cellPadding)
```

---

#### setCellPadding

void setCellPadding​(

String

cellPadding)

getCellSpacing

```java
String
getCellSpacing()
```

Specifies the horizontal and vertical separation between cells. See
the cellspacing attribute definition in HTML 4.0.

---

#### getCellSpacing

String

getCellSpacing()

Specifies the horizontal and vertical separation between cells. See
the cellspacing attribute definition in HTML 4.0.

setCellSpacing

```java
void setCellSpacing​(
String
cellSpacing)
```

---

#### setCellSpacing

void setCellSpacing​(

String

cellSpacing)

getFrame

```java
String
getFrame()
```

Specifies which external table borders to render. See the frame
attribute definition in HTML 4.0.

---

#### getFrame

String

getFrame()

Specifies which external table borders to render. See the frame
attribute definition in HTML 4.0.

setFrame

```java
void setFrame​(
String
frame)
```

---

#### setFrame

void setFrame​(

String

frame)

getRules

```java
String
getRules()
```

Specifies which internal table borders to render. See the rules
attribute definition in HTML 4.0.

---

#### getRules

String

getRules()

Specifies which internal table borders to render. See the rules
attribute definition in HTML 4.0.

setRules

```java
void setRules​(
String
rules)
```

---

#### setRules

void setRules​(

String

rules)

getSummary

```java
String
getSummary()
```

Description about the purpose or structure of a table. See the
summary attribute definition in HTML 4.0.

---

#### getSummary

String

getSummary()

Description about the purpose or structure of a table. See the
summary attribute definition in HTML 4.0.

setSummary

```java
void setSummary​(
String
summary)
```

---

#### setSummary

void setSummary​(

String

summary)

getWidth

```java
String
getWidth()
```

Specifies the desired table width. See the width attribute definition
in HTML 4.0.

---

#### getWidth

String

getWidth()

Specifies the desired table width. See the width attribute definition
in HTML 4.0.

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

createTHead

```java
HTMLElement
createTHead()
```

Create a table header row or return an existing one.

**Returns:** A new table header element (

THEAD

).

---

#### createTHead

HTMLElement

createTHead()

Create a table header row or return an existing one.

deleteTHead

```java
void deleteTHead()
```

Delete the header from the table, if one exists.

---

#### deleteTHead

void deleteTHead()

Delete the header from the table, if one exists.

createTFoot

```java
HTMLElement
createTFoot()
```

Create a table footer row or return an existing one.

**Returns:** A footer element (

TFOOT

).

---

#### createTFoot

HTMLElement

createTFoot()

Create a table footer row or return an existing one.

deleteTFoot

```java
void deleteTFoot()
```

Delete the footer from the table, if one exists.

---

#### deleteTFoot

void deleteTFoot()

Delete the footer from the table, if one exists.

createCaption

```java
HTMLElement
createCaption()
```

Create a new table caption object or return an existing one.

**Returns:** A

CAPTION

element.

---

#### createCaption

HTMLElement

createCaption()

Create a new table caption object or return an existing one.

deleteCaption

```java
void deleteCaption()
```

Delete the table caption, if one exists.

---

#### deleteCaption

void deleteCaption()

Delete the table caption, if one exists.

insertRow

```java
HTMLElement
insertRow​(int index)
throws
DOMException
```

Insert a new empty row in the table. The new row is inserted
immediately before and in the same section as the current

index

th row in the table. If

index

is equal
to the number of rows, the new row is appended. In addition, when the
table is empty the row is inserted into a

TBODY

which is
created and inserted into the table. Note. A table row cannot be empty
according to HTML 4.0 Recommendation.

**Parameters:** index

- The row number where to insert a new row. This index
starts from 0 and is relative to all the rows contained inside the
table, regardless of section parentage.
**Returns:** The newly created row.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows or if the index is negative.

---

#### insertRow

HTMLElement

insertRow​(int index)
throws

DOMException

Insert a new empty row in the table. The new row is inserted
immediately before and in the same section as the current

index

th row in the table. If

index

is equal
to the number of rows, the new row is appended. In addition, when the
table is empty the row is inserted into a

TBODY

which is
created and inserted into the table. Note. A table row cannot be empty
according to HTML 4.0 Recommendation.

deleteRow

```java
void deleteRow​(int index)
throws
DOMException
```

Delete a table row.

**Parameters:** index

- The index of the row to be deleted. This index starts
from 0 and is relative to all the rows contained inside the table,
regardless of section parentage.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

---

#### deleteRow

void deleteRow​(int index)
throws

DOMException

Delete a table row.

---

