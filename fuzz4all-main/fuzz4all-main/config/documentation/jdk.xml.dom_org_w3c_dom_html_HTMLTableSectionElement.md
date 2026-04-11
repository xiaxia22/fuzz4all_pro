# Interface HTMLTableSectionElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLTableSectionElement.html`

### Class Description

```java
public interface
HTMLTableSectionElement

extends
HTMLElement
```

The

THEAD

,

TFOOT

, and

TBODY

elements.

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
getAlign()

Horizontal alignment of data in cells. See the

align

attribute for HTMLTheadElement for details.

---

#### void setAlign​(
String
align)

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

Vertical alignment of data in cells. See the

valign

attribute for HTMLTheadElement for details.

---

#### void setVAlign​(
String
vAlign)

*No description found.*

---

#### HTMLCollection
getRows()

The collection of rows in this table section.

---

#### HTMLElement
insertRow​(int index)
throws
DOMException

Insert a row into this section. The new row is inserted immediately
before the current

index

th row in this section. If

index

is equal to the number of rows in this section, the
new row is appended.

**Parameters:**
- index

- The row number where to insert a new row. This index
starts from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.

**Returns:**
- The newly created row.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows of if the index is neagative.

---

#### void deleteRow​(int index)
throws
DOMException

Delete a row from this section.

**Parameters:**
- index

- The index of the row to be deleted. This index starts
from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

---

### Additional Sections

#### Interface HTMLTableSectionElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLTableSectionElement

extends
HTMLElement
```

The

THEAD

,

TFOOT

, and

TBODY

elements.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLTableSectionElement

extends

HTMLElement

The

THEAD

,

TFOOT

, and

TBODY

elements.

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

deleteRow

​(int index)

Delete a row from this section.

String

getAlign

()

Horizontal alignment of data in cells.

String

getCh

()

Alignment character for cells in a column.

String

getChOff

()

Offset of alignment character.

HTMLCollection

getRows

()

The collection of rows in this table section.

String

getVAlign

()

Vertical alignment of data in cells.

HTMLElement

insertRow

​(int index)

Insert a row into this section.

void

setAlign

​(

String

align)

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

deleteRow

​(int index)

Delete a row from this section.

String

getAlign

()

Horizontal alignment of data in cells.

String

getCh

()

Alignment character for cells in a column.

String

getChOff

()

Offset of alignment character.

HTMLCollection

getRows

()

The collection of rows in this table section.

String

getVAlign

()

Vertical alignment of data in cells.

HTMLElement

insertRow

​(int index)

Insert a row into this section.

void

setAlign

​(

String

align)

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

Delete a row from this section.

Horizontal alignment of data in cells.

Alignment character for cells in a column.

Offset of alignment character.

The collection of rows in this table section.

Vertical alignment of data in cells.

Insert a row into this section.

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

- getAlign

```java
String
getAlign()
```

Horizontal alignment of data in cells. See the

align

attribute for HTMLTheadElement for details.

- setAlign

```java
void setAlign​(
String
align)
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

Vertical alignment of data in cells. See the

valign

attribute for HTMLTheadElement for details.

- setVAlign

```java
void setVAlign​(
String
vAlign)
```

- getRows

```java
HTMLCollection
getRows()
```

The collection of rows in this table section.

- insertRow

```java
HTMLElement
insertRow​(int index)
throws
DOMException
```

Insert a row into this section. The new row is inserted immediately
before the current

index

th row in this section. If

index

is equal to the number of rows in this section, the
new row is appended.

**Parameters:** index

- The row number where to insert a new row. This index
starts from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.
**Returns:** The newly created row.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows of if the index is neagative.

- deleteRow

```java
void deleteRow​(int index)
throws
DOMException
```

Delete a row from this section.

**Parameters:** index

- The index of the row to be deleted. This index starts
from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

Method Detail

- getAlign

```java
String
getAlign()
```

Horizontal alignment of data in cells. See the

align

attribute for HTMLTheadElement for details.

- setAlign

```java
void setAlign​(
String
align)
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

Vertical alignment of data in cells. See the

valign

attribute for HTMLTheadElement for details.

- setVAlign

```java
void setVAlign​(
String
vAlign)
```

- getRows

```java
HTMLCollection
getRows()
```

The collection of rows in this table section.

- insertRow

```java
HTMLElement
insertRow​(int index)
throws
DOMException
```

Insert a row into this section. The new row is inserted immediately
before the current

index

th row in this section. If

index

is equal to the number of rows in this section, the
new row is appended.

**Parameters:** index

- The row number where to insert a new row. This index
starts from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.
**Returns:** The newly created row.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows of if the index is neagative.

- deleteRow

```java
void deleteRow​(int index)
throws
DOMException
```

Delete a row from this section.

**Parameters:** index

- The index of the row to be deleted. This index starts
from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

---

#### Method Detail

getAlign

```java
String
getAlign()
```

Horizontal alignment of data in cells. See the

align

attribute for HTMLTheadElement for details.

---

#### getAlign

String

getAlign()

Horizontal alignment of data in cells. See the

align

attribute for HTMLTheadElement for details.

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

Vertical alignment of data in cells. See the

valign

attribute for HTMLTheadElement for details.

---

#### getVAlign

String

getVAlign()

Vertical alignment of data in cells. See the

valign

attribute for HTMLTheadElement for details.

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

getRows

```java
HTMLCollection
getRows()
```

The collection of rows in this table section.

---

#### getRows

HTMLCollection

getRows()

The collection of rows in this table section.

insertRow

```java
HTMLElement
insertRow​(int index)
throws
DOMException
```

Insert a row into this section. The new row is inserted immediately
before the current

index

th row in this section. If

index

is equal to the number of rows in this section, the
new row is appended.

**Parameters:** index

- The row number where to insert a new row. This index
starts from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.
**Returns:** The newly created row.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than the
number of rows of if the index is neagative.

---

#### insertRow

HTMLElement

insertRow​(int index)
throws

DOMException

Insert a row into this section. The new row is inserted immediately
before the current

index

th row in this section. If

index

is equal to the number of rows in this section, the
new row is appended.

deleteRow

```java
void deleteRow​(int index)
throws
DOMException
```

Delete a row from this section.

**Parameters:** index

- The index of the row to be deleted. This index starts
from 0 and is relative only to the rows contained inside this
section, not all the rows in the table.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index is greater than or
equal to the number of rows or if the index is negative.

---

#### deleteRow

void deleteRow​(int index)
throws

DOMException

Delete a row from this section.

---

