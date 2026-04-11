# Interface HTMLTableCellElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLTableCellElement.html`

### Class Description

```java
public interface
HTMLTableCellElement

extends
HTMLElement
```

The object used to represent the

TH

and

TD

elements. See the TD element definition in HTML 4.0.

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

#### int getCellIndex()

The index of this cell in the row, starting from 0. This index is in
document tree order and not display order.

---

#### String
getAbbr()

Abbreviation for header cells. See the abbr attribute definition in
HTML 4.0.

---

#### void setAbbr​(
String
abbr)

*No description found.*

---

#### String
getAlign()

Horizontal alignment of data in cell. See the align attribute
definition in HTML 4.0.

---

#### void setAlign​(
String
align)

*No description found.*

---

#### String
getAxis()

Names group of related headers. See the axis attribute definition in
HTML 4.0.

---

#### void setAxis​(
String
axis)

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
getCh()

Alignment character for cells in a column. See the char attribute
definition in HTML 4.0.

---

#### void setCh​(
String
ch)

*No description found.*

---

#### String
getChOff()

Offset of alignment character. See the charoff attribute definition
in HTML 4.0.

---

#### void setChOff​(
String
chOff)

*No description found.*

---

#### int getColSpan()

Number of columns spanned by cell. See the colspan attribute
definition in HTML 4.0.

---

#### void setColSpan​(int colSpan)

*No description found.*

---

#### String
getHeaders()

List of

id

attribute values for header cells. See the
headers attribute definition in HTML 4.0.

---

#### void setHeaders​(
String
headers)

*No description found.*

---

#### String
getHeight()

Cell height. See the height attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### void setHeight​(
String
height)

*No description found.*

---

#### boolean getNoWrap()

Suppress word wrapping. See the nowrap attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

---

#### void setNoWrap​(boolean noWrap)

*No description found.*

---

#### int getRowSpan()

Number of rows spanned by cell. See the rowspan attribute definition
in HTML 4.0.

---

#### void setRowSpan​(int rowSpan)

*No description found.*

---

#### String
getScope()

Scope covered by header cells. See the scope attribute definition in
HTML 4.0.

---

#### void setScope​(
String
scope)

*No description found.*

---

#### String
getVAlign()

Vertical alignment of data in cell. See the valign attribute
definition in HTML 4.0.

---

#### void setVAlign​(
String
vAlign)

*No description found.*

---

#### String
getWidth()

Cell width. See the width attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### void setWidth​(
String
width)

*No description found.*

---

### Additional Sections

#### Interface HTMLTableCellElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLTableCellElement

extends
HTMLElement
```

The object used to represent the

TH

and

TD

elements. See the TD element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLTableCellElement

extends

HTMLElement

The object used to represent the

TH

and

TD

elements. See the TD element definition in HTML 4.0.

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

getAbbr

()

Abbreviation for header cells.

String

getAlign

()

Horizontal alignment of data in cell.

String

getAxis

()

Names group of related headers.

String

getBgColor

()

Cell background color.

int

getCellIndex

()

The index of this cell in the row, starting from 0.

String

getCh

()

Alignment character for cells in a column.

String

getChOff

()

Offset of alignment character.

int

getColSpan

()

Number of columns spanned by cell.

String

getHeaders

()

List of

id

attribute values for header cells.

String

getHeight

()

Cell height.

boolean

getNoWrap

()

Suppress word wrapping.

int

getRowSpan

()

Number of rows spanned by cell.

String

getScope

()

Scope covered by header cells.

String

getVAlign

()

Vertical alignment of data in cell.

String

getWidth

()

Cell width.

void

setAbbr

​(

String

abbr)

void

setAlign

​(

String

align)

void

setAxis

​(

String

axis)

void

setBgColor

​(

String

bgColor)

void

setCh

​(

String

ch)

void

setChOff

​(

String

chOff)

void

setColSpan

​(int colSpan)

void

setHeaders

​(

String

headers)

void

setHeight

​(

String

height)

void

setNoWrap

​(boolean noWrap)

void

setRowSpan

​(int rowSpan)

void

setScope

​(

String

scope)

void

setVAlign

​(

String

vAlign)

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

getAbbr

()

Abbreviation for header cells.

String

getAlign

()

Horizontal alignment of data in cell.

String

getAxis

()

Names group of related headers.

String

getBgColor

()

Cell background color.

int

getCellIndex

()

The index of this cell in the row, starting from 0.

String

getCh

()

Alignment character for cells in a column.

String

getChOff

()

Offset of alignment character.

int

getColSpan

()

Number of columns spanned by cell.

String

getHeaders

()

List of

id

attribute values for header cells.

String

getHeight

()

Cell height.

boolean

getNoWrap

()

Suppress word wrapping.

int

getRowSpan

()

Number of rows spanned by cell.

String

getScope

()

Scope covered by header cells.

String

getVAlign

()

Vertical alignment of data in cell.

String

getWidth

()

Cell width.

void

setAbbr

​(

String

abbr)

void

setAlign

​(

String

align)

void

setAxis

​(

String

axis)

void

setBgColor

​(

String

bgColor)

void

setCh

​(

String

ch)

void

setChOff

​(

String

chOff)

void

setColSpan

​(int colSpan)

void

setHeaders

​(

String

headers)

void

setHeight

​(

String

height)

void

setNoWrap

​(boolean noWrap)

void

setRowSpan

​(int rowSpan)

void

setScope

​(

String

scope)

void

setVAlign

​(

String

vAlign)

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

Abbreviation for header cells.

Horizontal alignment of data in cell.

Names group of related headers.

Cell background color.

The index of this cell in the row, starting from 0.

Alignment character for cells in a column.

Offset of alignment character.

Number of columns spanned by cell.

List of

id

attribute values for header cells.

Cell height.

Suppress word wrapping.

Number of rows spanned by cell.

Scope covered by header cells.

Vertical alignment of data in cell.

Cell width.

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

- getCellIndex

```java
int getCellIndex()
```

The index of this cell in the row, starting from 0. This index is in
document tree order and not display order.

- getAbbr

```java
String
getAbbr()
```

Abbreviation for header cells. See the abbr attribute definition in
HTML 4.0.

- setAbbr

```java
void setAbbr​(
String
abbr)
```

- getAlign

```java
String
getAlign()
```

Horizontal alignment of data in cell. See the align attribute
definition in HTML 4.0.

- setAlign

```java
void setAlign​(
String
align)
```

- getAxis

```java
String
getAxis()
```

Names group of related headers. See the axis attribute definition in
HTML 4.0.

- setAxis

```java
void setAxis​(
String
axis)
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

- getCh

```java
String
getCh()
```

Alignment character for cells in a column. See the char attribute
definition in HTML 4.0.

- setCh

```java
void setCh​(
String
ch)
```

- getChOff

```java
String
getChOff()
```

Offset of alignment character. See the charoff attribute definition
in HTML 4.0.

- setChOff

```java
void setChOff​(
String
chOff)
```

- getColSpan

```java
int getColSpan()
```

Number of columns spanned by cell. See the colspan attribute
definition in HTML 4.0.

- setColSpan

```java
void setColSpan​(int colSpan)
```

- getHeaders

```java
String
getHeaders()
```

List of

id

attribute values for header cells. See the
headers attribute definition in HTML 4.0.

- setHeaders

```java
void setHeaders​(
String
headers)
```

- getHeight

```java
String
getHeight()
```

Cell height. See the height attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setHeight

```java
void setHeight​(
String
height)
```

- getNoWrap

```java
boolean getNoWrap()
```

Suppress word wrapping. See the nowrap attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

- setNoWrap

```java
void setNoWrap​(boolean noWrap)
```

- getRowSpan

```java
int getRowSpan()
```

Number of rows spanned by cell. See the rowspan attribute definition
in HTML 4.0.

