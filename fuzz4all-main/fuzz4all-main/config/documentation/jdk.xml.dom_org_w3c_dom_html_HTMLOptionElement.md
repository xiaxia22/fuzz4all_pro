# Interface HTMLOptionElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLOptionElement.html`

### Class Description

```java
public interface
HTMLOptionElement

extends
HTMLElement
```

A selectable choice. See the OPTION element definition in HTML 4.0.

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

#### boolean getDefaultSelected()

Represents the value of the HTML selected attribute. The value of this
attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changing

defaultSelected

, however, resets the state of the form
control. See the selected attribute definition in HTML 4.0.

---

#### void setDefaultSelected​(boolean defaultSelected)

*No description found.*

---

#### String
getText()

The text contained within the option element.

---

#### int getIndex()

The index of this

OPTION

in its parent

SELECT

, starting from 0.

---

#### boolean getDisabled()

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

---

#### void setDisabled​(boolean disabled)

*No description found.*

---

#### String
getLabel()

Option label for use in hierarchical menus. See the label attribute
definition in HTML 4.0.

---

#### void setLabel​(
String
label)

*No description found.*

---

#### boolean getSelected()

Represents the current state of the corresponding form control, in an
interactive user agent. Changing this attribute changes the state of
the form control, but does not change the value of the HTML selected
attribute of the element.

---

#### void setSelected​(boolean selected)

*No description found.*

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

#### Interface HTMLOptionElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLOptionElement

extends
HTMLElement
```

A selectable choice. See the OPTION element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLOptionElement

extends

HTMLElement

A selectable choice. See the OPTION element definition in HTML 4.0.

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

boolean

getDefaultSelected

()

Represents the value of the HTML selected attribute.

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

int

getIndex

()

The index of this

OPTION

in its parent

SELECT

, starting from 0.

String

getLabel

()

Option label for use in hierarchical menus.

boolean

getSelected

()

Represents the current state of the corresponding form control, in an
interactive user agent.

String

getText

()

The text contained within the option element.

String

getValue

()

The current form control value.

void

setDefaultSelected

​(boolean defaultSelected)

void

setDisabled

​(boolean disabled)

void

setLabel

​(

String

label)

void

setSelected

​(boolean selected)

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

boolean

getDefaultSelected

()

Represents the value of the HTML selected attribute.

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

int

getIndex

()

The index of this

OPTION

in its parent

SELECT

, starting from 0.

String

getLabel

()

Option label for use in hierarchical menus.

boolean

getSelected

()

Represents the current state of the corresponding form control, in an
interactive user agent.

String

getText

()

The text contained within the option element.

String

getValue

()

The current form control value.

void

setDefaultSelected

​(boolean defaultSelected)

void

setDisabled

​(boolean disabled)

void

setLabel

​(

String

label)

void

setSelected

​(boolean selected)

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

Represents the value of the HTML selected attribute.

The control is unavailable in this context.

Returns the

FORM

element containing this control.

The index of this

OPTION

in its parent

SELECT

, starting from 0.

Option label for use in hierarchical menus.

Represents the current state of the corresponding form control, in an
interactive user agent.

The text contained within the option element.

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

- getDefaultSelected

```java
boolean getDefaultSelected()
```

Represents the value of the HTML selected attribute. The value of this
attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changing

defaultSelected

, however, resets the state of the form
control. See the selected attribute definition in HTML 4.0.

- setDefaultSelected

```java
void setDefaultSelected​(boolean defaultSelected)
```

- getText

```java
String
getText()
```

The text contained within the option element.

- getIndex

```java
int getIndex()
```

The index of this

OPTION

in its parent

SELECT

, starting from 0.

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

- getLabel

```java
String
getLabel()
```

Option label for use in hierarchical menus. See the label attribute
definition in HTML 4.0.

- setLabel

```java
void setLabel​(
String
label)
```

- getSelected

```java
boolean getSelected()
```

Represents the current state of the corresponding form control, in an
interactive user agent. Changing this attribute changes the state of
the form control, but does not change the value of the HTML selected
attribute of the element.

- setSelected

```java
void setSelected​(boolean selected)
```

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

- getDefaultSelected

```java
boolean getDefaultSelected()
```

Represents the value of the HTML selected attribute. The value of this
attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changing

defaultSelected

, however, resets the state of the form
control. See the selected attribute definition in HTML 4.0.

- setDefaultSelected

```java
void setDefaultSelected​(boolean defaultSelected)
```

- getText

```java
String
getText()
```

The text contained within the option element.

- getIndex

```java
int getIndex()
```

The index of this

OPTION

in its parent

SELECT

, starting from 0.

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

- getLabel

```java
String
getLabel()
```

Option label for use in hierarchical menus. See the label attribute
definition in HTML 4.0.

- setLabel

```java
void setLabel​(
String
label)
```

- getSelected

```java
boolean getSelected()
```

Represents the current state of the corresponding form control, in an
interactive user agent. Changing this attribute changes the state of
the form control, but does not change the value of the HTML selected
attribute of the element.

- setSelected

```java
void setSelected​(boolean selected)
```

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

getDefaultSelected

```java
boolean getDefaultSelected()
```

Represents the value of the HTML selected attribute. The value of this
attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changing

defaultSelected

, however, resets the state of the form
control. See the selected attribute definition in HTML 4.0.

---

#### getDefaultSelected

boolean getDefaultSelected()

Represents the value of the HTML selected attribute. The value of this
attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changing

defaultSelected

, however, resets the state of the form
control. See the selected attribute definition in HTML 4.0.

setDefaultSelected

```java
void setDefaultSelected​(boolean defaultSelected)
```

---

#### setDefaultSelected

void setDefaultSelected​(boolean defaultSelected)

getText

```java
String
getText()
```

The text contained within the option element.

---

#### getText

String

getText()

The text contained within the option element.

getIndex

```java
int getIndex()
```

The index of this

OPTION

in its parent

SELECT

, starting from 0.

---

#### getIndex

int getIndex()

The index of this

OPTION

in its parent

SELECT

, starting from 0.

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

getLabel

```java
String
getLabel()
```

Option label for use in hierarchical menus. See the label attribute
definition in HTML 4.0.

---

#### getLabel

String

getLabel()

Option label for use in hierarchical menus. See the label attribute
definition in HTML 4.0.

setLabel

```java
void setLabel​(
String
label)
```

---

#### setLabel

void setLabel​(

String

label)

getSelected

```java
boolean getSelected()
```

Represents the current state of the corresponding form control, in an
interactive user agent. Changing this attribute changes the state of
the form control, but does not change the value of the HTML selected
attribute of the element.

---

#### getSelected

boolean getSelected()

Represents the current state of the corresponding form control, in an
interactive user agent. Changing this attribute changes the state of
the form control, but does not change the value of the HTML selected
attribute of the element.

setSelected

```java
void setSelected​(boolean selected)
```

---

#### setSelected

void setSelected​(boolean selected)

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

