# Interface HTMLButtonElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLButtonElement.html`

### Class Description

```java
public interface
HTMLButtonElement

extends
HTMLElement
```

Push button. See the BUTTON element definition in HTML 4.0.

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
getAccessKey()

A single character access key to give access to the form control. See
the accesskey attribute definition in HTML 4.0.

---

#### void setAccessKey​(
String
accessKey)

*No description found.*

---

#### boolean getDisabled()

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

---

#### void setDisabled​(boolean disabled)

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

#### int getTabIndex()

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

---

#### void setTabIndex​(int tabIndex)

*No description found.*

---

#### String
getType()

The type of button. See the type attribute definition in HTML 4.0.

---

#### String
getValue()

The current form control value. See the value attribute definition in
HTML 4.0.

---

#### void setValue​(
String
value)

*No description found.*

---

### Additional Sections

#### Interface HTMLButtonElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLButtonElement

extends
HTMLElement
```

Push button. See the BUTTON element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLButtonElement

extends

HTMLElement

Push button. See the BUTTON element definition in HTML 4.0.

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

boolean

getDisabled

()

The control is unavailable in this context.

HTMLFormElement

getForm

()

Returns the

FORM

element containing this control.

String

getName

()

Form control or object name when submitted with a form.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

The type of button.

String

getValue

()

The current form control value.

void

setAccessKey

​(

String

accessKey)

void

setDisabled

​(boolean disabled)

void

setName

​(

String

name)

void

setTabIndex

​(int tabIndex)

void

setValue

​(

String

value)

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

boolean

getDisabled

()

The control is unavailable in this context.

HTMLFormElement

getForm

()

Returns the

FORM

element containing this control.

String

getName

()

Form control or object name when submitted with a form.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

The type of button.

String

getValue

()

The current form control value.

void

setAccessKey

​(

String

accessKey)

void

setDisabled

​(boolean disabled)

void

setName

​(

String

name)

void

setTabIndex

​(int tabIndex)

void

setValue

​(

String

value)

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

The control is unavailable in this context.

Returns the

FORM

element containing this control.

Form control or object name when submitted with a form.

Index that represents the element's position in the tabbing order.

The type of button.

The current form control value.

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

- getDisabled

```java
boolean getDisabled()
```

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

- setDisabled

```java
void setDisabled​(boolean disabled)
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

The type of button. See the type attribute definition in HTML 4.0.

- getValue

```java
String
getValue()
```

The current form control value. See the value attribute definition in
HTML 4.0.

- setValue

```java
void setValue​(
String
value)
```

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

- getDisabled

```java
boolean getDisabled()
```

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

- setDisabled

```java
void setDisabled​(boolean disabled)
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

The type of button. See the type attribute definition in HTML 4.0.

- getValue

```java
String
getValue()
```

The current form control value. See the value attribute definition in
HTML 4.0.

- setValue

```java
void setValue​(
String
value)
```

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

getDisabled

```java
boolean getDisabled()
```

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

---

#### getDisabled

boolean getDisabled()

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

setDisabled

```java
void setDisabled​(boolean disabled)
```

---

#### setDisabled

void setDisabled​(boolean disabled)

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

The type of button. See the type attribute definition in HTML 4.0.

---

#### getType

String

getType()

The type of button. See the type attribute definition in HTML 4.0.

getValue

```java
String
getValue()
```

The current form control value. See the value attribute definition in
HTML 4.0.

---

#### getValue

String

getValue()

The current form control value. See the value attribute definition in
HTML 4.0.

setValue

```java
void setValue​(
String
value)
```

---

#### setValue

void setValue​(

String

value)

---

