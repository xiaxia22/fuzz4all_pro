# Interface HTMLTextAreaElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLTextAreaElement.html`

### Class Description

```java
public interface
HTMLTextAreaElement

extends
HTMLElement
```

Multi-line text field. See the TEXTAREA element definition in HTML 4.0.

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
getDefaultValue()

Represents the contents of the element. The value of this attribute
does not change if the contents of the corresponding form control, in
an interactive user agent, changes. Changing this attribute, however,
resets the contents of the form control.

---

#### void setDefaultValue​(
String
defaultValue)

*No description found.*

---

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

#### int getCols()

Width of control (in characters). See the cols attribute definition
in HTML 4.0.

---

#### void setCols​(int cols)

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

#### boolean getReadOnly()

This control is read-only. See the readonly attribute definition in
HTML 4.0.

---

#### void setReadOnly​(boolean readOnly)

*No description found.*

---

#### int getRows()

Number of text rows. See the rows attribute definition in HTML 4.0.

---

#### void setRows​(int rows)

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

The type of this form control. This the string "textarea".

---

#### String
getValue()

Represents the current contents of the corresponding form control, in
an interactive user agent. Changing this attribute changes the
contents of the form control, but does not change the contents of the
element. If the entirety of the data can not fit into a single

DOMString

, the implementation may truncate the data.

---

#### void setValue​(
String
value)

*No description found.*

---

#### void blur()

Removes keyboard focus from this element.

---

#### void focus()

Gives keyboard focus to this element.

---

#### void select()

Select the contents of the

TEXTAREA

.

---

### Additional Sections

#### Interface HTMLTextAreaElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLTextAreaElement

extends
HTMLElement
```

Multi-line text field. See the TEXTAREA element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLTextAreaElement

extends

HTMLElement

Multi-line text field. See the TEXTAREA element definition in HTML 4.0.

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

blur

()

Removes keyboard focus from this element.

void

focus

()

Gives keyboard focus to this element.

String

getAccessKey

()

A single character access key to give access to the form control.

int

getCols

()

Width of control (in characters).

String

getDefaultValue

()

Represents the contents of the element.

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

boolean

getReadOnly

()

This control is read-only.

int

getRows

()

Number of text rows.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

The type of this form control.

String

getValue

()

Represents the current contents of the corresponding form control, in
an interactive user agent.

void

select

()

Select the contents of the

TEXTAREA

.

void

setAccessKey

​(

String

accessKey)

void

setCols

​(int cols)

void

setDefaultValue

​(

String

defaultValue)

void

setDisabled

​(boolean disabled)

void

setName

​(

String

name)

void

setReadOnly

​(boolean readOnly)

void

setRows

​(int rows)

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

void

blur

()

Removes keyboard focus from this element.

void

focus

()

Gives keyboard focus to this element.

String

getAccessKey

()

A single character access key to give access to the form control.

int

getCols

()

Width of control (in characters).

String

getDefaultValue

()

Represents the contents of the element.

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

boolean

getReadOnly

()

This control is read-only.

int

getRows

()

Number of text rows.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

The type of this form control.

String

getValue

()

Represents the current contents of the corresponding form control, in
an interactive user agent.

void

select

()

Select the contents of the

TEXTAREA

.

void

setAccessKey

​(

String

accessKey)

void

setCols

​(int cols)

void

setDefaultValue

​(

String

defaultValue)

void

setDisabled

​(boolean disabled)

void

setName

​(

String

name)

void

setReadOnly

​(boolean readOnly)

void

setRows

​(int rows)

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

Removes keyboard focus from this element.

Gives keyboard focus to this element.

A single character access key to give access to the form control.

Width of control (in characters).

Represents the contents of the element.

The control is unavailable in this context.

Returns the

FORM

element containing this control.

Form control or object name when submitted with a form.

This control is read-only.

Number of text rows.

Index that represents the element's position in the tabbing order.

The type of this form control.

Represents the current contents of the corresponding form control, in
an interactive user agent.

Select the contents of the

TEXTAREA

.

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

- getDefaultValue

```java
String
getDefaultValue()
```

Represents the contents of the element. The value of this attribute
does not change if the contents of the corresponding form control, in
an interactive user agent, changes. Changing this attribute, however,
resets the contents of the form control.

- setDefaultValue

```java
void setDefaultValue​(
String
defaultValue)
```

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

- getCols

```java
int getCols()
```

Width of control (in characters). See the cols attribute definition
in HTML 4.0.

- setCols

```java
void setCols​(int cols)
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

- getReadOnly

```java
boolean getReadOnly()
```

This control is read-only. See the readonly attribute definition in
HTML 4.0.

- setReadOnly

```java
void setReadOnly​(boolean readOnly)
```

- getRows

```java
int getRows()
```

Number of text rows. See the rows attribute definition in HTML 4.0.

