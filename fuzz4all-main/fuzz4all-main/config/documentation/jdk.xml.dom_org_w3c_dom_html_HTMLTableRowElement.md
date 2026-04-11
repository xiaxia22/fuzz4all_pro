# Interface HTMLTableRowElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLTableRowElement.html`

### Class Description

```java
public interface
HTMLTableRowElement

extends
HTMLElement
```

A row in a table. See the TR element definition in HTML 4.0.

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

#### int getRowIndex()

The index of this row, relative to the entire table, starting from 0.
This is in document tree order and not display order. The

rowIndex

does not take into account sections (

THEAD

,

TFOOT

, or

TBODY

)
within the table.

---

#### int getSectionRowIndex()

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

---

#### HTMLCollection
getCells()

The collection of cells in this row.

---

#### String
getAlign()

Horizontal alignment of data within cells of this row. See the align
attribute definition in HTML 4.0.

---

#### void setAlign​(
String
align)

*No description found.*

---

#### String
getBgColor()

Background color for rows. See the bgcolor attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

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

#### String
getVAlign()

Vertical alignment of data within cells of this row. See the valign
attribute definition in HTML 4.0.

---

#### void setVAlign​(
String
vAlign)

*No description found.*

---

#### HTMLElement
insertCell​(int index)
throws
DOMException

Insert an empty

TD

cell into this row. If

index

is equal to the number of cells, the new cell is
appended

**Parameters:**
- index

- The place to insert the cell, starting from 0.

**Returns:**
- The newly created cell.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than the number of cells or if the index is negative.

---

#### void deleteCell​(int index)
throws
DOMException

Delete a cell from the current row.

**Parameters:**
- index

- The index of the cell to delete, starting from 0.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than or equal to the number of cells or if the index is
negative.

---

### Additional Sections

#### Interface HTMLTableRowElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLTableRowElement

