# Interface HTMLElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLElement.html`

### Class Description

```java
public interface
HTMLElement

extends
Element
```

All HTML element interfaces derive from this class. Elements that only
expose the HTML core attributes are represented by the base

HTMLElement

interface. These elements are as follows: HEAD
special: SUB, SUP, SPAN, BDO font: TT, I, B, U, S, STRIKE, BIG, SMALL
phrase: EM, STRONG, DFN, CODE, SAMP, KBD, VAR, CITE, ACRONYM, ABBR list:
DD, DT NOFRAMES, NOSCRIPT ADDRESS, CENTER The

style

attribute
of an HTML element is accessible through the

ElementCSSInlineStyle

interface which is defined in the .

See also the

Document Object Model (DOM) Level 2 Specification

.

**All Superinterfaces:** Element

,

Node

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getId()

The element's identifier. See the id attribute definition in HTML 4.0.

---

#### void setId​(
String
id)

*No description found.*

---

#### String
getTitle()

The element's advisory title. See the title attribute definition in
HTML 4.0.

---

#### void setTitle​(
String
title)

*No description found.*

---

#### String
getLang()

Language code defined in RFC 1766. See the lang attribute definition
in HTML 4.0.

---

#### void setLang​(
String
lang)

*No description found.*

---

#### String
getDir()

Specifies the base direction of directionally neutral text and the
directionality of tables. See the dir attribute definition in HTML
4.0.

---

#### void setDir​(
String
dir)

*No description found.*

---

#### String
getClassName()

The class attribute of the element. This attribute has been renamed
due to conflicts with the "class" keyword exposed by many languages.
See the class attribute definition in HTML 4.0.

---

#### void setClassName​(
String
className)

*No description found.*

---

### Additional Sections

#### Interface HTMLElement

**All Superinterfaces:** Element

,

Node

**All Known Subinterfaces:** HTMLAnchorElement

,

HTMLAppletElement

,

HTMLAreaElement

,

HTMLBaseElement

,

HTMLBaseFontElement

,

HTMLBodyElement

,

HTMLBRElement

,

HTMLButtonElement

,

HTMLDirectoryElement

,

HTMLDivElement

,

HTMLDListElement

,

HTMLFieldSetElement

,

HTMLFontElement

,

HTMLFormElement

,

HTMLFrameElement

,

HTMLFrameSetElement

,

HTMLHeadElement

,

HTMLHeadingElement

,

HTMLHRElement

,

HTMLHtmlElement

,

HTMLIFrameElement

,

HTMLImageElement

,

HTMLInputElement

,

HTMLIsIndexElement

,

HTMLLabelElement

,

HTMLLegendElement

,

HTMLLIElement

,

HTMLLinkElement

,

HTMLMapElement

,

HTMLMenuElement

,

HTMLMetaElement

,

HTMLModElement

,

HTMLObjectElement

,

HTMLOListElement

,

HTMLOptGroupElement

,

HTMLOptionElement

,

HTMLParagraphElement

,

HTMLParamElement

,

HTMLPreElement

,

HTMLQuoteElement

,

HTMLScriptElement

,

HTMLSelectElement

,

HTMLStyleElement

,

HTMLTableCaptionElement

,

HTMLTableCellElement

,

HTMLTableColElement

,

HTMLTableElement

,

HTMLTableRowElement

,

HTMLTableSectionElement

,

HTMLTextAreaElement

,

HTMLTitleElement

,

HTMLUListElement

```java
public interface
HTMLElement

extends
Element
```

All HTML element interfaces derive from this class. Elements that only
expose the HTML core attributes are represented by the base

HTMLElement

interface. These elements are as follows: HEAD
special: SUB, SUP, SPAN, BDO font: TT, I, B, U, S, STRIKE, BIG, SMALL
phrase: EM, STRONG, DFN, CODE, SAMP, KBD, VAR, CITE, ACRONYM, ABBR list:
DD, DT NOFRAMES, NOSCRIPT ADDRESS, CENTER The

style

attribute
of an HTML element is accessible through the

ElementCSSInlineStyle

interface which is defined in the .

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLElement

extends

Element

All HTML element interfaces derive from this class. Elements that only
expose the HTML core attributes are represented by the base

HTMLElement

interface. These elements are as follows: HEAD
special: SUB, SUP, SPAN, BDO font: TT, I, B, U, S, STRIKE, BIG, SMALL
phrase: EM, STRONG, DFN, CODE, SAMP, KBD, VAR, CITE, ACRONYM, ABBR list:
DD, DT NOFRAMES, NOSCRIPT ADDRESS, CENTER The

style

attribute
of an HTML element is accessible through the

ElementCSSInlineStyle

interface which is defined in the .

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

getClassName

()

The class attribute of the element.

String

getDir

()

Specifies the base direction of directionally neutral text and the
directionality of tables.

String

getId

