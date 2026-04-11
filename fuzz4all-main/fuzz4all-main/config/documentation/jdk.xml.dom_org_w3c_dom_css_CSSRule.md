# Interface CSSRule

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSRule.html`

### Class Description

```java
public interface
CSSRule
```

The

CSSRule

interface is the abstract base interface for any
type of CSS statement. This includes both rule sets and at-rules. An
implementation is expected to preserve all rules specified in a CSS style
sheet, even if the rule is not recognized by the parser. Unrecognized
rules are represented using the

CSSUnknownRule

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Known Subinterfaces:** CSSCharsetRule

,

CSSFontFaceRule

,

CSSImportRule

,

CSSMediaRule

,

CSSPageRule

,

CSSStyleRule

,

CSSUnknownRule

---

### Field Details

#### static final short UNKNOWN_RULE

The rule is a

CSSUnknownRule

.

**See Also:**
- Constant Field Values

---

#### static final short STYLE_RULE

The rule is a

CSSStyleRule

.

**See Also:**
- Constant Field Values

---

#### static final short CHARSET_RULE

The rule is a

CSSCharsetRule

.

**See Also:**
- Constant Field Values

---

#### static final short IMPORT_RULE

The rule is a

CSSImportRule

.

**See Also:**
- Constant Field Values

---

#### static final short MEDIA_RULE

The rule is a

CSSMediaRule

.

**See Also:**
- Constant Field Values

---

#### static final short FONT_FACE_RULE

The rule is a

CSSFontFaceRule

.

**See Also:**
- Constant Field Values

---

#### static final short PAGE_RULE

The rule is a

CSSPageRule

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### short getType()

The type of the rule, as defined above. The expectation is that
binding-specific casting methods can be used to cast down from an
instance of the

CSSRule

interface to the specific
derived interface implied by the

type

.

---

#### String
getCssText()

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

---

#### void setCssText​(
String
cssText)
throws
DOMException

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of rule than the current one.

HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at
this point in the style sheet.

NO_MODIFICATION_ALLOWED_ERR: Raised if the rule is readonly.

---

#### CSSStyleSheet
getParentStyleSheet()

The style sheet that contains this rule.

---

#### CSSRule
getParentRule()

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule. If this rule is
not nested inside any other rules, this returns

null

.

---

### Additional Sections

#### Interface CSSRule

**All Known Subinterfaces:** CSSCharsetRule

,

CSSFontFaceRule

,

CSSImportRule

,

CSSMediaRule

,

CSSPageRule

,

CSSStyleRule

,

CSSUnknownRule

```java
public interface
CSSRule
```

The

CSSRule

interface is the abstract base interface for any
type of CSS statement. This includes both rule sets and at-rules. An
implementation is expected to preserve all rules specified in a CSS style
sheet, even if the rule is not recognized by the parser. Unrecognized
rules are represented using the

CSSUnknownRule

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSRule

The

CSSRule

interface is the abstract base interface for any
type of CSS statement. This includes both rule sets and at-rules. An
implementation is expected to preserve all rules specified in a CSS style
sheet, even if the rule is not recognized by the parser. Unrecognized
rules are represented using the

CSSUnknownRule

interface.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

CHARSET_RULE

The rule is a

CSSCharsetRule

.

static short

FONT_FACE_RULE

The rule is a

CSSFontFaceRule

.

static short

IMPORT_RULE

The rule is a

CSSImportRule

.

static short

MEDIA_RULE

The rule is a

CSSMediaRule

.

static short

PAGE_RULE

The rule is a

CSSPageRule

.

static short

STYLE_RULE

The rule is a

CSSStyleRule

.

static short

UNKNOWN_RULE

The rule is a

CSSUnknownRule

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCssText

()

The parsable textual representation of the rule.

CSSRule

getParentRule

()

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule.

CSSStyleSheet

getParentStyleSheet

()

The style sheet that contains this rule.

short

getType

()

The type of the rule, as defined above.

void

setCssText

​(

String

cssText)

The parsable textual representation of the rule.

Field Summary

Fields

Modifier and Type

Field

Description

static short

CHARSET_RULE

The rule is a

CSSCharsetRule

.

static short

FONT_FACE_RULE

The rule is a

CSSFontFaceRule

.

static short

IMPORT_RULE

The rule is a

CSSImportRule

.

static short

MEDIA_RULE

The rule is a

CSSMediaRule

.

static short

PAGE_RULE

The rule is a

CSSPageRule

.

static short

STYLE_RULE

The rule is a

CSSStyleRule

.

static short

UNKNOWN_RULE

The rule is a

CSSUnknownRule

.

---

#### Field Summary

The rule is a

CSSCharsetRule

.

The rule is a

CSSFontFaceRule

.

The rule is a

CSSImportRule

.

The rule is a

CSSMediaRule

.

The rule is a

CSSPageRule

.

The rule is a

CSSStyleRule

.

The rule is a

CSSUnknownRule

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCssText

()

The parsable textual representation of the rule.

CSSRule

getParentRule

()

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule.

CSSStyleSheet

getParentStyleSheet

()

The style sheet that contains this rule.

short

getType

()

The type of the rule, as defined above.

void

setCssText

​(

String

cssText)

The parsable textual representation of the rule.

---

#### Method Summary

The parsable textual representation of the rule.

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule.

The style sheet that contains this rule.

The type of the rule, as defined above.

============ FIELD DETAIL ===========

- Field Detail

- UNKNOWN_RULE

```java
static final short UNKNOWN_RULE
```

The rule is a

CSSUnknownRule

.

**See Also:** Constant Field Values

- STYLE_RULE

```java
static final short STYLE_RULE
```

The rule is a

CSSStyleRule

.

**See Also:** Constant Field Values

- CHARSET_RULE

```java
static final short CHARSET_RULE
```

The rule is a

CSSCharsetRule

.

**See Also:** Constant Field Values

- IMPORT_RULE

```java
static final short IMPORT_RULE
```

The rule is a

CSSImportRule

.

**See Also:** Constant Field Values

- MEDIA_RULE

```java
static final short MEDIA_RULE
```

The rule is a

CSSMediaRule

.

**See Also:** Constant Field Values

- FONT_FACE_RULE

```java
static final short FONT_FACE_RULE
```

The rule is a

CSSFontFaceRule

.

**See Also:** Constant Field Values

- PAGE_RULE

```java
static final short PAGE_RULE
```

The rule is a

CSSPageRule

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
short getType()
```

