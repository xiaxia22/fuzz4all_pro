# Interface HTMLSelectElement

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLSelectElement.html`

### Class Description

```java
public interface
HTMLSelectElement

extends
HTMLElement
```

The select element allows the selection of an option. The contained
options can be directly accessed through the select element as a
collection. See the SELECT element definition in HTML 4.0.

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
getType()

The type of this form control. This is the string "select-multiple"
when the multiple attribute is

true

and the string
"select-one" when

false

.

---

#### int getSelectedIndex()

The ordinal index of the selected option, starting from 0. The value
-1 is returned if no element is selected. If multiple options are
selected, the index of the first selected option is returned.

---

#### void setSelectedIndex​(int selectedIndex)

*No description found.*

---

#### String
getValue()

The current form control value.

---

#### void setValue​(
String
value)

*No description found.*

---

#### int getLength()

The number of options in this

SELECT

.

---

#### HTMLFormElement
getForm()

Returns the

FORM

element containing this control. Returns

null

if this control is not within the context of a form.

---

#### HTMLCollection
getOptions()

The collection of

OPTION

elements contained by this
element.

---

#### boolean getDisabled()

The control is unavailable in this context. See the disabled
attribute definition in HTML 4.0.

---

#### void setDisabled​(boolean disabled)

*No description found.*

---

#### boolean getMultiple()

If true, multiple

OPTION

elements may be selected in
this

SELECT

. See the multiple attribute definition in
HTML 4.0.

---

#### void setMultiple​(boolean multiple)

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

#### int getSize()

Number of visible rows. See the size attribute definition in HTML 4.0.

---

#### void setSize​(int size)

*No description found.*

---

#### int getTabIndex()

Index that represents the element's position in the tabbing order. See
the tabindex attribute definition in HTML 4.0.

---

#### void setTabIndex​(int tabIndex)

*No description found.*

---

#### void add​(
HTMLElement
element,

HTMLElement
before)
throws
DOMException

Add a new element to the collection of

OPTION

elements
for this

SELECT

. This method is the equivalent of the

appendChild

method of the

Node

interface if
the

before

parameter is

null

. It is
equivalent to the

insertBefore

method on the parent of

before

in all other cases.

**Parameters:**
- element

- The element to add.
- before

- The element to insert before, or

null

for
the tail of the list.

**Throws:**
- DOMException

- NOT_FOUND_ERR: Raised if

before

is not a descendant of
the

SELECT

element.

---

#### void remove​(int index)

Remove an element from the collection of

OPTION

elements
for this

SELECT

. Does nothing if no element has the given
index.

**Parameters:**
- index

- The index of the item to remove, starting from 0.

---

#### void blur()

Removes keyboard focus from this element.

---

#### void focus()

Gives keyboard focus to this element.

---

### Additional Sections

#### Interface HTMLSelectElement

**All Superinterfaces:** Element

,

HTMLElement

,

Node

```java
public interface
HTMLSelectElement

