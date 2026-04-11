# Interface HTMLInputElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLInputElement.html`

### Class Description

```java
public interface
HTMLInputElement

extends
HTMLElement
```

Form control. Note. Depending upon the environment in which the page is
being viewed, the value property may be read-only for the file upload
input type. For the "password" input type, the actual value returned may
be masked to prevent unauthorized use. See the INPUT element definition
in HTML 4.0.

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

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element. The value of this attribute does not change if the
contents of the corresponding form control, in an interactive user
agent, changes. Changing this attribute, however, resets the contents
of the form control. See the value attribute definition in HTML 4.0.

---

#### void setDefaultValue​(
String
defaultValue)

*No description found.*

---

#### boolean getDefaultChecked()

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element. The value of
this attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changes to this
attribute, however, resets the state of the form control. See the
checked attribute definition in HTML 4.0.

---

#### void setDefaultChecked​(boolean defaultChecked)

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
getAccept()

A comma-separated list of content types that a server processing this
form will handle correctly. See the accept attribute definition in
HTML 4.0.

---

#### void setAccept​(
String
accept)

*No description found.*

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
getAlt()

Alternate text for user agents not rendering the normal content of
this element. See the alt attribute definition in HTML 4.0.

---

#### void setAlt​(
String
alt)

*No description found.*

---

#### boolean getChecked()

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent. Changes to this attribute
change the state of the form control, but do not change the value of
the HTML value attribute of the element.

---

#### void setChecked​(boolean checked)

*No description found.*

---

#### boolean getDisabled()

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

---

#### void setDisabled​(boolean disabled)

*No description found.*

---

#### int getMaxLength()

Maximum number of characters for text fields, when

type

has the value "Text" or "Password". See the maxlength attribute
definition in HTML 4.0.

---

#### void setMaxLength​(int maxLength)

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

This control is read-only. Relevant only when

type

has
the value "Text" or "Password". See the readonly attribute definition
in HTML 4.0.

---

#### void setReadOnly​(boolean readOnly)

*No description found.*

---

#### String
getSize()

Size information. The precise meaning is specific to each type of
field. See the size attribute definition in HTML 4.0.

---

#### void setSize​(
String
size)

*No description found.*

---

#### String
getSrc()

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button. See the src attribute definition in HTML
4.0.

---

#### void setSrc​(
String
src)

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

The type of control created. See the type attribute definition in
HTML 4.0.

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
getValue()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent. Changing
this attribute changes the contents of the form control, but does not
change the value of the HTML value attribute of the element. When the

type

attribute of the element has the value "Button",
"Hidden", "Submit", "Reset", "Image", "Checkbox" or "Radio", this
represents the HTML value attribute of the element. See the value
attribute definition in HTML 4.0.

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

Select the contents of the text area. For

INPUT

elements
whose

type

attribute has one of the following values:
"Text", "File", or "Password".

---

#### void click()

Simulate a mouse-click. For

INPUT

elements whose

type

attribute has one of the following values: "Button",
"Checkbox", "Radio", "Reset", or "Submit".

---

### Additional Sections

#### Interface HTMLInputElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLInputElement

extends
HTMLElement
```

Form control. Note. Depending upon the environment in which the page is
being viewed, the value property may be read-only for the file upload
input type. For the "password" input type, the actual value returned may
be masked to prevent unauthorized use. See the INPUT element definition
in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLInputElement

extends

HTMLElement

Form control. Note. Depending upon the environment in which the page is
being viewed, the value property may be read-only for the file upload
input type. For the "password" input type, the actual value returned may
be masked to prevent unauthorized use. See the INPUT element definition
in HTML 4.0.

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

click

()

Simulate a mouse-click.

void

focus

()

Gives keyboard focus to this element.

String

getAccept

()

A comma-separated list of content types that a server processing this
form will handle correctly.

String

getAccessKey

()

A single character access key to give access to the form control.

String

getAlign

()

Aligns this object (vertically or horizontally) with respect to its
surrounding text.

String

getAlt

()

Alternate text for user agents not rendering the normal content of
this element.

boolean

getChecked

()

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent.

boolean

getDefaultChecked

()

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element.

String

getDefaultValue

()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element.

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

getMaxLength

()

Maximum number of characters for text fields, when

type

has the value "Text" or "Password".

String

getName

()

Form control or object name when submitted with a form.

boolean

getReadOnly

()

This control is read-only.

String

getSize

()

Size information.

String

getSrc

()

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

The type of control created.

String

getUseMap

()

Use client-side image map.

String

getValue

()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent.

void

select

()

Select the contents of the text area.

void

setAccept

​(

String

accept)

void

setAccessKey

​(

String

accessKey)

void

setAlign

​(

String

align)

void

setAlt

​(

String

alt)

void

setChecked

​(boolean checked)

void

setDefaultChecked

​(boolean defaultChecked)

void

setDefaultValue

​(

String

defaultValue)

void

setDisabled

​(boolean disabled)

void

setMaxLength

​(int maxLength)

void

setName

​(

String

name)

void

setReadOnly

​(boolean readOnly)

void

setSize

​(

String

size)

void

setSrc

​(

String

src)

void

setTabIndex

​(int tabIndex)

void

setUseMap

​(

String

useMap)

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

click

()

Simulate a mouse-click.

void

focus

()

Gives keyboard focus to this element.

String

getAccept

()

A comma-separated list of content types that a server processing this
form will handle correctly.

String

getAccessKey

()

A single character access key to give access to the form control.

String

getAlign

()

Aligns this object (vertically or horizontally) with respect to its
surrounding text.

String

getAlt

()

Alternate text for user agents not rendering the normal content of
this element.

boolean

getChecked

()

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent.

boolean

getDefaultChecked

()

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element.

String

getDefaultValue

()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element.

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

getMaxLength

()

Maximum number of characters for text fields, when

type

has the value "Text" or "Password".

String

getName

()

Form control or object name when submitted with a form.

boolean

getReadOnly

()

This control is read-only.

String

getSize

()

Size information.

String

getSrc

()

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button.

int

getTabIndex

()

Index that represents the element's position in the tabbing order.

String

getType

()

The type of control created.

String

getUseMap

()

Use client-side image map.

String

getValue

()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent.

void

select

()

Select the contents of the text area.

void

setAccept

​(

String

accept)

void

setAccessKey

​(

String

accessKey)

void

setAlign

​(

String

align)

void

setAlt

​(

String

alt)

void

setChecked

​(boolean checked)

void

setDefaultChecked

​(boolean defaultChecked)

void

setDefaultValue

​(

String

defaultValue)

void

setDisabled

​(boolean disabled)

void

setMaxLength

​(int maxLength)

void

setName

​(

String

name)

void

setReadOnly

​(boolean readOnly)

void

setSize

​(

String

size)

void

setSrc

​(

String

src)

void

setTabIndex

​(int tabIndex)

void

setUseMap

​(

String

useMap)

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

Simulate a mouse-click.

Gives keyboard focus to this element.

A comma-separated list of content types that a server processing this
form will handle correctly.

A single character access key to give access to the form control.

Aligns this object (vertically or horizontally) with respect to its
surrounding text.

Alternate text for user agents not rendering the normal content of
this element.

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent.

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element.

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element.

The control is unavailable in this context.

Returns the

FORM

element containing this control.

Maximum number of characters for text fields, when

type

has the value "Text" or "Password".

Form control or object name when submitted with a form.

This control is read-only.

Size information.

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button.

Index that represents the element's position in the tabbing order.

The type of control created.

Use client-side image map.

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent.

Select the contents of the text area.

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

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element. The value of this attribute does not change if the
contents of the corresponding form control, in an interactive user
agent, changes. Changing this attribute, however, resets the contents
of the form control. See the value attribute definition in HTML 4.0.

- setDefaultValue

```java
void setDefaultValue​(
String
defaultValue)
```

- getDefaultChecked

```java
boolean getDefaultChecked()
```

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element. The value of
this attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changes to this
attribute, however, resets the state of the form control. See the
checked attribute definition in HTML 4.0.

- setDefaultChecked

```java
void setDefaultChecked​(boolean defaultChecked)
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

- getAccept

```java
String
getAccept()
```

A comma-separated list of content types that a server processing this
form will handle correctly. See the accept attribute definition in
HTML 4.0.

- setAccept

```java
void setAccept​(
String
accept)
```

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

- getChecked

```java
boolean getChecked()
```

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent. Changes to this attribute
change the state of the form control, but do not change the value of
the HTML value attribute of the element.

- setChecked

```java
void setChecked​(boolean checked)
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

- getMaxLength

```java
int getMaxLength()
```

Maximum number of characters for text fields, when

type

has the value "Text" or "Password". See the maxlength attribute
definition in HTML 4.0.

- setMaxLength

```java
void setMaxLength​(int maxLength)
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

This control is read-only. Relevant only when

type

has
the value "Text" or "Password". See the readonly attribute definition
in HTML 4.0.

- setReadOnly

```java
void setReadOnly​(boolean readOnly)
```

- getSize

```java
String
getSize()
```

Size information. The precise meaning is specific to each type of
field. See the size attribute definition in HTML 4.0.

- setSize