extends
HTMLElement
```

A row in a table. See the TR element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLTableRowElement

extends

HTMLElement

A row in a table. See the TR element definition in HTML 4.0.

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

deleteCell

​(int index)

Delete a cell from the current row.

String

getAlign

()

Horizontal alignment of data within cells of this row.

String

getBgColor

()

Background color for rows.

HTMLCollection

getCells

()

The collection of cells in this row.

String

getCh

()

Alignment character for cells in a column.

String

getChOff

()

Offset of alignment character.

int

getRowIndex

()

The index of this row, relative to the entire table, starting from 0.

int

getSectionRowIndex

()

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

String

getVAlign

()

Vertical alignment of data within cells of this row.

HTMLElement

insertCell

​(int index)

Insert an empty

TD

cell into this row.

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

setVAlign

​(

String

vAlign)

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

deleteCell

​(int index)

Delete a cell from the current row.

String

getAlign

()

Horizontal alignment of data within cells of this row.

String

getBgColor

()

Background color for rows.

HTMLCollection

getCells

()

The collection of cells in this row.

String

getCh

()

Alignment character for cells in a column.

String

getChOff

()

Offset of alignment character.

int

getRowIndex

()

The index of this row, relative to the entire table, starting from 0.

int

getSectionRowIndex

()

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

String

getVAlign

()

Vertical alignment of data within cells of this row.

HTMLElement

insertCell

​(int index)

Insert an empty

TD

cell into this row.

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

setVAlign

​(

String

vAlign)

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

Delete a cell from the current row.

Horizontal alignment of data within cells of this row.

Background color for rows.

The collection of cells in this row.

Alignment character for cells in a column.

Offset of alignment character.

The index of this row, relative to the entire table, starting from 0.

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

Vertical alignment of data within cells of this row.

Insert an empty

TD

cell into this row.

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

- getRowIndex

```java
int getRowIndex()
```

The index of this row, relative to the entire table, starting from 0.
This is in document tree order and not display order. The

rowIndex

does not take into account sections (

THEAD

,

TFOOT

, or

TBODY

)
within the table.

- getSectionRowIndex

```java
int getSectionRowIndex()
```

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

- getCells

```java
HTMLCollection
getCells()
```

The collection of cells in this row.

- getAlign

```java
String
getAlign()
```

Horizontal alignment of data within cells of this row. See the align
attribute definition in HTML 4.0.

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

Background color for rows. See the bgcolor attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

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

- getVAlign

```java
String
getVAlign()
```

Vertical alignment of data within cells of this row. See the valign
attribute definition in HTML 4.0.

- setVAlign

```java
void setVAlign​(
String
vAlign)
```

- insertCell

```java
HTMLElement
insertCell​(int index)
throws
DOMException
```

Insert an empty

TD

cell into this row. If

index

is equal to the number of cells, the new cell is
appended

**Parameters:** index

- The place to insert the cell, starting from 0.
**Returns:** The newly created cell.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than the number of cells or if the index is negative.

- deleteCell

```java
void deleteCell​(int index)
throws
DOMException
```

Delete a cell from the current row.

**Parameters:** index

- The index of the cell to delete, starting from 0.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than or equal to the number of cells or if the index is
negative.

Method Detail

- getRowIndex

```java
int getRowIndex()
```

The index of this row, relative to the entire table, starting from 0.
This is in document tree order and not display order. The

rowIndex

does not take into account sections (

THEAD

,

TFOOT

, or

TBODY

)
within the table.

- getSectionRowIndex

```java
int getSectionRowIndex()
```

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

- getCells

```java
HTMLCollection
getCells()
```

The collection of cells in this row.

- getAlign

```java
String
getAlign()
```

Horizontal alignment of data within cells of this row. See the align
attribute definition in HTML 4.0.

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

Background color for rows. See the bgcolor attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

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

- getVAlign

```java
String
getVAlign()
```

Vertical alignment of data within cells of this row. See the valign
attribute definition in HTML 4.0.

- setVAlign

```java
void setVAlign​(
String
vAlign)
```

- insertCell

```java
HTMLElement
insertCell​(int index)
throws
DOMException
```

Insert an empty

TD

cell into this row. If

index

is equal to the number of cells, the new cell is
appended

**Parameters:** index

- The place to insert the cell, starting from 0.
**Returns:** The newly created cell.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than the number of cells or if the index is negative.

- deleteCell

```java
void deleteCell​(int index)
throws
DOMException
```

Delete a cell from the current row.

**Parameters:** index

- The index of the cell to delete, starting from 0.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than or equal to the number of cells or if the index is
negative.

---

#### Method Detail

getRowIndex

```java
int getRowIndex()
```

The index of this row, relative to the entire table, starting from 0.
This is in document tree order and not display order. The

rowIndex

does not take into account sections (

THEAD

,

TFOOT

, or

TBODY

)
within the table.

---

#### getRowIndex

int getRowIndex()

The index of this row, relative to the entire table, starting from 0.
This is in document tree order and not display order. The

rowIndex

does not take into account sections (

THEAD

,

TFOOT

, or

TBODY

)
within the table.

getSectionRowIndex

```java
int getSectionRowIndex()
```

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

---

#### getSectionRowIndex

int getSectionRowIndex()

The index of this row, relative to the current section (

THEAD

,

TFOOT

, or

TBODY

),
starting from 0.

getCells

```java
HTMLCollection
getCells()
```

The collection of cells in this row.

---

#### getCells

HTMLCollection

getCells()

The collection of cells in this row.

getAlign

```java
String
getAlign()
```

Horizontal alignment of data within cells of this row. See the align
attribute definition in HTML 4.0.

---

#### getAlign

String

getAlign()

Horizontal alignment of data within cells of this row. See the align
attribute definition in HTML 4.0.

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

Background color for rows. See the bgcolor attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

---

#### getBgColor

String

getBgColor()

Background color for rows. See the bgcolor attribute definition in
HTML 4.0. This attribute is deprecated in HTML 4.0.

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

getVAlign

```java
String
getVAlign()
```

Vertical alignment of data within cells of this row. See the valign
attribute definition in HTML 4.0.

---

#### getVAlign

String

getVAlign()

Vertical alignment of data within cells of this row. See the valign
attribute definition in HTML 4.0.

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

insertCell

```java
HTMLElement
insertCell​(int index)
throws
DOMException
```

Insert an empty

TD

cell into this row. If

index

is equal to the number of cells, the new cell is
appended

**Parameters:** index

- The place to insert the cell, starting from 0.
**Returns:** The newly created cell.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than the number of cells or if the index is negative.

---

#### insertCell

HTMLElement

insertCell​(int index)
throws

DOMException

Insert an empty

TD

cell into this row. If

index

is equal to the number of cells, the new cell is
appended

deleteCell

```java
void deleteCell​(int index)
throws
DOMException
```

Delete a cell from the current row.

**Parameters:** index

- The index of the cell to delete, starting from 0.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified

index

is
greater than or equal to the number of cells or if the index is
negative.

---

#### deleteCell

void deleteCell​(int index)
throws

DOMException

Delete a cell from the current row.

---

