# Interface CSSStyleRule

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSStyleRule.html`

### Class Description

```java
public interface
CSSStyleRule

extends
CSSRule
```

The

CSSStyleRule

interface represents a single rule set in a
CSS style sheet.

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

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

---

#### void setSelectorText​(
String
selectorText)
throws
DOMException

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

---

#### CSSStyleDeclaration
getStyle()

The declaration-block of this rule set.

---

### Additional Sections

#### Interface CSSStyleRule

**All Superinterfaces:** CSSRule

```java
public interface
CSSStyleRule

extends
CSSRule
```

The

CSSStyleRule

interface represents a single rule set in a
CSS style sheet.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSStyleRule

extends

CSSRule

The

CSSStyleRule

interface represents a single rule set in a
CSS style sheet.

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

The textual representation of the selector for the rule set.

CSSStyleDeclaration

getStyle

()

The declaration-block of this rule set.

void

setSelectorText

​(

String

selectorText)

The textual representation of the selector for the rule set.

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

The textual representation of the selector for the rule set.

CSSStyleDeclaration

getStyle

()

The declaration-block of this rule set.

void

setSelectorText

​(

String

selectorText)

The textual representation of the selector for the rule set.

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

The textual representation of the selector for the rule set.

The declaration-block of this rule set.

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

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

- setSelectorText

```java
void setSelectorText​(
String
selectorText)
throws
DOMException
```

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

- getStyle

```java
CSSStyleDeclaration
getStyle()
```

The declaration-block of this rule set.

Method Detail

- getSelectorText

```java
String
getSelectorText()
```

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

- setSelectorText

```java
void setSelectorText​(
String
selectorText)
throws
DOMException
```

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this rule is readonly.

- getStyle

```java
CSSStyleDeclaration
getStyle()
```

The declaration-block of this rule set.

---

#### Method Detail

getSelectorText

```java
String
getSelectorText()
```

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

---

#### getSelectorText

String

getSelectorText()

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

setSelectorText

```java
void setSelectorText​(
String
selectorText)
throws
DOMException
```

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

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

The textual representation of the selector for the rule set. The
implementation may have stripped out insignificant whitespace while
parsing the selector.

getStyle

```java
CSSStyleDeclaration
getStyle()
```

The declaration-block of this rule set.

---

#### getStyle

CSSStyleDeclaration

getStyle()

The declaration-block of this rule set.

---