```java
void setSize​(
String
size)
```

- getSrc

```java
String
getSrc()
```

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button. See the src attribute definition in HTML
4.0.

- setSrc

```java
void setSrc​(
String
src)
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

The type of control created. See the type attribute definition in
HTML 4.0.

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

- getValue

```java
String
getValue()
```

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent. Changing
this attribute changes the contents of the form control, but does not
change the value of the HTML value attribute of the element. When the

type

attribute of the element has the value "Button",
"Hidden", "Submit", "Reset", "Image", "Checkbox" or "Radio", this
represents the HTML value attribute of the element. See the value
attribute definition in HTML 4.0.

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

Select the contents of the text area. For

INPUT

elements
whose

type

attribute has one of the following values:
"Text", "File", or "Password".

- click

```java
void click()
```

Simulate a mouse-click. For

INPUT

elements whose

type

attribute has one of the following values: "Button",
"Checkbox", "Radio", "Reset", or "Submit".

Method Detail

- getDefaultValue

```java
String
getDefaultValue()
```

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element. The value of this attribute does not change if the
contents of the corresponding form control, in an interactive user
agent, changes. Changing this attribute, however, resets the contents
of the form control. See the value attribute definition in HTML 4.0.

- setDefaultValue

```java
void setDefaultValue​(
String
defaultValue)
```

- getDefaultChecked

```java
boolean getDefaultChecked()
```

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element. The value of
this attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changes to this
attribute, however, resets the state of the form control. See the
checked attribute definition in HTML 4.0.

- setDefaultChecked

```java
void setDefaultChecked​(boolean defaultChecked)
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

- getAccept

```java
String
getAccept()
```

A comma-separated list of content types that a server processing this
form will handle correctly. See the accept attribute definition in
HTML 4.0.

- setAccept

```java
void setAccept​(
String
accept)
```

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

- getChecked

```java
boolean getChecked()
```

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent. Changes to this attribute
change the state of the form control, but do not change the value of
the HTML value attribute of the element.

- setChecked

```java
void setChecked​(boolean checked)
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

- getMaxLength

```java
int getMaxLength()
```

Maximum number of characters for text fields, when

type

has the value "Text" or "Password". See the maxlength attribute
definition in HTML 4.0.

- setMaxLength

```java
void setMaxLength​(int maxLength)
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

This control is read-only. Relevant only when

type

has
the value "Text" or "Password". See the readonly attribute definition
in HTML 4.0.

- setReadOnly

```java
void setReadOnly​(boolean readOnly)
```

- getSize

```java
String
getSize()
```

Size information. The precise meaning is specific to each type of
field. See the size attribute definition in HTML 4.0.

- setSize

```java
void setSize​(
String
size)
```

- getSrc

```java
String
getSrc()
```

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button. See the src attribute definition in HTML
4.0.

- setSrc

