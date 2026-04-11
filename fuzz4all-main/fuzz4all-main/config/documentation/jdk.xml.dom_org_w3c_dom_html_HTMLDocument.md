# Interface HTMLDocument

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLDocument.html`

### Class Description

```java
public interface
HTMLDocument

extends
Document
```

An

HTMLDocument

is the root of the HTML hierarchy and holds
the entire content. Besides providing access to the hierarchy, it also
provides some convenience methods for accessing certain sets of
information from the document.

The following properties have been deprecated in favor of the
corresponding ones for the

BODY

element: alinkColor background
bgColor fgColor linkColor vlinkColor In DOM Level 2, the method

getElementById

is inherited from the

Document

interface where it was moved.

See also the

Document Object Model (DOM) Level 2 Specification

.

**All Superinterfaces:** Document

,

Node

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getTitle()

The title of a document as specified by the

TITLE

element
in the head of the document.

---

#### void setTitle​(
String
title)

*No description found.*

---

#### String
getReferrer()

Returns the URI of the page that linked to this page. The value is an
empty string if the user navigated to the page directly (not through a
link, but, for example, via a bookmark).

---

#### String
getDomain()

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

---

#### String
getURL()

The complete URI of the document.

---

#### HTMLElement
getBody()

The element that contains the content for the document. In documents
with

BODY

contents, returns the

BODY

element. In frameset documents, this returns the outermost

FRAMESET

element.

---

#### void setBody​(
HTMLElement
body)

*No description found.*

---

#### HTMLCollection
getImages()

A collection of all the

IMG

elements in a document. The
behavior is limited to

IMG

elements for backwards
compatibility.

---

#### HTMLCollection
getApplets()

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

---

#### HTMLCollection
getLinks()

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

---

#### HTMLCollection
getForms()

A collection of all the forms of a document.

---

#### HTMLCollection
getAnchors()

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute. Note. For reasons
of backwards compatibility, the returned set of anchors only contains
those anchors created with the

name

attribute, not those
created with the

id

attribute.

---

#### String
getCookie()

The cookies associated with this document. If there are none, the
value is an empty string. Otherwise, the value is a string: a
semicolon-delimited list of "name, value" pairs for all the cookies
associated with the page. For example,

name=value;expires=date

.

---

#### void setCookie​(
String
cookie)

*No description found.*

---

#### void open()

Note. This method and the ones following allow a user to add to or
replace the structure model of a document using strings of unparsed
HTML. At the time of writing alternate methods for providing similar
functionality for both HTML and XML documents were being considered.
The following methods may be deprecated at some point in the future in
favor of a more general-purpose mechanism.

Open a document stream for writing. If a document exists in the
target, this method clears it.

---

#### void close()

Closes a document stream opened by

open()

and forces
rendering.

---

#### void write​(
String
text)

Write a string of text to a document stream opened by

open()

. The text is parsed into the document's structure
model.

**Parameters:**
- text

- The string to be parsed into some structure in the
document structure model.

---

#### void writeln​(
String
text)

Write a string of text followed by a newline character to a document
stream opened by

open()

. The text is parsed into the
document's structure model.

**Parameters:**
- text

- The string to be parsed into some structure in the
document structure model.

---

#### NodeList
getElementsByName​(
String
elementName)

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

**Parameters:**
- elementName

- The

name

attribute value for an
element.

**Returns:**
- The matching elements.

---

### Additional Sections

#### Interface HTMLDocument

**All Superinterfaces:** Document

,

Node

```java
public interface
HTMLDocument

