# Interface ViewCSS

**Source:** `jdk.xml.dom\org\w3c\dom\css\ViewCSS.html`

### Class Description

```java
public interface
ViewCSS

extends
AbstractView
```

This interface represents a CSS view. The

getComputedStyle

method provides a read only access to the computed values of an element.

The expectation is that an instance of the

ViewCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

AbstractView

interface.

Since a computed style is related to an

Element

node, if
this element is removed from the document, the associated

CSSStyleDeclaration

and

CSSValue

related to
this declaration are no longer valid.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** AbstractView

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CSSStyleDeclaration
getComputedStyle​(
Element
elt,

String
pseudoElt)

This method is used to get the computed style as it is defined in [

CSS2

].

**Parameters:**
- elt

- The element whose style is to be computed. This parameter
cannot be null.
- pseudoElt

- The pseudo-element or

null

if none.

**Returns:**
- The computed style. The

CSSStyleDeclaration

is
read-only and contains only absolute values.

---

### Additional Sections

#### Interface ViewCSS

**All Superinterfaces:** AbstractView

```java
public interface
ViewCSS

extends
AbstractView
```

This interface represents a CSS view. The

getComputedStyle

method provides a read only access to the computed values of an element.

The expectation is that an instance of the

ViewCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

AbstractView

interface.

Since a computed style is related to an

Element

node, if
this element is removed from the document, the associated

CSSStyleDeclaration

and

CSSValue

related to
this declaration are no longer valid.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

ViewCSS

extends

AbstractView

This interface represents a CSS view. The

getComputedStyle

method provides a read only access to the computed values of an element.

The expectation is that an instance of the

ViewCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

AbstractView

interface.

Since a computed style is related to an

Element

node, if
this element is removed from the document, the associated

CSSStyleDeclaration

and

CSSValue

related to
this declaration are no longer valid.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The expectation is that an instance of the

ViewCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

AbstractView

interface.

Since a computed style is related to an

Element

node, if
this element is removed from the document, the associated

CSSStyleDeclaration

and

CSSValue

related to
this declaration are no longer valid.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

Since a computed style is related to an

Element

node, if
this element is removed from the document, the associated

CSSStyleDeclaration

and

CSSValue

related to
this declaration are no longer valid.

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

CSSStyleDeclaration

getComputedStyle

​(

Element

elt,

String

pseudoElt)

This method is used to get the computed style as it is defined in [

CSS2

].

- Methods declared in interface org.w3c.dom.views.

AbstractView

getDocument

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CSSStyleDeclaration

getComputedStyle

​(

Element

elt,

String

pseudoElt)

This method is used to get the computed style as it is defined in [

CSS2

].

- Methods declared in interface org.w3c.dom.views.

AbstractView

getDocument

---

#### Method Summary

This method is used to get the computed style as it is defined in [

CSS2

].

Methods declared in interface org.w3c.dom.views.

AbstractView

getDocument

---

#### Methods declared in interface org.w3c.dom.views. AbstractView

============ METHOD DETAIL ==========

- Method Detail

- getComputedStyle

```java
CSSStyleDeclaration
getComputedStyle​(
Element
elt,

String
pseudoElt)
```

This method is used to get the computed style as it is defined in [

CSS2

].

**Parameters:** elt

- The element whose style is to be computed. This parameter
cannot be null.
**Parameters:** pseudoElt

- The pseudo-element or

null

if none.
**Returns:** The computed style. The

CSSStyleDeclaration

is
read-only and contains only absolute values.

Method Detail

- getComputedStyle

```java
CSSStyleDeclaration
getComputedStyle​(
Element
elt,

String
pseudoElt)
```

This method is used to get the computed style as it is defined in [

CSS2

].

**Parameters:** elt

- The element whose style is to be computed. This parameter
cannot be null.
**Parameters:** pseudoElt

- The pseudo-element or

null

if none.
**Returns:** The computed style. The

CSSStyleDeclaration

is
read-only and contains only absolute values.

---

#### Method Detail

getComputedStyle

```java
CSSStyleDeclaration
getComputedStyle​(
Element
elt,

String
pseudoElt)
```

This method is used to get the computed style as it is defined in [

CSS2

].

**Parameters:** elt

- The element whose style is to be computed. This parameter
cannot be null.
**Parameters:** pseudoElt

- The pseudo-element or

null

if none.
**Returns:** The computed style. The

CSSStyleDeclaration

is
read-only and contains only absolute values.

---

#### getComputedStyle

CSSStyleDeclaration

getComputedStyle​(

Element

elt,

String

pseudoElt)

This method is used to get the computed style as it is defined in [

CSS2

].

---