The type of the rule, as defined above. The expectation is that
binding-specific casting methods can be used to cast down from an
instance of the

CSSRule

interface to the specific
derived interface implied by the

type

.

- getCssText

```java
String
getCssText()
```

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

- setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of rule than the current one.

HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at
this point in the style sheet.

NO_MODIFICATION_ALLOWED_ERR: Raised if the rule is readonly.

- getParentStyleSheet

```java
CSSStyleSheet
getParentStyleSheet()
```

The style sheet that contains this rule.

- getParentRule

```java
CSSRule
getParentRule()
```

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule. If this rule is
not nested inside any other rules, this returns

null

.

Field Detail

- UNKNOWN_RULE

```java
static final short UNKNOWN_RULE
```

The rule is a

CSSUnknownRule

.

**See Also:** Constant Field Values

- STYLE_RULE

```java
static final short STYLE_RULE
```

The rule is a

CSSStyleRule

.

**See Also:** Constant Field Values

- CHARSET_RULE

```java
static final short CHARSET_RULE
```

The rule is a

CSSCharsetRule

.

**See Also:** Constant Field Values

- IMPORT_RULE

```java
static final short IMPORT_RULE
```

The rule is a

CSSImportRule

.

**See Also:** Constant Field Values

- MEDIA_RULE

```java
static final short MEDIA_RULE
```

The rule is a

CSSMediaRule

.

**See Also:** Constant Field Values

- FONT_FACE_RULE

```java
static final short FONT_FACE_RULE
```

The rule is a

CSSFontFaceRule

.

**See Also:** Constant Field Values

- PAGE_RULE

```java
static final short PAGE_RULE
```

The rule is a

CSSPageRule

.

**See Also:** Constant Field Values

---

#### Field Detail

UNKNOWN_RULE