extends
HTMLElement
```

The select element allows the selection of an option. The contained
options can be directly accessed through the select element as a
collection. See the SELECT element definition in HTML 4.0.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLSelectElement

extends

HTMLElement

The select element allows the selection of an option. The contained
options can be directly accessed through the select element as a
collection. See the SELECT element definition in HTML 4.0.

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

add

​(

HTMLElement

element,

HTMLElement

before)

Add a new element to the collection of

OPTION

elements
for this

SELECT

.

void

blur

()

Removes keyboard focus from this element.

void

focus

()

Gives keyboard focus to this element.

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

getLength

()

The number of options in this

SELECT

.

boolean

getMultiple

()

If true, multiple

OPTION

elements may be selected in
this

SELECT

.

String

getName

()

Form control or object name when submitted with a form.

HTMLCollection

getOptions

()

The collection of

OPTION

elements contained by this
element.

int

getSelectedIndex

()

The ordinal index of the selected option, starting from 0.

int

getSize

()

Number of visible rows.

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

The current form control value.

void

remove

​(int index)

Remove an element from the collection of

OPTION

elements
for this

SELECT

.

void

setDisabled

​(boolean disabled)

void

setMultiple

​(boolean multiple)

void

setName

​(

String

name)

void

setSelectedIndex

​(int selectedIndex)

void

setSize

​(int size)

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

add

​(

HTMLElement

element,

HTMLElement

before)

Add a new element to the collection of

OPTION

elements
for this

SELECT

.

void

blur

()

Removes keyboard focus from this element.

void

focus

()

Gives keyboard focus to this element.

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

getLength

()

The number of options in this

SELECT

.

boolean

getMultiple

()

If true, multiple

OPTION

elements may be selected in
this

SELECT

.

String

getName

()

Form control or object name when submitted with a form.

HTMLCollection

getOptions

()

The collection of

OPTION

elements contained by this
element.

int

getSelectedIndex

()

The ordinal index of the selected option, starting from 0.

int

getSize

()

Number of visible rows.

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

The current form control value.

void

remove

​(int index)

Remove an element from the collection of

OPTION

elements
for this

SELECT

.

void

setDisabled

​(boolean disabled)

void

setMultiple

​(boolean multiple)

void

setName

​(

String

name)

void

setSelectedIndex

​(int selectedIndex)

void

setSize

​(int size)

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

Add a new element to the collection of

OPTION

elements
for this

SELECT

.

Removes keyboard focus from this element.

Gives keyboard focus to this element.

The control is unavailable in this context.

Returns the

FORM

element containing this control.

The number of options in this

SELECT

.

If true, multiple

OPTION

elements may be selected in
this

SELECT

.

Form control or object name when submitted with a form.

The collection of

OPTION

elements contained by this
element.

The ordinal index of the selected option, starting from 0.

Number of visible rows.

Index that represents the element's position in the tabbing order.

The type of this form control.

The current form control value.

Remove an element from the collection of

OPTION

elements
for this

SELECT

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

- getType

```java
String
getType()
```

The type of this form control. This is the string "select-multiple"
when the multiple attribute is

true

and the string
"select-one" when

false

.

- getSelectedIndex

```java
int getSelectedIndex()
```

The ordinal index of the selected option, starting from 0. The value
-1 is returned if no element is selected. If multiple options are
selected, the index of the first selected option is returned.

- setSelectedIndex

```java
void setSelectedIndex​(int selectedIndex)
```

- getValue

```java
String
getValue()
```

The current form control value.

- setValue

```java
void setValue​(
String
value)
```

- getLength

```java
int getLength()
```

The number of options in this

SELECT

.

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

- getOptions

```java
HTMLCollection
getOptions()
```

The collection of

OPTION

elements contained by this
element.

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

- getMultiple

```java
boolean getMultiple()
```

If true, multiple

OPTION

elements may be selected in
this

SELECT

. See the multiple attribute definition in
HTML 4.0.

- setMultiple

```java
void setMultiple​(boolean multiple)
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

- getSize

```java
int getSize()
```

Number of visible rows. See the size attribute definition in HTML 4.0.

- setSize

```java
void setSize​(int size)
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

- add

```java
void add​(
HTMLElement
element,

HTMLElement
before)
throws
DOMException
```

Add a new element to the collection of

OPTION

elements
for this

SELECT

. This method is the equivalent of the

appendChild

method of the

Node

interface if
the

before

parameter is

null

. It is
equivalent to the

insertBefore

method on the parent of

before

in all other cases.

**Parameters:** element

- The element to add.
**Parameters:** before

- The element to insert before, or

null

for
the tail of the list.
**Throws:** DOMException

- NOT_FOUND_ERR: Raised if

before

is not a descendant of
the

SELECT

element.

- remove

```java
void remove​(int index)
```

Remove an element from the collection of

OPTION

elements
for this

SELECT

. Does nothing if no element has the given
index.

**Parameters:** index

- The index of the item to remove, starting from 0.

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

Method Detail

- getType

```java
String
getType()
```

The type of this form control. This is the string "select-multiple"
when the multiple attribute is

true

and the string
"select-one" when

false

.

- getSelectedIndex

```java
int getSelectedIndex()
```

The ordinal index of the selected option, starting from 0. The value
-1 is returned if no element is selected. If multiple options are
selected, the index of the first selected option is returned.

- setSelectedIndex

```java
void setSelectedIndex​(int selectedIndex)
```

- getValue

```java
String
getValue()
```

The current form control value.

- setValue

```java
void setValue​(
String
value)
```

- getLength

```java
int getLength()
```

The number of options in this

SELECT

.

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

- getOptions

```java
HTMLCollection
getOptions()
```

The collection of

OPTION

elements contained by this
element.

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

- getMultiple

```java
boolean getMultiple()
```

If true, multiple

OPTION

elements may be selected in
this

SELECT

. See the multiple attribute definition in
HTML 4.0.

- setMultiple

```java
void setMultiple​(boolean multiple)
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

