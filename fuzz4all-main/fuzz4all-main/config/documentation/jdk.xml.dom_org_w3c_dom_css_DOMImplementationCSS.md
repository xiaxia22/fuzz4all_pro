# Interface DOMImplementationCSS

**Source:** `jdk.xml.dom\org\w3c\dom\css\DOMImplementationCSS.html`

### Class Description

```java
public interface
DOMImplementationCSS

extends
DOMImplementation
```

This interface allows the DOM user to create a

CSSStyleSheet

outside the context of a document. There is no way to associate the new

CSSStyleSheet

with a document in DOM Level 2.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** DOMImplementation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CSSStyleSheet
createCSSStyleSheet​(
String
title,

String
media)
throws
DOMException

Creates a new

CSSStyleSheet

.

**Parameters:**
- title

- The advisory title. See also the section.
- media

- The comma-separated list of media associated with the
new style sheet. See also the section.

**Returns:**
- A new CSS style sheet.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified media string value has a syntax
error and is unparsable.

---

### Additional Sections

#### Interface DOMImplementationCSS

**All Superinterfaces:** DOMImplementation

```java
public interface
DOMImplementationCSS

extends
DOMImplementation
```

This interface allows the DOM user to create a

CSSStyleSheet

outside the context of a document. There is no way to associate the new

CSSStyleSheet

with a document in DOM Level 2.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

DOMImplementationCSS

extends

DOMImplementation

This interface allows the DOM user to create a

CSSStyleSheet

outside the context of a document. There is no way to associate the new

CSSStyleSheet

with a document in DOM Level 2.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CSSStyleSheet

createCSSStyleSheet

​(

String

title,

String

media)

Creates a new

CSSStyleSheet

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

CSSStyleSheet

createCSSStyleSheet

​(

String

title,

String

media)

Creates a new

CSSStyleSheet

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

Creates a new

CSSStyleSheet

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

- createCSSStyleSheet

```java
CSSStyleSheet
createCSSStyleSheet​(
String
title,

String
media)
throws
DOMException
```

Creates a new

CSSStyleSheet

.

**Parameters:** title

- The advisory title. See also the section.
**Parameters:** media

- The comma-separated list of media associated with the
new style sheet. See also the section.
**Returns:** A new CSS style sheet.
**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified media string value has a syntax
error and is unparsable.

Method Detail

- createCSSStyleSheet

```java
CSSStyleSheet
createCSSStyleSheet​(
String
title,

String
media)
throws
DOMException
```

Creates a new

CSSStyleSheet

.

**Parameters:** title

- The advisory title. See also the section.
**Parameters:** media

- The comma-separated list of media associated with the
new style sheet. See also the section.
**Returns:** A new CSS style sheet.
**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified media string value has a syntax
error and is unparsable.

---

#### Method Detail

createCSSStyleSheet

```java
CSSStyleSheet
createCSSStyleSheet​(
String
title,

String
media)
throws
DOMException
```

Creates a new

CSSStyleSheet

.

**Parameters:** title

- The advisory title. See also the section.
**Parameters:** media

- The comma-separated list of media associated with the
new style sheet. See also the section.
**Returns:** A new CSS style sheet.
**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified media string value has a syntax
error and is unparsable.

---

#### createCSSStyleSheet

CSSStyleSheet

createCSSStyleSheet​(

String

title,

String

media)
throws

DOMException

Creates a new

CSSStyleSheet

.

---

