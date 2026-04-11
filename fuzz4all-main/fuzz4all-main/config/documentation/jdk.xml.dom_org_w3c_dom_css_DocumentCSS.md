# Interface DocumentCSS

**Source:** `jdk.xml.dom\org\w3c\dom\css\DocumentCSS.html`

### Class Description

```java
public interface
DocumentCSS

extends
DocumentStyle
```

This interface represents a document with a CSS view.

The

getOverrideStyle

method provides a mechanism through
which a DOM author could effect immediate change to the style of an
element without modifying the explicitly linked style sheets of a
document or the inline style of elements in the style sheets. This style
sheet comes after the author style sheet in the cascade algorithm and is
called override style sheet. The override style sheet takes precedence
over author style sheets. An "!important" declaration still takes
precedence over a normal declaration. Override, author, and user style
sheets all may contain "!important" declarations. User "!important" rules
take precedence over both override and author "!important" rules, and
override "!important" rules take precedence over author "!important"
rules.

The expectation is that an instance of the

DocumentCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** DocumentStyle

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CSSStyleDeclaration
getOverrideStyle​(
Element
elt,

String
pseudoElt)

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

**Parameters:**
- elt

- The element whose style is to be modified. This parameter
cannot be null.
- pseudoElt

- The pseudo-element or

null

if none.

**Returns:**
- The override style declaration.

---

### Additional Sections

#### Interface DocumentCSS

**All Superinterfaces:** DocumentStyle

```java
public interface
DocumentCSS

extends
DocumentStyle
```

This interface represents a document with a CSS view.

The

getOverrideStyle

method provides a mechanism through
which a DOM author could effect immediate change to the style of an
element without modifying the explicitly linked style sheets of a
document or the inline style of elements in the style sheets. This style
sheet comes after the author style sheet in the cascade algorithm and is
called override style sheet. The override style sheet takes precedence
over author style sheets. An "!important" declaration still takes
precedence over a normal declaration. Override, author, and user style
sheets all may contain "!important" declarations. User "!important" rules
take precedence over both override and author "!important" rules, and
override "!important" rules take precedence over author "!important"
rules.

The expectation is that an instance of the

DocumentCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

DocumentCSS

extends

DocumentStyle

This interface represents a document with a CSS view.

The

getOverrideStyle

method provides a mechanism through
which a DOM author could effect immediate change to the style of an
element without modifying the explicitly linked style sheets of a
document or the inline style of elements in the style sheets. This style
sheet comes after the author style sheet in the cascade algorithm and is
called override style sheet. The override style sheet takes precedence
over author style sheets. An "!important" declaration still takes
precedence over a normal declaration. Override, author, and user style
sheets all may contain "!important" declarations. User "!important" rules
take precedence over both override and author "!important" rules, and
override "!important" rules take precedence over author "!important"
rules.

The expectation is that an instance of the

DocumentCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The

getOverrideStyle

method provides a mechanism through
which a DOM author could effect immediate change to the style of an
element without modifying the explicitly linked style sheets of a
document or the inline style of elements in the style sheets. This style
sheet comes after the author style sheet in the cascade algorithm and is
called override style sheet. The override style sheet takes precedence
over author style sheets. An "!important" declaration still takes
precedence over a normal declaration. Override, author, and user style
sheets all may contain "!important" declarations. User "!important" rules
take precedence over both override and author "!important" rules, and
override "!important" rules take precedence over author "!important"
rules.

The expectation is that an instance of the

DocumentCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

Document

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The expectation is that an instance of the

DocumentCSS

interface can be obtained by using binding-specific casting methods on an
instance of the

Document

interface.

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

getOverrideStyle

​(

Element

elt,

String

pseudoElt)

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

- Methods declared in interface org.w3c.dom.stylesheets.

DocumentStyle

getStyleSheets

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CSSStyleDeclaration

getOverrideStyle

​(

Element

elt,

String

pseudoElt)

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

- Methods declared in interface org.w3c.dom.stylesheets.

DocumentStyle

getStyleSheets

---

#### Method Summary

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

Methods declared in interface org.w3c.dom.stylesheets.

DocumentStyle

getStyleSheets

---

#### Methods declared in interface org.w3c.dom.stylesheets. DocumentStyle

============ METHOD DETAIL ==========

- Method Detail

- getOverrideStyle

```java
CSSStyleDeclaration
getOverrideStyle​(
Element
elt,

String
pseudoElt)
```

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

**Parameters:** elt

- The element whose style is to be modified. This parameter
cannot be null.
**Parameters:** pseudoElt

- The pseudo-element or

null

if none.
**Returns:** The override style declaration.

Method Detail

- getOverrideStyle

```java
CSSStyleDeclaration
getOverrideStyle​(
Element
elt,

String
pseudoElt)
```

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

**Parameters:** elt

- The element whose style is to be modified. This parameter
cannot be null.
**Parameters:** pseudoElt

- The pseudo-element or

null

if none.
**Returns:** The override style declaration.

---

#### Method Detail

getOverrideStyle

```java
CSSStyleDeclaration
getOverrideStyle​(
Element
elt,

String
pseudoElt)
```

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

**Parameters:** elt

- The element whose style is to be modified. This parameter
cannot be null.
**Parameters:** pseudoElt

- The pseudo-element or

null

if none.
**Returns:** The override style declaration.

---

#### getOverrideStyle

CSSStyleDeclaration

getOverrideStyle​(

Element

elt,

String

pseudoElt)

This method is used to retrieve the override style declaration for a
specified element and a specified pseudo-element.

---

