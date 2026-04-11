# Interface HTMLDOMImplementation

**Source:** `jdk.xml.dom\org\w3c\dom\html\HTMLDOMImplementation.html`

### Class Description

```java
public interface
HTMLDOMImplementation

extends
DOMImplementation
```

The

HTMLDOMImplementation

interface extends the

DOMImplementation

interface with a method for creating an
HTML document instance.

**All Superinterfaces:** DOMImplementation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### HTMLDocument
createHTMLDocument​(
String
title)

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

**Parameters:**
- title

- The title of the document to be set as the content of the

TITLE

element, through a child

Text

node.

**Returns:**
- A new

HTMLDocument

object.

---

### Additional Sections

#### Interface HTMLDOMImplementation

**All Superinterfaces:** DOMImplementation

```java
public interface
HTMLDOMImplementation

extends
DOMImplementation
```

The

HTMLDOMImplementation

interface extends the

DOMImplementation

interface with a method for creating an
HTML document instance.

**Since:** 1.4, DOM Level 2

public interface

HTMLDOMImplementation

extends

DOMImplementation

The

HTMLDOMImplementation

interface extends the

DOMImplementation

interface with a method for creating an
HTML document instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HTMLDocument

createHTMLDocument

​(

String

title)

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

- Methods declared in interface org.w3c.dom.

DOMImplementation

createDocument

,

createDocumentType

,

getFeature

,

hasFeature

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

HTMLDocument

createHTMLDocument

​(

String

title)

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

- Methods declared in interface org.w3c.dom.

DOMImplementation

createDocument

,

createDocumentType

,

getFeature

,

hasFeature

---

#### Method Summary

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

Methods declared in interface org.w3c.dom.

DOMImplementation

createDocument

,

createDocumentType

,

getFeature

,

hasFeature

---

#### Methods declared in interface org.w3c.dom. DOMImplementation

============ METHOD DETAIL ==========

- Method Detail

- createHTMLDocument

```java
HTMLDocument
createHTMLDocument​(
String
title)
```

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

**Parameters:** title

- The title of the document to be set as the content of the

TITLE

element, through a child

Text

node.
**Returns:** A new

HTMLDocument

object.

Method Detail

- createHTMLDocument

```java
HTMLDocument
createHTMLDocument​(
String
title)
```

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

**Parameters:** title

- The title of the document to be set as the content of the

TITLE

element, through a child

Text

node.
**Returns:** A new

HTMLDocument

object.

---

#### Method Detail

createHTMLDocument

```java
HTMLDocument
createHTMLDocument​(
String
title)
```

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

**Parameters:** title

- The title of the document to be set as the content of the

TITLE

element, through a child

Text

node.
**Returns:** A new

HTMLDocument

object.

---

#### createHTMLDocument

HTMLDocument

createHTMLDocument​(

String

title)

Creates an

HTMLDocument

object with the minimal tree made
of the following elements:

HTML

,

HEAD

,

TITLE

, and

BODY

.

---