- getSize

```java
int getSize()
```

Number of visible rows. See the size attribute definition in HTML 4.0.

- setSize

```java
void setSize​(int size)
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

- add

```java
void add​(
HTMLElement
element,

HTMLElement
before)
throws
DOMException
```

Add a new element to the collection of

OPTION

elements
for this

SELECT

. This method is the equivalent of the

appendChild

method of the

Node

interface if
the

before

parameter is

null

. It is
equivalent to the

insertBefore

method on the parent of

before

in all other cases.

**Parameters:** element

- The element to add.
**Parameters:** before

- The element to insert before, or

null

for
the tail of the list.
**Throws:** DOMException

- NOT_FOUND_ERR: Raised if

before

is not a descendant of
the

SELECT

element.

- remove

```java
void remove​(int index)
```

Remove an element from the collection of

OPTION

elements
for this

SELECT

. Does nothing if no element has the given
index.

**Parameters:** index

- The index of the item to remove, starting from 0.

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

---

#### Method Detail

getType

```java
String
getType()
```

The type of this form control. This is the string "select-multiple"
when the multiple attribute is

true

and the string
"select-one" when

false

.

---

#### getType

String

getType()

The type of this form control. This is the string "select-multiple"
when the multiple attribute is

true

and the string
"select-one" when

false

.

getSelectedIndex

```java
int getSelectedIndex()
```

The ordinal index of the selected option, starting from 0. The value
-1 is returned if no element is selected. If multiple options are
selected, the index of the first selected option is returned.

---

#### getSelectedIndex

int getSelectedIndex()

The ordinal index of the selected option, starting from 0. The value
-1 is returned if no element is selected. If multiple options are
selected, the index of the first selected option is returned.

setSelectedIndex

```java
void setSelectedIndex​(int selectedIndex)
```

---

#### setSelectedIndex

void setSelectedIndex​(int selectedIndex)

getValue

```java
String
getValue()
```

The current form control value.

---

#### getValue

String

getValue()

The current form control value.

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

getLength

```java
int getLength()
```

The number of options in this

SELECT

.

---

#### getLength

int getLength()

The number of options in this

SELECT

.

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

getOptions

```java
HTMLCollection
getOptions()
```

The collection of

OPTION

elements contained by this
element.

---

#### getOptions

HTMLCollection

getOptions()

The collection of

OPTION

elements contained by this
element.

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

getMultiple

```java
boolean getMultiple()
```

If true, multiple

OPTION

elements may be selected in
this

SELECT

. See the multiple attribute definition in
HTML 4.0.

---

#### getMultiple

boolean getMultiple()

If true, multiple

OPTION

elements may be selected in
this

SELECT

. See the multiple attribute definition in
HTML 4.0.

setMultiple

```java
void setMultiple​(boolean multiple)
```

---

#### setMultiple

void setMultiple​(boolean multiple)

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

getSize

```java
int getSize()
```

Number of visible rows. See the size attribute definition in HTML 4.0.

---

#### getSize

int getSize()

Number of visible rows. See the size attribute definition in HTML 4.0.

setSize

```java
void setSize​(int size)
```

---

#### setSize

void setSize​(int size)

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

add

```java
void add​(
HTMLElement
element,

HTMLElement
before)
throws
DOMException
```

Add a new element to the collection of

OPTION

elements
for this

SELECT

. This method is the equivalent of the

appendChild

method of the

Node

interface if
the

before

parameter is

null

. It is
equivalent to the

insertBefore

method on the parent of

before

in all other cases.

**Parameters:** element

- The element to add.
**Parameters:** before

- The element to insert before, or

null

for
the tail of the list.
**Throws:** DOMException

- NOT_FOUND_ERR: Raised if

before

is not a descendant of
the

SELECT

element.

---

#### add

void add​(

HTMLElement

element,

HTMLElement

before)
throws

DOMException

Add a new element to the collection of

OPTION

elements
for this

SELECT

. This method is the equivalent of the

appendChild

method of the

Node

interface if
the

before

parameter is

null

. It is
equivalent to the

insertBefore

method on the parent of

before

in all other cases.

remove

```java
void remove​(int index)
```

Remove an element from the collection of

OPTION

elements
for this

SELECT

. Does nothing if no element has the given
index.

**Parameters:** index

- The index of the item to remove, starting from 0.

---

#### remove

void remove​(int index)

Remove an element from the collection of

OPTION

elements
for this

SELECT

. Does nothing if no element has the given
index.

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

---