```java
void setSrc​(
String
src)
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

The type of control created. See the type attribute definition in
HTML 4.0.

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

- getValue

```java
String
getValue()
```

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent. Changing
this attribute changes the contents of the form control, but does not
change the value of the HTML value attribute of the element. When the

type

attribute of the element has the value "Button",
"Hidden", "Submit", "Reset", "Image", "Checkbox" or "Radio", this
represents the HTML value attribute of the element. See the value
attribute definition in HTML 4.0.

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

Select the contents of the text area. For

INPUT

elements
whose

type

attribute has one of the following values:
"Text", "File", or "Password".

- click

```java
void click()
```

Simulate a mouse-click. For

INPUT

elements whose

type

attribute has one of the following values: "Button",
"Checkbox", "Radio", "Reset", or "Submit".

---

#### Method Detail

getDefaultValue

```java
String
getDefaultValue()
```

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element. The value of this attribute does not change if the
contents of the corresponding form control, in an interactive user
agent, changes. Changing this attribute, however, resets the contents
of the form control. See the value attribute definition in HTML 4.0.

---

#### getDefaultValue

String

getDefaultValue()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the HTML value attribute
of the element. The value of this attribute does not change if the
contents of the corresponding form control, in an interactive user
agent, changes. Changing this attribute, however, resets the contents
of the form control. See the value attribute definition in HTML 4.0.

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

getDefaultChecked

```java
boolean getDefaultChecked()
```

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element. The value of
this attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changes to this
attribute, however, resets the state of the form control. See the
checked attribute definition in HTML 4.0.

---

#### getDefaultChecked

boolean getDefaultChecked()

When

type

has the value "Radio" or "Checkbox", this
represents the HTML checked attribute of the element. The value of
this attribute does not change if the state of the corresponding form
control, in an interactive user agent, changes. Changes to this
attribute, however, resets the state of the form control. See the
checked attribute definition in HTML 4.0.

setDefaultChecked

```java
void setDefaultChecked​(boolean defaultChecked)
```

---

#### setDefaultChecked

void setDefaultChecked​(boolean defaultChecked)

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

getAccept

```java
String
getAccept()
```

A comma-separated list of content types that a server processing this
form will handle correctly. See the accept attribute definition in
HTML 4.0.

---

#### getAccept

String

getAccept()

A comma-separated list of content types that a server processing this
form will handle correctly. See the accept attribute definition in
HTML 4.0.

setAccept

```java
void setAccept​(
String
accept)
```

---

#### setAccept

void setAccept​(

String

accept)

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

getChecked

```java
boolean getChecked()
```

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent. Changes to this attribute
change the state of the form control, but do not change the value of
the HTML value attribute of the element.

---

#### getChecked

boolean getChecked()

When the

type

attribute of the element has the value
"Radio" or "Checkbox", this represents the current state of the form
control, in an interactive user agent. Changes to this attribute
change the state of the form control, but do not change the value of
the HTML value attribute of the element.

setChecked

```java
void setChecked​(boolean checked)
```

---

#### setChecked

void setChecked​(boolean checked)

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

getMaxLength

```java
int getMaxLength()
```

Maximum number of characters for text fields, when

type

has the value "Text" or "Password". See the maxlength attribute
definition in HTML 4.0.

---

#### getMaxLength

int getMaxLength()

Maximum number of characters for text fields, when

type

has the value "Text" or "Password". See the maxlength attribute
definition in HTML 4.0.

setMaxLength

```java
void setMaxLength​(int maxLength)
```

---

#### setMaxLength

void setMaxLength​(int maxLength)

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

This control is read-only. Relevant only when

type

has
the value "Text" or "Password". See the readonly attribute definition
in HTML 4.0.

---

#### getReadOnly

boolean getReadOnly()

This control is read-only. Relevant only when

type

has
the value "Text" or "Password". See the readonly attribute definition
in HTML 4.0.

setReadOnly

```java
void setReadOnly​(boolean readOnly)
```

---

#### setReadOnly

void setReadOnly​(boolean readOnly)

getSize

```java
String
getSize()
```

Size information. The precise meaning is specific to each type of
field. See the size attribute definition in HTML 4.0.

---

#### getSize

String

getSize()

Size information. The precise meaning is specific to each type of
field. See the size attribute definition in HTML 4.0.

setSize

```java
void setSize​(
String
size)
```

---

#### setSize

void setSize​(

String

size)

getSrc

```java
String
getSrc()
```

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button. See the src attribute definition in HTML
4.0.

---

#### getSrc

String

getSrc()

When the

type

attribute has the value "Image", this
attribute specifies the location of the image to be used to decorate
the graphical submit button. See the src attribute definition in HTML
4.0.

setSrc

```java
void setSrc​(
String
src)
```

---

#### setSrc

void setSrc​(

String

src)

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

The type of control created. See the type attribute definition in
HTML 4.0.

---

#### getType

String

getType()

The type of control created. See the type attribute definition in
HTML 4.0.

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

getValue

```java
String
getValue()
```

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent. Changing
this attribute changes the contents of the form control, but does not
change the value of the HTML value attribute of the element. When the

type

attribute of the element has the value "Button",
"Hidden", "Submit", "Reset", "Image", "Checkbox" or "Radio", this
represents the HTML value attribute of the element. See the value
attribute definition in HTML 4.0.

---

#### getValue

String

getValue()

When the

type

attribute of the element has the value
"Text", "File" or "Password", this represents the current contents of
the corresponding form control, in an interactive user agent. Changing
this attribute changes the contents of the form control, but does not
change the value of the HTML value attribute of the element. When the

type

attribute of the element has the value "Button",
"Hidden", "Submit", "Reset", "Image", "Checkbox" or "Radio", this
represents the HTML value attribute of the element. See the value
attribute definition in HTML 4.0.

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

Select the contents of the text area. For

INPUT

elements
whose

type

attribute has one of the following values:
"Text", "File", or "Password".

---

#### select

void select()

Select the contents of the text area. For

INPUT

elements
whose

type

attribute has one of the following values:
"Text", "File", or "Password".

click

```java
void click()
```

Simulate a mouse-click. For

INPUT

elements whose

type

attribute has one of the following values: "Button",
"Checkbox", "Radio", "Reset", or "Submit".

---

#### click

void click()

Simulate a mouse-click. For

INPUT

elements whose

type

attribute has one of the following values: "Button",
"Checkbox", "Radio", "Reset", or "Submit".

---