- setRowSpan

```java
void setRowSpan​(int rowSpan)
```

- getScope

```java
String
getScope()
```

Scope covered by header cells. See the scope attribute definition in
HTML 4.0.

- setScope

```java
void setScope​(
String
scope)
```

- getVAlign

```java
String
getVAlign()
```

Vertical alignment of data in cell. See the valign attribute
definition in HTML 4.0.

- setVAlign

```java
void setVAlign​(
String
vAlign)
```

- getWidth

```java
String
getWidth()
```

Cell width. See the width attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setWidth

```java
void setWidth​(
String
width)
```

Method Detail

- getCellIndex

```java
int getCellIndex()
```

The index of this cell in the row, starting from 0. This index is in
document tree order and not display order.

- getAbbr

```java
String
getAbbr()
```

Abbreviation for header cells. See the abbr attribute definition in
HTML 4.0.

- setAbbr

```java
void setAbbr​(
String
abbr)
```

- getAlign

```java
String
getAlign()
```

Horizontal alignment of data in cell. See the align attribute
definition in HTML 4.0.

- setAlign

```java
void setAlign​(
String
align)
```

- getAxis

```java
String
getAxis()
```

Names group of related headers. See the axis attribute definition in
HTML 4.0.

- setAxis

```java
void setAxis​(
String
axis)
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

- getCh

```java
String
getCh()
```

Alignment character for cells in a column. See the char attribute
definition in HTML 4.0.

- setCh

```java
void setCh​(
String
ch)
```

- getChOff

```java
String
getChOff()
```

Offset of alignment character. See the charoff attribute definition
in HTML 4.0.

- setChOff

```java
void setChOff​(
String
chOff)
```

- getColSpan

```java
int getColSpan()
```

Number of columns spanned by cell. See the colspan attribute
definition in HTML 4.0.

- setColSpan

```java
void setColSpan​(int colSpan)
```

- getHeaders

```java
String
getHeaders()
```

List of

id

attribute values for header cells. See the
headers attribute definition in HTML 4.0.

- setHeaders

```java
void setHeaders​(
String
headers)
```

- getHeight

```java
String
getHeight()
```

Cell height. See the height attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setHeight

```java
void setHeight​(
String
height)
```

- getNoWrap

```java
boolean getNoWrap()
```

Suppress word wrapping. See the nowrap attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

- setNoWrap

```java
void setNoWrap​(boolean noWrap)
```

- getRowSpan

```java
int getRowSpan()
```

Number of rows spanned by cell. See the rowspan attribute definition
in HTML 4.0.

- setRowSpan

```java
void setRowSpan​(int rowSpan)
```

- getScope

```java
String
getScope()
```

Scope covered by header cells. See the scope attribute definition in
HTML 4.0.

- setScope

```java
void setScope​(
String
scope)
```

- getVAlign

```java
String
getVAlign()
```

Vertical alignment of data in cell. See the valign attribute
definition in HTML 4.0.

- setVAlign

```java
void setVAlign​(
String
vAlign)
```

- getWidth

```java
String
getWidth()
```

Cell width. See the width attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

- setWidth

```java
void setWidth​(
String
width)
```

---

#### Method Detail

getCellIndex

```java
int getCellIndex()
```

The index of this cell in the row, starting from 0. This index is in
document tree order and not display order.

---

#### getCellIndex

int getCellIndex()

The index of this cell in the row, starting from 0. This index is in
document tree order and not display order.

getAbbr

```java
String
getAbbr()
```

Abbreviation for header cells. See the abbr attribute definition in
HTML 4.0.

---

#### getAbbr

String

getAbbr()

Abbreviation for header cells. See the abbr attribute definition in
HTML 4.0.

setAbbr

```java
void setAbbr​(
String
abbr)
```

---

#### setAbbr

void setAbbr​(

String

abbr)

getAlign

```java
String
getAlign()
```

Horizontal alignment of data in cell. See the align attribute
definition in HTML 4.0.

---

#### getAlign

String

getAlign()

Horizontal alignment of data in cell. See the align attribute
definition in HTML 4.0.

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

getAxis

```java
String
getAxis()
```

Names group of related headers. See the axis attribute definition in
HTML 4.0.

---

#### getAxis

String

getAxis()

Names group of related headers. See the axis attribute definition in
HTML 4.0.

setAxis

```java
void setAxis​(
String
axis)
```

---

#### setAxis

void setAxis​(

String

axis)

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

getCh

```java
String
getCh()
```

Alignment character for cells in a column. See the char attribute
definition in HTML 4.0.

---

#### getCh

String

getCh()

Alignment character for cells in a column. See the char attribute
definition in HTML 4.0.

setCh

```java
void setCh​(
String
ch)
```

---

#### setCh

void setCh​(

String

ch)

getChOff

```java
String
getChOff()
```

Offset of alignment character. See the charoff attribute definition
in HTML 4.0.

---

#### getChOff

String

getChOff()

Offset of alignment character. See the charoff attribute definition
in HTML 4.0.

setChOff

```java
void setChOff​(
String
chOff)
```

---

#### setChOff

void setChOff​(

String

chOff)

getColSpan

```java
int getColSpan()
```

Number of columns spanned by cell. See the colspan attribute
definition in HTML 4.0.

---

#### getColSpan

int getColSpan()

Number of columns spanned by cell. See the colspan attribute
definition in HTML 4.0.

setColSpan

```java
void setColSpan​(int colSpan)
```

---

#### setColSpan

void setColSpan​(int colSpan)

getHeaders

```java
String
getHeaders()
```

List of

id

attribute values for header cells. See the
headers attribute definition in HTML 4.0.

---

#### getHeaders

String

getHeaders()

List of

id

attribute values for header cells. See the
headers attribute definition in HTML 4.0.

setHeaders

```java
void setHeaders​(
String
headers)
```

---

#### setHeaders

void setHeaders​(

String

headers)

getHeight

```java
String
getHeight()
```

Cell height. See the height attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### getHeight

String

getHeight()

Cell height. See the height attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

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

getNoWrap

```java
boolean getNoWrap()
```

Suppress word wrapping. See the nowrap attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

---

#### getNoWrap

boolean getNoWrap()

Suppress word wrapping. See the nowrap attribute definition in HTML
4.0. This attribute is deprecated in HTML 4.0.

setNoWrap

```java
void setNoWrap​(boolean noWrap)
```

---

#### setNoWrap

void setNoWrap​(boolean noWrap)

getRowSpan

```java
int getRowSpan()
```

Number of rows spanned by cell. See the rowspan attribute definition
in HTML 4.0.

---

#### getRowSpan

int getRowSpan()

Number of rows spanned by cell. See the rowspan attribute definition
in HTML 4.0.

setRowSpan

```java
void setRowSpan​(int rowSpan)
```

---

#### setRowSpan

void setRowSpan​(int rowSpan)

getScope

```java
String
getScope()
```

Scope covered by header cells. See the scope attribute definition in
HTML 4.0.

---

#### getScope

String

getScope()

Scope covered by header cells. See the scope attribute definition in
HTML 4.0.

setScope

```java
void setScope​(
String
scope)
```

---

#### setScope

void setScope​(

String

scope)

getVAlign

```java
String
getVAlign()
```

Vertical alignment of data in cell. See the valign attribute
definition in HTML 4.0.

---

#### getVAlign

String

getVAlign()

Vertical alignment of data in cell. See the valign attribute
definition in HTML 4.0.

setVAlign

```java
void setVAlign​(
String
vAlign)
```

---

#### setVAlign

void setVAlign​(

String

vAlign)

getWidth

```java
String
getWidth()
```

Cell width. See the width attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

---

#### getWidth

String

getWidth()

Cell width. See the width attribute definition in HTML 4.0. This
attribute is deprecated in HTML 4.0.

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