()

The element's identifier.

String

getLang

()

Language code defined in RFC 1766.

String

getTitle

()

The element's advisory title.

void

setClassName

​(

String

className)

void

setDir

​(

String

dir)

void

setId

​(

String

id)

void

setLang

​(

String

lang)

void

setTitle

​(

String

title)

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

getClassName

()

The class attribute of the element.

String

getDir

()

Specifies the base direction of directionally neutral text and the
directionality of tables.

String

getId

()

The element's identifier.

String

getLang

()

Language code defined in RFC 1766.

String

getTitle

()

The element's advisory title.

void

setClassName

​(

String

className)

void

setDir

​(

String

dir)

void

setId

​(

String

id)

void

setLang

​(

String

lang)

void

setTitle

​(

String

title)

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

The class attribute of the element.

Specifies the base direction of directionally neutral text and the
directionality of tables.

The element's identifier.

Language code defined in RFC 1766.

The element's advisory title.

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

- getId

```java
String
getId()
```

The element's identifier. See the id attribute definition in HTML 4.0.

- setId

```java
void setId​(
String
id)
```

- getTitle

```java
String
getTitle()
```

The element's advisory title. See the title attribute definition in
HTML 4.0.

- setTitle

```java
void setTitle​(
String
title)
```

- getLang

```java
String
getLang()
```

Language code defined in RFC 1766. See the lang attribute definition
in HTML 4.0.

- setLang

```java
void setLang​(
String
lang)
```

- getDir

```java
String
getDir()
```

Specifies the base direction of directionally neutral text and the
directionality of tables. See the dir attribute definition in HTML
4.0.

- setDir

```java
void setDir​(
String
dir)
```

- getClassName

```java
String
getClassName()
```

The class attribute of the element. This attribute has been renamed
due to conflicts with the "class" keyword exposed by many languages.
See the class attribute definition in HTML 4.0.

- setClassName

```java
void setClassName​(
String
className)
```

Method Detail

- getId

```java
String
getId()
```

The element's identifier. See the id attribute definition in HTML 4.0.

- setId

```java
void setId​(
String
id)
```

- getTitle

```java
String
getTitle()
```

The element's advisory title. See the title attribute definition in
HTML 4.0.

- setTitle

```java
void setTitle​(
String
title)
```

- getLang

```java
String
getLang()
```

Language code defined in RFC 1766. See the lang attribute definition
in HTML 4.0.

- setLang

```java
void setLang​(
String
lang)
```

- getDir

```java
String
getDir()
```

Specifies the base direction of directionally neutral text and the
directionality of tables. See the dir attribute definition in HTML
4.0.

- setDir

```java
void setDir​(
String
dir)
```

- getClassName

```java
String
getClassName()
```

The class attribute of the element. This attribute has been renamed
due to conflicts with the "class" keyword exposed by many languages.
See the class attribute definition in HTML 4.0.

- setClassName

```java
void setClassName​(
String
className)
```

---

#### Method Detail

getId

```java
String
getId()
```

The element's identifier. See the id attribute definition in HTML 4.0.

---

#### getId

String

getId()

The element's identifier. See the id attribute definition in HTML 4.0.

setId

```java
void setId​(
String
id)
```

---

#### setId

void setId​(

String

id)

getTitle

```java
String
getTitle()
```

The element's advisory title. See the title attribute definition in
HTML 4.0.

---

#### getTitle

String

getTitle()

The element's advisory title. See the title attribute definition in
HTML 4.0.

setTitle

```java
void setTitle​(
String
title)
```

---

#### setTitle

void setTitle​(

String

title)

getLang

```java
String
getLang()
```

Language code defined in RFC 1766. See the lang attribute definition
in HTML 4.0.

---

#### getLang

String

getLang()

Language code defined in RFC 1766. See the lang attribute definition
in HTML 4.0.

setLang

```java
void setLang​(
String
lang)
```

---

#### setLang

void setLang​(

String

lang)

getDir

```java
String
getDir()
```

Specifies the base direction of directionally neutral text and the
directionality of tables. See the dir attribute definition in HTML
4.0.

---

#### getDir

String

getDir()

Specifies the base direction of directionally neutral text and the
directionality of tables. See the dir attribute definition in HTML
4.0.

setDir

```java
void setDir​(
String
dir)
```

---

#### setDir

void setDir​(

String

dir)

getClassName

```java
String
getClassName()
```

The class attribute of the element. This attribute has been renamed
due to conflicts with the "class" keyword exposed by many languages.
See the class attribute definition in HTML 4.0.

---

#### getClassName

String

getClassName()

The class attribute of the element. This attribute has been renamed
due to conflicts with the "class" keyword exposed by many languages.
See the class attribute definition in HTML 4.0.

setClassName

```java
void setClassName​(
String
className)
```

---

#### setClassName

void setClassName​(

String

className)

---