- setRows

```java
void setRows​(int rows)
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

The type of this form control. This the string "textarea".

- getValue

```java
String
getValue()
```

Represents the current contents of the corresponding form control, in
an interactive user agent. Changing this attribute changes the
contents of the form control, but does not change the contents of the
element. If the entirety of the data can not fit into a single

DOMString

, the implementation may truncate the data.

- setValue

```java
void setValue​(
String
value)
```

- blur

```java
void blur()
```

Removes keyboard focus from this element.

- focus

```java
void focus()
```

Gives keyboard focus to this element.

- select

```java
void select()
```

Select the contents of the

TEXTAREA

.

Method Detail

- getDefaultValue

```java
String
getDefaultValue()
```

Represents the contents of the element. The value of this attribute
does not change if the contents of the corresponding form control, in
an interactive user agent, changes. Changing this attribute, however,
resets the contents of the form control.

- setDefaultValue

```java
void setDefaultValue​(
String
defaultValue)
```

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

- getCols

```java
int getCols()
```

Width of control (in characters). See the cols attribute definition
in HTML 4.0.

- setCols

```java
void setCols​(int cols)
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

- getReadOnly

```java
boolean getReadOnly()
```

This control is read-only. See the readonly attribute definition in
HTML 4.0.

- setReadOnly

```java
void setReadOnly​(boolean readOnly)
```

- getRows

```java
int getRows()
```

Number of text rows. See the rows attribute definition in HTML 4.0.

- setRows

```java
void setRows​(int rows)
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

The type of this form control. This the string "textarea".

- getValue

```java
String
getValue()
```

Represents the current contents of the corresponding form control, in
an interactive user agent. Changing this attribute changes the
contents of the form control, but does not change the contents of the
element. If the entirety of the data can not fit into a single

DOMString

, the implementation may truncate the data.

- setValue

```java
void setValue​(
String
value)
```

- blur

```java
void blur()
```

Removes keyboard focus from this element.

- focus

```java
void focus()
```

Gives keyboard focus to this element.

- select

```java
void select()
```

Select the contents of the

TEXTAREA

.

---

#### Method Detail

getDefaultValue

```java
String
getDefaultValue()
```

Represents the contents of the element. The value of this attribute
does not change if the contents of the corresponding form control, in
an interactive user agent, changes. Changing this attribute, however,
resets the contents of the form control.

---

#### getDefaultValue

String

getDefaultValue()

Represents the contents of the element. The value of this attribute
does not change if the contents of the corresponding form control, in
an interactive user agent, changes. Changing this attribute, however,
resets the contents of the form control.

setDefaultValue

```java
void setDefaultValue​(
String
defaultValue)
```

---

#### setDefaultValue

void setDefaultValue​(

String

defaultValue)

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

getCols

```java
int getCols()
```

Width of control (in characters). See the cols attribute definition
in HTML 4.0.

---

#### getCols

int getCols()

Width of control (in characters). See the cols attribute definition
in HTML 4.0.

setCols

```java
void setCols​(int cols)
```

---

#### setCols

void setCols​(int cols)

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

getReadOnly

```java
boolean getReadOnly()
```

This control is read-only. See the readonly attribute definition in
HTML 4.0.

---

#### getReadOnly

boolean getReadOnly()

This control is read-only. See the readonly attribute definition in
HTML 4.0.

setReadOnly

```java
void setReadOnly​(boolean readOnly)
```

---

#### setReadOnly

void setReadOnly​(boolean readOnly)

getRows

```java
int getRows()
```

Number of text rows. See the rows attribute definition in HTML 4.0.

---

#### getRows

int getRows()

Number of text rows. See the rows attribute definition in HTML 4.0.

setRows

```java
void setRows​(int rows)
```

---

#### setRows

void setRows​(int rows)

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

The type of this form control. This the string "textarea".

---

#### getType

String

getType()

The type of this form control. This the string "textarea".

getValue

```java
String
getValue()
```

Represents the current contents of the corresponding form control, in
an interactive user agent. Changing this attribute changes the
contents of the form control, but does not change the contents of the
element. If the entirety of the data can not fit into a single

DOMString

, the implementation may truncate the data.

---

#### getValue

String

getValue()

Represents the current contents of the corresponding form control, in
an interactive user agent. Changing this attribute changes the
contents of the form control, but does not change the contents of the
element. If the entirety of the data can not fit into a single

DOMString

, the implementation may truncate the data.

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

blur

```java
void blur()
```

Removes keyboard focus from this element.

---

#### blur

void blur()

Removes keyboard focus from this element.

focus

```java
void focus()
```

Gives keyboard focus to this element.

---

#### focus

void focus()

Gives keyboard focus to this element.

select

```java
void select()
```

Select the contents of the

TEXTAREA

.

---

#### select

void select()

Select the contents of the

TEXTAREA

.

---