```java
static final short UNKNOWN_RULE
```

The rule is a

CSSUnknownRule

.

**See Also:** Constant Field Values

---

#### UNKNOWN_RULE

static final short UNKNOWN_RULE

The rule is a

CSSUnknownRule

.

STYLE_RULE

```java
static final short STYLE_RULE
```

The rule is a

CSSStyleRule

.

**See Also:** Constant Field Values

---

#### STYLE_RULE

static final short STYLE_RULE

The rule is a

CSSStyleRule

.

CHARSET_RULE

```java
static final short CHARSET_RULE
```

The rule is a

CSSCharsetRule

.

**See Also:** Constant Field Values

---

#### CHARSET_RULE

static final short CHARSET_RULE

The rule is a

CSSCharsetRule

.

IMPORT_RULE

```java
static final short IMPORT_RULE
```

The rule is a

CSSImportRule

.

**See Also:** Constant Field Values

---

#### IMPORT_RULE

static final short IMPORT_RULE

The rule is a

CSSImportRule

.

MEDIA_RULE

```java
static final short MEDIA_RULE
```

The rule is a

CSSMediaRule

.

**See Also:** Constant Field Values

---

#### MEDIA_RULE

static final short MEDIA_RULE

The rule is a

CSSMediaRule

.

FONT_FACE_RULE

```java
static final short FONT_FACE_RULE
```

The rule is a

CSSFontFaceRule

.

**See Also:** Constant Field Values

---

#### FONT_FACE_RULE

static final short FONT_FACE_RULE

The rule is a

CSSFontFaceRule

.

PAGE_RULE

```java
static final short PAGE_RULE
```

The rule is a

CSSPageRule

.

**See Also:** Constant Field Values

---

#### PAGE_RULE

static final short PAGE_RULE

The rule is a

CSSPageRule

.

Method Detail

- getType

```java
short getType()
```

The type of the rule, as defined above. The expectation is that
binding-specific casting methods can be used to cast down from an
instance of the

CSSRule

interface to the specific
derived interface implied by the

type

.

- getCssText

```java
String
getCssText()
```

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

- setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of rule than the current one.

HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at
this point in the style sheet.

NO_MODIFICATION_ALLOWED_ERR: Raised if the rule is readonly.

- getParentStyleSheet

```java
CSSStyleSheet
getParentStyleSheet()
```

The style sheet that contains this rule.

- getParentRule

```java
CSSRule
getParentRule()
```

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule. If this rule is
not nested inside any other rules, this returns

null

.

---

#### Method Detail

getType

```java
short getType()
```

The type of the rule, as defined above. The expectation is that
binding-specific casting methods can be used to cast down from an
instance of the

CSSRule

interface to the specific
derived interface implied by the

type

.

---

#### getType

short getType()

The type of the rule, as defined above. The expectation is that
binding-specific casting methods can be used to cast down from an
instance of the

CSSRule

interface to the specific
derived interface implied by the

type

.

getCssText

```java
String
getCssText()
```

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

---

#### getCssText

String

getCssText()

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

setCssText

```java
void setCssText​(
String
cssText)
throws
DOMException
```

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified CSS string value has a syntax
error and is unparsable.

INVALID_MODIFICATION_ERR: Raised if the specified CSS string
value represents a different type of rule than the current one.

HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at
this point in the style sheet.

NO_MODIFICATION_ALLOWED_ERR: Raised if the rule is readonly.

---

#### setCssText

void setCssText​(

String

cssText)
throws

DOMException

The parsable textual representation of the rule. This reflects the
current state of the rule and not its initial value.

getParentStyleSheet

```java
CSSStyleSheet
getParentStyleSheet()
```

The style sheet that contains this rule.

---

#### getParentStyleSheet

CSSStyleSheet

getParentStyleSheet()

The style sheet that contains this rule.

getParentRule

```java
CSSRule
getParentRule()
```

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule. If this rule is
not nested inside any other rules, this returns

null

.

---

#### getParentRule

CSSRule

getParentRule()

If this rule is contained inside another rule (e.g. a style rule
inside an @media block), this is the containing rule. If this rule is
not nested inside any other rules, this returns

null

.

---

