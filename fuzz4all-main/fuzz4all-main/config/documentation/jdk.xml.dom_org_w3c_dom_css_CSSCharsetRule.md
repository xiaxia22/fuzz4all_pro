# Interface CSSCharsetRule

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSCharsetRule.html`

### Class Description

```java
public interface
CSSCharsetRule

extends
CSSRule
```

The

CSSCharsetRule

interface represents a @charset rule in a
CSS style sheet. The value of the

encoding

attribute does
not affect the encoding of text data in the DOM objects; this encoding is
always UTF-16. After a stylesheet is loaded, the value of the

encoding

attribute is the value found in the

@charset

rule. If there was no

@charset

in the
original document, then no

CSSCharsetRule

is created. The
value of the

encoding

attribute may also be used as a hint
for the encoding used on serialization of the style sheet.

The value of the @charset rule (and therefore of the

CSSCharsetRule

) may not correspond to the encoding the
document actually came in; character encoding information e.g. in an HTTP
header, has priority (see CSS document representation) but this is not
reflected in the

CSSCharsetRule

.

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
getEncoding()

The encoding information used in this

@charset

rule.

---

#### void setEncoding​(
String
encoding)
throws
DOMException

The encoding information used in this

@charset

rule.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified encoding value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this encoding rule is
readonly.

---

### Additional Sections

#### Interface CSSCharsetRule

**All Superinterfaces:** CSSRule

```java
public interface
CSSCharsetRule

extends
CSSRule
```

The

CSSCharsetRule

interface represents a @charset rule in a
CSS style sheet. The value of the

encoding

attribute does
not affect the encoding of text data in the DOM objects; this encoding is
always UTF-16. After a stylesheet is loaded, the value of the

encoding

attribute is the value found in the

@charset

rule. If there was no

@charset

in the
original document, then no

CSSCharsetRule

is created. The
value of the

encoding

attribute may also be used as a hint
for the encoding used on serialization of the style sheet.

The value of the @charset rule (and therefore of the

CSSCharsetRule

) may not correspond to the encoding the
document actually came in; character encoding information e.g. in an HTTP
header, has priority (see CSS document representation) but this is not
reflected in the

CSSCharsetRule

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSCharsetRule

extends

CSSRule

The

CSSCharsetRule

interface represents a @charset rule in a
CSS style sheet. The value of the

encoding

attribute does
not affect the encoding of text data in the DOM objects; this encoding is
always UTF-16. After a stylesheet is loaded, the value of the

encoding

attribute is the value found in the

@charset

rule. If there was no

@charset

in the
original document, then no

CSSCharsetRule

is created. The
value of the

encoding

attribute may also be used as a hint
for the encoding used on serialization of the style sheet.

The value of the @charset rule (and therefore of the

CSSCharsetRule

) may not correspond to the encoding the
document actually came in; character encoding information e.g. in an HTTP
header, has priority (see CSS document representation) but this is not
reflected in the

CSSCharsetRule

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The value of the @charset rule (and therefore of the

CSSCharsetRule

) may not correspond to the encoding the
document actually came in; character encoding information e.g. in an HTTP
header, has priority (see CSS document representation) but this is not
reflected in the

CSSCharsetRule

.

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

getEncoding

()

The encoding information used in this

@charset

rule.

void

setEncoding

​(

String

encoding)

The encoding information used in this

@charset

rule.

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

getEncoding

()

The encoding information used in this

@charset

rule.

void

setEncoding

​(

String

encoding)

The encoding information used in this

@charset

rule.

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

The encoding information used in this

@charset

rule.

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

- getEncoding

```java
String
getEncoding()
```

The encoding information used in this

@charset

rule.

- setEncoding

```java
void setEncoding​(
String
encoding)
throws
DOMException
```

The encoding information used in this

@charset

rule.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified encoding value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this encoding rule is
readonly.

Method Detail

- getEncoding

```java
String
getEncoding()
```

The encoding information used in this

@charset

rule.

- setEncoding

```java
void setEncoding​(
String
encoding)
throws
DOMException
```

The encoding information used in this

@charset

rule.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified encoding value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this encoding rule is
readonly.

---

#### Method Detail

getEncoding

```java
String
getEncoding()
```

The encoding information used in this

@charset

rule.

---

#### getEncoding

String

getEncoding()

The encoding information used in this

@charset

rule.

setEncoding

```java
void setEncoding​(
String
encoding)
throws
DOMException
```

The encoding information used in this

@charset

rule.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified encoding value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this encoding rule is
readonly.

---

#### setEncoding

void setEncoding​(

String

encoding)
throws

DOMException

The encoding information used in this

@charset

rule.

---

