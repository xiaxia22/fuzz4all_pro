# Interface CSSPageRule

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSPageRule.html`

### Class Description

```java
public interface
CSSPageRule

extends
CSSRule
```

The

CSSPageRule

interface represents a @page rule within a
CSS style sheet. The

@page

rule is used to specify the
dimensions, orientation, margins, etc. of a page box for paged media.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** CSSRule

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getSelectorText()

The parsable textual representation of the page selector for the rule.

---

#### void setSelectorText​(
String
selectorText)
throws
DOMException

The parsable textual representation of the page selector for the rule.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

---

#### CSSStyleDeclaration
getStyle()

The declaration-block of this rule.

---

### Additional Sections

#### Interface CSSPageRule

**All Superinterfaces:** CSSRule

```java
public interface
CSSPageRule

extends
CSSRule
```

The

CSSPageRule

interface represents a @page rule within a
CSS style sheet. The

@page

rule is used to specify the
dimensions, orientation, margins, etc. of a page box for paged media.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSPageRule

extends

CSSRule

The

CSSPageRule

interface represents a @page rule within a
CSS style sheet. The

@page

rule is used to specify the
dimensions, orientation, margins, etc. of a page box for paged media.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.css.

CSSRule

CHARSET_RULE

,

FONT_FACE_RULE

,

IMPORT_RULE

,

MEDIA_RULE

,

PAGE_RULE

,

STYLE_RULE

,

UNKNOWN_RULE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getSelectorText

()

The parsable textual representation of the page selector for the rule.

CSSStyleDeclaration

getStyle

()

The declaration-block of this rule.

void

setSelectorText

​(

String

selectorText)

The parsable textual representation of the page selector for the rule.

- Methods declared in interface org.w3c.dom.css.

CSSRule

getCssText

,

getParentRule

,

getParentStyleSheet

,

getType

,

setCssText

Field Summary

- Fields declared in interface org.w3c.dom.css.

CSSRule

CHARSET_RULE

,

FONT_FACE_RULE

,

IMPORT_RULE

,

MEDIA_RULE

,

PAGE_RULE

,

STYLE_RULE

,

UNKNOWN_RULE

---

#### Field Summary

Fields declared in interface org.w3c.dom.css.

CSSRule

CHARSET_RULE

,

FONT_FACE_RULE

,

IMPORT_RULE

,

MEDIA_RULE

,

PAGE_RULE

,

STYLE_RULE

,

UNKNOWN_RULE

---

#### Fields declared in interface org.w3c.dom.css. CSSRule

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getSelectorText

()

The parsable textual representation of the page selector for the rule.

CSSStyleDeclaration

getStyle

()

The declaration-block of this rule.

void

setSelectorText

​(

String

selectorText)

The parsable textual representation of the page selector for the rule.

- Methods declared in interface org.w3c.dom.css.

CSSRule

getCssText

,

getParentRule

,

getParentStyleSheet

,

getType

,

setCssText

---

#### Method Summary

The parsable textual representation of the page selector for the rule.

The declaration-block of this rule.

Methods declared in interface org.w3c.dom.css.

CSSRule

getCssText

,

getParentRule

,

getParentStyleSheet

,

getType

,

setCssText

---

#### Methods declared in interface org.w3c.dom.css. CSSRule

============ METHOD DETAIL ==========

- Method Detail

- getSelectorText

```java
String
getSelectorText()
```

The parsable textual representation of the page selector for the rule.

- setSelectorText

```java
void setSelectorText​(
String
selectorText)
throws
DOMException
```

The parsable textual representation of the page selector for the rule.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

- getStyle

```java
CSSStyleDeclaration
getStyle()
```

The declaration-block of this rule.

Method Detail

- getSelectorText

```java
String
getSelectorText()
```

The parsable textual representation of the page selector for the rule.

- setSelectorText

```java
void setSelectorText​(
String
selectorText)
throws
DOMException
```

The parsable textual representation of the page selector for the rule.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

- getStyle

```java
CSSStyleDeclaration
getStyle()
```

The declaration-block of this rule.

---

#### Method Detail

getSelectorText

```java
String
getSelectorText()
```

The parsable textual representation of the page selector for the rule.

---

#### getSelectorText

String

getSelectorText()

The parsable textual representation of the page selector for the rule.

setSelectorText

```java
void setSelectorText​(
String
selectorText)
throws
DOMException
```

The parsable textual representation of the page selector for the rule.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

---

#### setSelectorText

void setSelectorText​(

String

selectorText)
throws

DOMException

The parsable textual representation of the page selector for the rule.

getStyle

```java
CSSStyleDeclaration
getStyle()
```

The declaration-block of this rule.

---

#### getStyle

CSSStyleDeclaration

getStyle()

The declaration-block of this rule.

---