extends
Document
```

An

HTMLDocument

is the root of the HTML hierarchy and holds
the entire content. Besides providing access to the hierarchy, it also
provides some convenience methods for accessing certain sets of
information from the document.

The following properties have been deprecated in favor of the
corresponding ones for the

BODY

element: alinkColor background
bgColor fgColor linkColor vlinkColor In DOM Level 2, the method

getElementById

is inherited from the

Document

interface where it was moved.

See also the

Document Object Model (DOM) Level 2 Specification

.

**Since:** 1.4, DOM Level 2

public interface

HTMLDocument

extends

Document

An

HTMLDocument

is the root of the HTML hierarchy and holds
the entire content. Besides providing access to the hierarchy, it also
provides some convenience methods for accessing certain sets of
information from the document.

The following properties have been deprecated in favor of the
corresponding ones for the

BODY

element: alinkColor background
bgColor fgColor linkColor vlinkColor In DOM Level 2, the method

getElementById

is inherited from the

Document

interface where it was moved.

See also the

Document Object Model (DOM) Level 2 Specification

.

The following properties have been deprecated in favor of the
corresponding ones for the

BODY

element: alinkColor background
bgColor fgColor linkColor vlinkColor In DOM Level 2, the method

getElementById

is inherited from the

Document

interface where it was moved.

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

close

()

Closes a document stream opened by

open()

and forces
rendering.

HTMLCollection

getAnchors

()

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute.

HTMLCollection

getApplets

()

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

HTMLElement

getBody

()

The element that contains the content for the document.

String

getCookie

()

The cookies associated with this document.

String

getDomain

()

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

NodeList

getElementsByName

​(

String

elementName)

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

HTMLCollection

getForms

()

A collection of all the forms of a document.

HTMLCollection

getImages

()

A collection of all the

IMG

elements in a document.

HTMLCollection

getLinks

()

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

String

getReferrer

()

Returns the URI of the page that linked to this page.

String

getTitle

()

The title of a document as specified by the

TITLE

element
in the head of the document.

String

getURL

()

The complete URI of the document.

void

open

()

Note.

void

setBody

​(

HTMLElement

body)

void

setCookie

​(

String

cookie)

void

setTitle

​(

String

title)

void

write

​(

String

text)

Write a string of text to a document stream opened by

open()

.

void

writeln

​(

String

text)

Write a string of text followed by a newline character to a document
stream opened by

open()

.

- Methods declared in interface org.w3c.dom.

Document

adoptNode

,

createAttribute

,

createAttributeNS

,

createCDATASection

,

createComment

,

createDocumentFragment

,

createElement

,

createElementNS

,

createEntityReference

,

createProcessingInstruction

,

createTextNode

,

getDoctype

,

getDocumentElement

,

getDocumentURI

,

getDomConfig

,

getElementById

,

getElementsByTagName

,

getElementsByTagNameNS

,

getImplementation

,

getInputEncoding

,

getStrictErrorChecking

,

getXmlEncoding

,

getXmlStandalone

,

getXmlVersion

,

importNode

,

normalizeDocument

,

renameNode

,

setDocumentURI

,

setStrictErrorChecking

,

setXmlStandalone

,

setXmlVersion

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

close

()

Closes a document stream opened by

open()

and forces
rendering.

HTMLCollection

getAnchors

()

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute.

HTMLCollection

getApplets

()

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

HTMLElement

getBody

()

The element that contains the content for the document.

String

getCookie

()

The cookies associated with this document.

String

getDomain

()

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

NodeList

getElementsByName

​(

String

elementName)

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

HTMLCollection

getForms

()

A collection of all the forms of a document.

HTMLCollection

getImages

()

A collection of all the

IMG

elements in a document.

HTMLCollection

getLinks

()

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

String

getReferrer

()

Returns the URI of the page that linked to this page.

String

getTitle

()

The title of a document as specified by the

TITLE

element
in the head of the document.

String

getURL

()

The complete URI of the document.

void

open

()

Note.

void

setBody

​(

HTMLElement

body)

void

setCookie

​(

String

cookie)

void

setTitle

​(

String

title)

void

write

​(

String

text)

Write a string of text to a document stream opened by

open()

.

void

writeln

​(

String

text)

Write a string of text followed by a newline character to a document
stream opened by

open()

.

- Methods declared in interface org.w3c.dom.

Document

adoptNode

,

createAttribute

,

createAttributeNS

,

createCDATASection

,

createComment

,

createDocumentFragment

,

createElement

,

createElementNS

,

createEntityReference

,

createProcessingInstruction

,

createTextNode

,

getDoctype

,

getDocumentElement

,

getDocumentURI

,

getDomConfig

,

getElementById

,

getElementsByTagName

,

getElementsByTagNameNS

,

getImplementation

,

getInputEncoding

,

getStrictErrorChecking

,

getXmlEncoding

,

getXmlStandalone

,

getXmlVersion

,

importNode

,

normalizeDocument

,

renameNode

,

setDocumentURI

,

setStrictErrorChecking

,

setXmlStandalone

,

setXmlVersion

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

Closes a document stream opened by

open()

and forces
rendering.

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute.

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

The element that contains the content for the document.

The cookies associated with this document.

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

A collection of all the forms of a document.

A collection of all the

IMG

elements in a document.

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

Returns the URI of the page that linked to this page.

The title of a document as specified by the

TITLE

element
in the head of the document.

The complete URI of the document.

Note.

Write a string of text to a document stream opened by

open()

.

Write a string of text followed by a newline character to a document
stream opened by

open()

.

Methods declared in interface org.w3c.dom.

Document

adoptNode

,

createAttribute

,

createAttributeNS

,

createCDATASection

,

createComment

,

createDocumentFragment

,

createElement

,

createElementNS

,

createEntityReference

,

createProcessingInstruction

,

createTextNode

,

getDoctype

,

getDocumentElement

,

getDocumentURI

,

getDomConfig

,

getElementById

,

getElementsByTagName

,

getElementsByTagNameNS

,

getImplementation

,

getInputEncoding

,

getStrictErrorChecking

,

getXmlEncoding

,

getXmlStandalone

,

getXmlVersion

,

importNode

,

normalizeDocument

,

renameNode

,

setDocumentURI

,

setStrictErrorChecking

,

setXmlStandalone

,

setXmlVersion

---

#### Methods declared in interface org.w3c.dom. Document

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

- getTitle

```java
String
getTitle()
```

The title of a document as specified by the

TITLE

element
in the head of the document.

- setTitle

```java
void setTitle​(
String
title)
```

- getReferrer

```java
String
getReferrer()
```

Returns the URI of the page that linked to this page. The value is an
empty string if the user navigated to the page directly (not through a
link, but, for example, via a bookmark).

- getDomain

```java
String
getDomain()
```

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

- getURL

```java
String
getURL()
```

The complete URI of the document.

- getBody

```java
HTMLElement
getBody()
```

The element that contains the content for the document. In documents
with

BODY

contents, returns the

BODY

element. In frameset documents, this returns the outermost

FRAMESET

element.

- setBody

```java
void setBody​(
HTMLElement
body)
```

- getImages

```java
HTMLCollection
getImages()
```

A collection of all the

IMG

elements in a document. The
behavior is limited to

IMG

elements for backwards
compatibility.

- getApplets

```java
HTMLCollection
getApplets()
```

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

- getLinks

```java
HTMLCollection
getLinks()
```

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

- getForms

```java
HTMLCollection
getForms()
```

A collection of all the forms of a document.

- getAnchors

```java
HTMLCollection
getAnchors()
```

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute. Note. For reasons
of backwards compatibility, the returned set of anchors only contains
those anchors created with the

name

attribute, not those
created with the

id

attribute.

- getCookie

```java
String
getCookie()
```

The cookies associated with this document. If there are none, the
value is an empty string. Otherwise, the value is a string: a
semicolon-delimited list of "name, value" pairs for all the cookies
associated with the page. For example,

name=value;expires=date

.

- setCookie

```java
void setCookie​(
String
cookie)
```

- open

```java
void open()
```

Note. This method and the ones following allow a user to add to or
replace the structure model of a document using strings of unparsed
HTML. At the time of writing alternate methods for providing similar
functionality for both HTML and XML documents were being considered.
The following methods may be deprecated at some point in the future in
favor of a more general-purpose mechanism.

Open a document stream for writing. If a document exists in the
target, this method clears it.

- close

```java
void close()
```

Closes a document stream opened by

open()

and forces
rendering.

- write

```java
void write​(
String
text)
```

Write a string of text to a document stream opened by

open()

. The text is parsed into the document's structure
model.

**Parameters:** text

- The string to be parsed into some structure in the
document structure model.

- writeln

```java
void writeln​(
String
text)
```

Write a string of text followed by a newline character to a document
stream opened by

open()

. The text is parsed into the
document's structure model.

**Parameters:** text

- The string to be parsed into some structure in the
document structure model.

- getElementsByName

```java
NodeList
getElementsByName​(
String
elementName)
```

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

**Parameters:** elementName

- The

name

attribute value for an
element.
**Returns:** The matching elements.

Method Detail

- getTitle

```java
String
getTitle()
```

The title of a document as specified by the

TITLE

element
in the head of the document.

- setTitle

```java
void setTitle​(
String
title)
```

- getReferrer

```java
String
getReferrer()
```

Returns the URI of the page that linked to this page. The value is an
empty string if the user navigated to the page directly (not through a
link, but, for example, via a bookmark).

- getDomain

```java
String
getDomain()
```

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

- getURL

```java
String
getURL()
```

The complete URI of the document.

- getBody

```java
HTMLElement
getBody()
```

The element that contains the content for the document. In documents
with

BODY

contents, returns the

BODY

element. In frameset documents, this returns the outermost

FRAMESET

element.

- setBody

```java
void setBody​(
HTMLElement
body)
```

- getImages

```java
HTMLCollection
getImages()
```

A collection of all the

IMG

elements in a document. The
behavior is limited to

IMG

elements for backwards
compatibility.

- getApplets

```java
HTMLCollection
getApplets()
```

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

- getLinks

```java
HTMLCollection
getLinks()
```

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

- getForms

```java
HTMLCollection
getForms()
```

A collection of all the forms of a document.

- getAnchors

```java
HTMLCollection
getAnchors()
```

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute. Note. For reasons
of backwards compatibility, the returned set of anchors only contains
those anchors created with the

name

attribute, not those
created with the

id

attribute.

- getCookie

```java
String
getCookie()
```

The cookies associated with this document. If there are none, the
value is an empty string. Otherwise, the value is a string: a
semicolon-delimited list of "name, value" pairs for all the cookies
associated with the page. For example,

name=value;expires=date

.

- setCookie

```java
void setCookie​(
String
cookie)
```

- open

```java
void open()
```

Note. This method and the ones following allow a user to add to or
replace the structure model of a document using strings of unparsed
HTML. At the time of writing alternate methods for providing similar
functionality for both HTML and XML documents were being considered.
The following methods may be deprecated at some point in the future in
favor of a more general-purpose mechanism.

Open a document stream for writing. If a document exists in the
target, this method clears it.

- close

```java
void close()
```

Closes a document stream opened by

open()

and forces
rendering.

- write

```java
void write​(
String
text)
```

Write a string of text to a document stream opened by

open()

. The text is parsed into the document's structure
model.

**Parameters:** text

- The string to be parsed into some structure in the
document structure model.

- writeln

```java
void writeln​(
String
text)
```

Write a string of text followed by a newline character to a document
stream opened by

open()

. The text is parsed into the
document's structure model.

**Parameters:** text

- The string to be parsed into some structure in the
document structure model.

- getElementsByName

```java
NodeList
getElementsByName​(
String
elementName)
```

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

**Parameters:** elementName

- The

name

attribute value for an
element.
**Returns:** The matching elements.

---

#### Method Detail

getTitle

```java
String
getTitle()
```

The title of a document as specified by the

TITLE

element
in the head of the document.

---

#### getTitle

String

getTitle()

The title of a document as specified by the

TITLE

element
in the head of the document.

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

getReferrer

```java
String
getReferrer()
```

Returns the URI of the page that linked to this page. The value is an
empty string if the user navigated to the page directly (not through a
link, but, for example, via a bookmark).

---

#### getReferrer

String

getReferrer()

Returns the URI of the page that linked to this page. The value is an
empty string if the user navigated to the page directly (not through a
link, but, for example, via a bookmark).

getDomain

```java
String
getDomain()
```

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

---

#### getDomain

String

getDomain()

The domain name of the server that served the document, or

null

if the server cannot be identified by a domain name.

getURL

```java
String
getURL()
```

The complete URI of the document.

---

#### getURL

String

getURL()

The complete URI of the document.

getBody

```java
HTMLElement
getBody()
```

The element that contains the content for the document. In documents
with

BODY

contents, returns the

BODY

element. In frameset documents, this returns the outermost

FRAMESET

element.

---

#### getBody

HTMLElement

getBody()

The element that contains the content for the document. In documents
with

BODY

contents, returns the

BODY

element. In frameset documents, this returns the outermost

FRAMESET

element.

setBody

```java
void setBody​(
HTMLElement
body)
```

---

#### setBody

void setBody​(

HTMLElement

body)

getImages

```java
HTMLCollection
getImages()
```

A collection of all the

IMG

elements in a document. The
behavior is limited to

IMG

elements for backwards
compatibility.

---

#### getImages

HTMLCollection

getImages()

A collection of all the

IMG

elements in a document. The
behavior is limited to

IMG

elements for backwards
compatibility.

getApplets

```java
HTMLCollection
getApplets()
```

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

---

#### getApplets

HTMLCollection

getApplets()

A collection of all the

OBJECT

elements that include
applets and

APPLET

( deprecated ) elements in a document.

getLinks

```java
HTMLCollection
getLinks()
```

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

---

#### getLinks

HTMLCollection

getLinks()

A collection of all

AREA

elements and anchor (

A

) elements in a document with a value for the

href

attribute.

getForms

```java
HTMLCollection
getForms()
```

A collection of all the forms of a document.

---

#### getForms

HTMLCollection

getForms()

A collection of all the forms of a document.

getAnchors

```java
HTMLCollection
getAnchors()
```

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute. Note. For reasons
of backwards compatibility, the returned set of anchors only contains
those anchors created with the

name

attribute, not those
created with the

id

attribute.

---

#### getAnchors

HTMLCollection

getAnchors()

A collection of all the anchor (

A

) elements in a document
with a value for the

name

attribute. Note. For reasons
of backwards compatibility, the returned set of anchors only contains
those anchors created with the

name

attribute, not those
created with the

id

attribute.

getCookie

```java
String
getCookie()
```

The cookies associated with this document. If there are none, the
value is an empty string. Otherwise, the value is a string: a
semicolon-delimited list of "name, value" pairs for all the cookies
associated with the page. For example,

name=value;expires=date

.

---

#### getCookie

String

getCookie()

The cookies associated with this document. If there are none, the
value is an empty string. Otherwise, the value is a string: a
semicolon-delimited list of "name, value" pairs for all the cookies
associated with the page. For example,

name=value;expires=date

.

setCookie

```java
void setCookie​(
String
cookie)
```

---

#### setCookie

void setCookie​(

String

cookie)

open

```java
void open()
```

Note. This method and the ones following allow a user to add to or
replace the structure model of a document using strings of unparsed
HTML. At the time of writing alternate methods for providing similar
functionality for both HTML and XML documents were being considered.
The following methods may be deprecated at some point in the future in
favor of a more general-purpose mechanism.

Open a document stream for writing. If a document exists in the
target, this method clears it.

---

#### open

void open()

Note. This method and the ones following allow a user to add to or
replace the structure model of a document using strings of unparsed
HTML. At the time of writing alternate methods for providing similar
functionality for both HTML and XML documents were being considered.
The following methods may be deprecated at some point in the future in
favor of a more general-purpose mechanism.

Open a document stream for writing. If a document exists in the
target, this method clears it.

close

```java
void close()
```

Closes a document stream opened by

open()

and forces
rendering.

---

#### close

void close()

Closes a document stream opened by

open()

and forces
rendering.

write

```java
void write​(
String
text)
```

Write a string of text to a document stream opened by

open()

. The text is parsed into the document's structure
model.

**Parameters:** text

- The string to be parsed into some structure in the
document structure model.

---

#### write

void write​(

String

text)

Write a string of text to a document stream opened by

open()

. The text is parsed into the document's structure
model.

writeln

```java
void writeln​(
String
text)
```

Write a string of text followed by a newline character to a document
stream opened by

open()

. The text is parsed into the
document's structure model.

**Parameters:** text

- The string to be parsed into some structure in the
document structure model.

---

#### writeln

void writeln​(

String

text)

Write a string of text followed by a newline character to a document
stream opened by

open()

. The text is parsed into the
document's structure model.

getElementsByName

```java
NodeList
getElementsByName​(
String
elementName)
```

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

**Parameters:** elementName

- The

name

attribute value for an
element.
**Returns:** The matching elements.

---

#### getElementsByName

NodeList

getElementsByName​(

String

elementName)

Returns the (possibly empty) collection of elements whose

name

value is given by

elementName

.

---

